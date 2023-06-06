# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maket.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 906)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 680, 281, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 10, 431, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1080, 760, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.raw_data = QtWidgets.QCheckBox(self.centralwidget)
        self.raw_data.setGeometry(QtCore.QRect(724, 300, 161, 17))
        self.raw_data.setObjectName("raw_data")
        self.derivate = QtWidgets.QCheckBox(self.centralwidget)
        self.derivate.setGeometry(QtCore.QRect(724, 330, 171, 21))
        self.derivate.setObjectName("derivate")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 231, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(724, 440, 431, 81))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(1040, 710, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1040, 680, 111, 16))
        self.label_7.setObjectName("label_7")
        self.refliction_of_past_data = QtWidgets.QCheckBox(self.centralwidget)
        self.refliction_of_past_data.setGeometry(QtCore.QRect(724, 370, 181, 16))
        self.refliction_of_past_data.setObjectName("refliction_of_past_data")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(740, 410, 73, 20))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_3.setGeometry(QtCore.QRect(835, 410, 73, 20))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(730, 410, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(818, 410, 16, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(720, 120, 431, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 740, 281, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.smoothing_methods = QtWidgets.QComboBox(self.centralwidget)
        self.smoothing_methods.setGeometry(QtCore.QRect(724, 260, 131, 23))
        self.smoothing_methods.setObjectName("smoothing_methods")
        self.smoothing_methods.addItem("")
        self.smoothing_methods.addItem("")
        self.smoothing_methods.setItemText(1, "")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 260, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(720, 70, 90, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(852, 70, 105, 17))
        self.radioButton.setObjectName("radioButton")
        self.humidity_value = QtWidgets.QLabel(self.centralwidget)
        self.humidity_value.setGeometry(QtCore.QRect(333, 60, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.humidity_value.setFont(font)
        self.humidity_value.setObjectName("humidity_value")
        self.speed_of_parametr_change_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.speed_of_parametr_change_2.setGeometry(QtCore.QRect(438, 60, 111, 101))
        self.speed_of_parametr_change_2.setObjectName("speed_of_parametr_change_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.speed_of_parametr_change_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.speed_of_parametr_change_1.setGeometry(QtCore.QRect(115, 60, 111, 101))
        self.speed_of_parametr_change_1.setObjectName("speed_of_parametr_change_1")
        self.temperature_value = QtWidgets.QLabel(self.centralwidget)
        self.temperature_value.setGeometry(QtCore.QRect(20, 20, 114, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temperature_value.setFont(font)
        self.temperature_value.setObjectName("temperature_value")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(338, 20, 95, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 671, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("temp.jpg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1161, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Скачать данные "))
        self.pushButton_2.setText(_translate("MainWindow", "Подключится к датчику"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))
        self.raw_data.setText(_translate("MainWindow", "Сырые данные"))
        self.derivate.setText(_translate("MainWindow", "Скорости изменения (тренд)"))
        self.label_5.setText(_translate("MainWindow", "Коэфициент благополучия, %"))
        self.label_6.setText(_translate("MainWindow", "Рекомендации :"))
        self.label_7.setText(_translate("MainWindow", "Период скачивания "))
        self.refliction_of_past_data.setText(_translate("MainWindow", "Отображение прошлых данных"))
        self.label_8.setText(_translate("MainWindow", "с"))
        self.label_9.setText(_translate("MainWindow", "по"))
        self.pushButton_5.setText(_translate("MainWindow", "Настройки оповещения"))
        self.pushButton_6.setText(_translate("MainWindow", "Отчет"))
        self.smoothing_methods.setItemText(0, _translate("MainWindow", "Методы сглаживания"))
        self.pushButton_4.setText(_translate("MainWindow", "Настройки"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Тип датчика"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Пробный"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Ардуино"))
        self.radioButton.setText(_translate("MainWindow", "Статус датчика"))
        self.humidity_value.setText(_translate("MainWindow", "50С\""))
        self.label_4.setText(_translate("MainWindow", "50С\""))
        self.temperature_value.setText(_translate("MainWindow", "Температура"))
        self.label_2.setText(_translate("MainWindow", "Влажность"))