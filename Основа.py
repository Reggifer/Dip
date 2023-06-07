# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:44:16 2023

@author: user
"""
# библиотеки для окна

from PyQt5 import QtWidgets, QtGui, QtCore, QtTest
from PyQt5.QtWidgets import QFileDialog, QApplication, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage

import mainwindow


# %% основные библиотеки

import matplotlib as mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import sqlite3
import json
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mpl.style.use("seaborn-whitegrid")

#

con = sqlite3.connect("Data_Sensors.db")  # Основная база данных
cur = con.cursor()  # перемещение по базе данных

cur.execute("""create table if not exists `Data_Sensors` ( 
  date_created datetime, time_created datetime, 
  temperature float,
  humidity float)""")


# Сенсор

class Sensor:
    def __init__(self, filename):
        self.df = None
        self.current_temp_time = 0
        self.current_hum_time = 0

        self.reload_data(filename)

    def reload_data(self, filename):
        df = pd.read_csv(filename, sep=" ", header=None)
        df.columns = ["Дата", "Время", "Темп", "Влаж"]
        df = df.replace("error", np.NaN)  # заменяем все error на NaN
        df = df.fillna("0000.0")  # все NaN заменяем на 0000.0 для индефикации
        df["Время"] = df["Время"].str.slice(start=6)  # делаем сек
        df["Темп"] = df["Темп"].str.slice(start=2, stop=6)  # оставляем только числа
        df["Влаж"] = df["Влаж"].str.slice(start=2, stop=6)  # оставляем только числа
        df.Темп = df.Темп.astype(float)
        df.Влаж = df.Влаж.astype(float)
        self.df = df

    def read_temperature(self):
        temp = self.df['Темп'][self.current_temp_time]
        self.current_temp_time += 1
        if self.current_temp_time >= len(self.df.index):
            return

        return temp

    def read_humidity(self):
        hum = self.df['Влаж'][self.current_hum_time]
        self.current_hum_time += 1
        if self.current_hum_time >= len(self.df.index):  # Сделать так, чтобы прекратилась подача данных
            self.current_hum_time = 0

        return hum


sensor = Sensor('log_temp.log')  # Определяем сенсора


# Обработка графика

def plot_graph(t, temp, hum, ax=None, line_1 = None, line_2 = None, clear = True):
    if ax is None:
        ax = plt
    if clear:
        ax.clear()
    ax.plot(t, temp, color = line_1)
    ax.plot(t, hum, color = line_2)


def clean_data(t, data):
    return data

# Скользящее среднее

def smooth_data(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        start_index = max(0, i - window_size + 1)
        end_index = i + 1
        subset = data[start_index:end_index]
        smoothed_value = sum(subset) / len(subset)
        smoothed_data.append(smoothed_value)
    return smoothed_data

# Ароксимация данных

def find_best_polynomial_degree(t, data, max_degree):
    best_degree = 0
    min_residual = float('inf')

    for degree in range(1, max_degree + 1):
        coeffs = np.polyfit(t, data, degree)
        approx_curve = np.polyval(coeffs, t)
        residuals = data - approx_curve
        squared_residuals = residuals**2
        total_residual = np.sum(squared_residuals)

        if total_residual < min_residual:
            min_residual = total_residual
            best_degree = degree

    return best_degree

def get_data_with_approximation(time, temperature, humidity, max_degree):
    best_temp_degree = find_best_polynomial_degree(time, temperature, max_degree)
    best_hum_degree = find_best_polynomial_degree(time, humidity, max_degree)

    temp_coeffs = np.polyfit(time, temperature, best_temp_degree)
    hum_coeffs = np.polyfit(time, humidity, best_hum_degree)

    approx_temp = np.polyval(temp_coeffs, time)
    approx_hum = np.polyval(hum_coeffs, time)

    return approx_temp, approx_hum


# %% основной код приложения

a = mainwindow.Ui_MainWindow


class Mywindow(QtWidgets.QMainWindow, a):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.active = False

        self.pushButton_2.clicked.connect(self.podcluchenie_k_datchiky)

        self.pushButton_3.clicked.connect(self.vixod)

        self.End.clicked.connect(self.zavershenie)

    def zavershenie(self):
        self.active = False
    def vixod(self):
        self.active = False
        self.close()

    def podcluchenie_k_datchiky(self):

        con = sqlite3.connect("sensor.db")
        cur = con.cursor()
        cur.execute("""create table if not exists `sensor` ( 
          date_created datetime default current_timestamp, 
          temperature float,
          humidity float)""")

        current_t = 0
        passed_time = []
        all_tmp = []
        all_hum = []

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        raw_d = self.raw_data.isChecked()
        self.active = True
        while self.active:

            temp = sensor.read_temperature()
            hum = sensor.read_humidity()
            passed_time.append(current_t)
            # Проверяем, достигла ли температура заданного уровня
            if temp >= int(self.lineEdit_2.text()):
                # Отправляем уведомление на почту
                try:
                    send_email('Температура достигла порога', 'Текущая температура: {} градусов'.format(temp),
                           's-kolcov@bk.ru', self.lineEdit.text())
                except Exception as e:
                    pass

            self.label_4.setText(f"{temp}C" )
            self.humidity_value.setText(f"{hum}%")

            all_tmp.append(temp)
            all_hum.append(hum)
            cur.execute("insert into sensor (temperature, humidity) values (%d, %d)" % (temp, hum))
            con.commit()

            clear_tmp = clean_data(passed_time, all_tmp)
            clear_hum = clean_data(passed_time, all_hum)
            if raw_d == True:
                plot_graph(passed_time, all_tmp, all_hum, ax = ax, line_1 = "#FF4500", line_2 = "#3D2B1F") # График по сырым Сырые данные

            clear_tmp_smooth = smooth_data(clear_tmp, 3) # Сглаживание
            clear_hum_smooth = smooth_data(clear_hum, 3) # Сглаживание

            #plot_graph(passed_time, clear_tmp_smooth, clear_hum_smooth, line_1 = "#FF851B", line_2 = "#7D4627") # График по сглаженным данным

            if current_t >= 3:
                clear_tmp_smooth_approx, clear_hum_smooth_approx = get_data_with_approximation(passed_time, clear_tmp_smooth,clear_hum_smooth, 5)
                if raw_d == True:
                    plot_graph(passed_time, clear_tmp_smooth_approx, clear_hum_smooth_approx, ax = ax, line_1 = "red", line_2 = "blue", clear = False)
                if raw_d == False:
                    plot_graph(passed_time, clear_tmp_smooth_approx, clear_hum_smooth_approx, ax=ax, line_1="red", line_2="blue", clear = True)
            plt.title("Данные", fontsize=15)

            plt.savefig("temp.png")
            self.label.setPixmap(QtGui.QPixmap("temp.png"))

            QApplication.processEvents()
            QtTest.QTest.qWait(1000)
            current_t += 1


# Функция для отправки уведомления на почту
def send_email(subject, message, from_email, to_email):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Создаем SMTP объект
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    # Авторизуемся на сервере
    server.login('s-kolcov@bk.ru', 'efae3HDG0xNDAAdrRxEe')

    # Отправляем сообщение
    server.sendmail('s-kolcov@bk.ru', to_email, msg.as_string())
    server.quit()


app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
app.exec_()

