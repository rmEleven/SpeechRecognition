# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDesktopWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        '''设置主窗口属性'''
        # 为主窗口设置对象名称
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # 设置主窗口的背景色
        MainWindow.setStyleSheet("background-color: #24292e;")


        '''设置中央窗口部件'''
        # 创建一个中央部件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # 为中央部件设置了一个对象名称
        self.centralwidget.setObjectName("centralwidget")


        '''创建用于显示 GIF 动画的 QLabel 部件 voiceFig'''
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(300, 50, 160, 200))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/play.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")


        '''创建用于显示文本的 QLabel 部件 label'''
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label")
        self.label_1.setWordWrap(True)
        # 设置位置和大小
        self.label_1.setGeometry(QtCore.QRect(250, 250, 300, 50))
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: #c0c0c0;")

        
        '''创建用于显示文本的 QLabel 部件 label_2'''
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)
        # 设置位置和大小
        self.label_2.setGeometry(QtCore.QRect(100, 300, 500, 30))
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #c0c0c0;")


        '''创建用于显示文本的 QLabel 部件 label_3'''
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")  # 设置 label_3 的对象名称
        self.label_3.setWordWrap(True)         # 设置 label_3 的文本自动换行
        # 设置位置和大小
        self.label_3.setGeometry(QtCore.QRect(100, 350, 600, 50))
        # 设置字体
        font = QtGui.QFont()              # 创建字体对象 font
        font.setFamily("Segoe UI")        # 设置字体家族为 "Segoe UI"
        font.setPointSize(14)             # 设置字体大小为 14
        font.setWeight(QtGui.QFont.Bold)  # 设置字体加粗
        self.label_3.setFont(font)        # 将 font 对象应用到 label_3 上
        # 设置 label_3 的样式表
        self.label_3.setStyleSheet("color: #c0c0c0; border: 1px solid #c0c0c0; padding: 5px; border-radius: 5px;")
        

        '''创建用于显示文本的 QLabel 部件 label_4'''
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setWordWrap(True)
        # 设置位置和大小
        self.label_4.setGeometry(QtCore.QRect(100, 450, 600, 50))
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setWeight(QtGui.QFont.Bold)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #c0c0c0; border: 1px solid #c0c0c0; padding: 5px; border-radius: 5px;")


        # 设置主窗口的中央部件为 centralwidget
        MainWindow.setCentralWidget(self.centralwidget)


        # 创建状态栏部件
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # 设置窗口标题和文本标签的内容
        self.retranslateUi(MainWindow)


        # 将信号与槽函数连接起来，实现动作响应
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_1.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play Music\""))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
