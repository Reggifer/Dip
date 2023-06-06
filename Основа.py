# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:44:16 2023

@author: user
"""
# библиотеки для окна

from PyQt5 import QtWidgets, QtGui, QtCore, QtTest
from PyQt5.QtWidgets import QFileDialog, QApplication, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage

import Base_window4
import Podkluchenie_k_datchikam1

# %% основные библиотеки

import matplotlib
from statistics import mean
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import sqlite3
import json
import sys
import time

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

def plot_graph(t, temp, hum, ax=None, line_color_1 = None, line_color_2 = None):
    if ax is None:
        ax = plt
    else:
        ax.clear()
    ax.plot(t, temp, color = line_color_1)
    ax.plot(t, hum, color = line_color_2)


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


# %% основной код приложения


b = Podkluchenie_k_datchikam1.Ui_MainWindow


class Mywindow_small(QtWidgets.QMainWindow, b):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Подключение датчиков')
        self.setupUi(self)

        self.pushButton.clicked.connect(self.prodoljenie)

    def prodoljenie(self):
        self.podcluchenie_k_datchiky()


a = Base_window4.Ui_MainWindow


class Mywindow(QtWidgets.QMainWindow, a):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.active = False

        self.pushButton_2.clicked.connect(self.podcluchenie_k_datchiky)

    def show_window(self):
        window1 = Mywindow_small()
        window1.show()





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
        self.active = True
        while self.active:

            temp = sensor.read_temperature()
            hum = sensor.read_humidity()
            passed_time.append(current_t)

            all_tmp.append(temp)
            all_hum.append(hum)
            cur.execute("insert into sensor (temperature, humidity) values (%d, %d)" % (temp, hum))
            con.commit()

            clear_tmp = clean_data(passed_time, all_tmp)
            clear_hum = clean_data(passed_time, all_hum)

            plot_graph(passed_time, all_tmp, all_hum) # График по сырым Сырые данные

            clear_tmp_smooth = smooth_data(clear_tmp, 3) # Сглаживание
            clear_hum_smooth = smooth_data(clear_hum, 3) # Сглаживание

            plot_graph(passed_time, clear_tmp_smooth, clear_hum_smooth) # График по сглаженным данным

# Сделать аппроксимацию/интерполяцию по сглаженным данным от времени
# Если хватит сил, напиши функцию которая будет возвращать функцию производной, или если не получиться произдводную в точке( но это не обязательно, так общее тх поменялось)

            plt.title("Данные", fontsize=15)

            plt.savefig("temp.png")
            self.label.setPixmap(QtGui.QPixmap("temp.png"))

            QApplication.processEvents()
            QtTest.QTest.qWait(10)
            current_t += 1


try:
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    app.exec_()
except Exception as e:
    print(e)
