# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:44:16 2023

@author: user
"""
# библиотеки для окна

from PyQt5 import QtWidgets, QtGui, QtCore, QtTest
from PyQt5.QtWidgets import QFileDialog, QApplication, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import Qt
import Base_window4
import Podkluchenie_k_datchikam1

# %% основные библиотеки

import matplotlib
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

def plot_graph(t, temp, hum, ax=None):
    if ax is None:
        ax = plt
    else:
        ax.clear()
    ax.plot(t, temp)
    ax.plot(t, hum)


def clean_data(t, data):
    return data


# %% основной код приложения


b = Podkluchenie_k_datchikam1.Ui_MainWindow


class Mywindow_small(QtWidgets.QMainWindow, b):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Подключение датчиков')
        self.setupUi(self)

        self.pushButton.clicked.connect(self.prin_sensors)

    def prin_sensors(self):  # Подключение датчиков
        Var = []
        chek1 = self.checkBox.isChecked()
        chek2 = self.checkBox_2.isChecked()

        if chek1 == True and chek2 == True:
            value1 = self.comboBox.currentText()
            value2 = self.comboBox_2.currentText()

            if value1 == "Пробный" and value2 == "Пробный":
                var1 = 1
                var2 = 1
                Var.append(var1, var2)

            elif value1 == "DS18B20" and value2 == "DS18B20":
                var1 = 2
                var2 = 2
                Var.append(var1, var2)

            elif value1 == "DHT11" and value2 == "DHT11":
                var1 = 3
                var2 = 3
                Var.append(var1, var2)

            elif value1 == "Пробный" and value2 == "DS18B20" or value1 == "DS18B20" and value2 == "Пробный":
                var1 = 1
                var2 = 2
                Var.append(var1, var2)

            elif value1 == "Пробный" and value2 == "DHT11" or value1 == "DHT11" and value2 == "Пробный":
                var1 = 1
                var2 = 3
                Var.append(var1, var2)

            elif value1 == "DS18B20" and value2 == "DHT11" or value1 == "DHT11" and value2 == "DS18B20":
                var1 = 2
                var2 = 3
                Var.append(var1, var2)


        elif chek1 == True and chek2 != True or chek2 == True and chek1 != True:
            value1 = self.comboBox.currentText()
            value2 = self.comboBox_2.currentText()

            if value1 == "Пробный" or value2 == "Пробный":
                var = 1
                Var.append(var)

            elif value1 == "DS18B20" or value2 == "DS18B20":
                var = 2
                Var.append(var)

            elif value1 == "DHT11" or value2 == "DHT11":
                var = 3
                Var.append(var)

        self.accept()
        self.close()
        sys.exit(app.exec_())


a = Base_window4.Ui_MainWindow


class Mywindow(QtWidgets.QMainWindow, a):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.active = False
        self.pushButton_2.clicked.connect(self.podcluchenie_k_datchiky)

    def podcluchenie_k_datchiky(self, Var=None):

        #window1 = Mywindow_small()
        #window1.show()
        #app.exec_()


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
        #if Var == [1, 1]:
            temp = sensor.read_temperature()
            hum = sensor.read_humidity()
            passed_time.append(current_t)

            all_tmp.append(temp)
            all_hum.append(hum)
            cur.execute("insert into sensor (temperature, humidity) values (%d, %d)" % (temp, hum))
            con.commit()
            clear_tmp = clean_data(passed_time, all_tmp)
            clear_hum = clean_data(passed_time, all_hum)
            plot_graph(passed_time, all_tmp, all_hum)
            plot_graph(passed_time, clear_tmp, clear_hum)

            plt.title("Данные", fontsize=15)

            plt.savefig("temp.png")
            self.label.setPixmap(QtGui.QPixmap("temp.png"))

            QApplication.processEvents()
            QtTest.QTest.qWait(1000)
            current_t += 1


try:
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    app.exec_()
except Exception as e:
    print(e)
