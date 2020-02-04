# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimediaWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 3, 2, 1)
        self.widget_2 = QtMultimediaWidgets.QVideoWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 4, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 3)
        self.choose = QtWidgets.QPushButton(self.centralwidget)
        self.choose.setObjectName("choose")
        self.gridLayout_2.addWidget(self.choose, 2, 0, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout_2.addWidget(self.start, 2, 1, 1, 1)
        self.suspend = QtWidgets.QPushButton(self.centralwidget)
        self.suspend.setObjectName("suspend")
        self.gridLayout_2.addWidget(self.suspend, 2, 2, 1, 1)
        self.widget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 30))
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
        self.choose.setText(_translate("MainWindow", "选择文件"))
        self.start.setText(_translate("MainWindow", "▶"))
        self.suspend.setText(_translate("MainWindow", "||"))

        MainWindow.setWindowOpacity(0.9)

        pe = QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.darkCyan)  # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        MainWindow.setPalette(pe)

        self.choose.setStyleSheet('''QPushButton{border-radius:3px;font-size:12pt;}
                QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            border-radius:35px;
                            background:#6DDF6D;}''')
        self.start.setStyleSheet('''QPushButton{border-radius:3px;font-size:12pt;}
                QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            border-radius:35px;
                            background:#6DDF6D;}''')
        self.suspend.setStyleSheet('''QPushButton{border-radius:3px;font-size:12pt;}
                QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            border-radius:35px;
                            background:#6DDF6D;}''')

        MainWindow.setStyleSheet('''
            QPushButton{border:none;color:white;padding-left:5px;
                    height:35px;
                    font-size:15px;
                    padding-right:10px;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QWidget#left_widget{
                background:Gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QPushButton#left_button:hover{ color:white;
                    border:2px solid #F3F3F5;
                    border-radius:15px;
                    background:black;}''')

