# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 600, 720))
        self.centralwidget.setObjectName("centralwidget")

        self.inner_widget = QtWidgets.QWidget(self.centralwidget)
        self.inner_widget.setGeometry(QtCore.QRect(0, 0, 600, 720))
        self.inner_widget.setObjectName("inner_widget")

        self.voiceFig = QtWidgets.QLabel(self.inner_widget)
        self.voiceFig.setGeometry(QtCore.QRect(140, 0, 320, 240))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.inner_widget)
        self.label.setGeometry(QtCore.QRect(220, 210, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.inner_widget)
        self.label_2.setGeometry(QtCore.QRect(70, 250, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.inner_widget)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 500, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.inner_widget)
        self.label_4.setGeometry(QtCore.QRect(70, 350, 500, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.inner_widget)
        self.label_5.setGeometry(QtCore.QRect(70, 420, 500, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.inner_widget)
        self.label_6.setGeometry(QtCore.QRect(70, 490, 500, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.user_input_label = QtWidgets.QLabel(self.inner_widget)
        self.user_input_label.setGeometry(QtCore.QRect(100, 560, 400, 140))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.user_input_label.setFont(font)
        self.user_input_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_input_label.setWordWrap(True)
        self.user_input_label.setObjectName("user_input_label")

        self.sound_wave_label = QtWidgets.QLabel(self.centralwidget)
        self.sound_wave_label.setGeometry(QtCore.QRect(60, 720, 480, 80))
        self.sound_wave_label.setText("")
        self.sound_wave_gif = QtGui.QMovie("icon/sound_wave.gif")
        self.sound_wave_label.setMovie(self.sound_wave_gif)
        self.sound_wave_label.setScaledContents(True)
        self.sound_wave_label.setObjectName("sound_wave_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"play music\""))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"open Notepad\""))
        self.label_5.setText(_translate("MainWindow", "3. Adjust system volume by saying \"volume up/down\""))
        self.label_6.setText(_translate("MainWindow", "4. Quit the program by saying \"exit/quit\""))

        self.sound_wave_label.hide()



