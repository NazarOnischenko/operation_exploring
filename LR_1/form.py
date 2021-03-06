# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(485, 236)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CheckFormula1 = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckFormula1.setGeometry(QtCore.QRect(20, 50, 121, 41))
        self.CheckFormula1.setObjectName("checkFormula1")
        self.CheckFormula2 = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckFormula2.setGeometry(QtCore.QRect(20, 100, 161, 41))
        self.CheckFormula2.setObjectName("checkFormula2")
        self.CheckFormula3 = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckFormula3.setGeometry(QtCore.QRect(20, 150, 181, 41))
        self.CheckFormula3.setObjectName("checkFormula3")
        self.ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ComboBox.setGeometry(QtCore.QRect(210, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ComboBox.setFont(font)
        self.ComboBox.setAccessibleDescription("")
        self.ComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ComboBox.setAutoFillBackground(False)
        self.ComboBox.setEditable(False)
        self.ComboBox.setMaxVisibleItems(10)
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SpinAmount = QtWidgets.QSpinBox(self.centralwidget)
        self.SpinAmount.setGeometry(QtCore.QRect(410, 160, 51, 22))
        self.SpinAmount.setMaximum(100000000)
        self.SpinAmount.setProperty("value", 400)
        self.SpinAmount.setObjectName("SpinAmount")
        self.SpinStart = QtWidgets.QSpinBox(self.centralwidget)
        self.SpinStart.setGeometry(QtCore.QRect(240, 160, 42, 22))
        self.SpinStart.setMinimum(-1000000000)
        self.SpinStart.setSingleStep(1)
        self.SpinStart.setProperty("value", -15)
        self.SpinStart.setObjectName("SpinStart")
        self.SpinEnd = QtWidgets.QSpinBox(self.centralwidget)
        self.SpinEnd.setGeometry(QtCore.QRect(330, 160, 42, 22))
        self.SpinEnd.setMinimum(-1000000000)
        self.SpinEnd.setSingleStep(1)
        self.SpinEnd.setProperty("value", 15)
        self.SpinEnd.setObjectName("SpinEnd")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 130, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 130, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 130, 47, 13))
        self.label_4.setObjectName("label_4")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(320, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Close.setFont(font)
        self.Close.setObjectName("Close")
        self.Apply = QtWidgets.QPushButton(self.centralwidget)
        self.Apply.setGeometry(QtCore.QRect(210, 70, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Apply.setFont(font)
        self.Apply.setObjectName("Apply")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TM-81,Onischenko Nazar Ruslanovych ,LR ??? 1"))
        self.CheckFormula1.setText(_translate("MainWindow", "y =  (x - N / 2) ** 2"))
        self.CheckFormula2.setText(_translate("MainWindow", "y =  (x - N / 2) ** 2 + N * x"))
        self.CheckFormula3.setText(_translate("MainWindow", "y =  (x - N / 2) ** 2 + N * x ** 2"))
        self.ComboBox.setItemText(0, _translate("MainWindow", "Search Method"))
        self.ComboBox.setItemText(1, _translate("MainWindow", "Specification Method"))
        self.label.setText(_translate("MainWindow", "Functions"))
        self.label_2.setText(_translate("MainWindow", "StartInterval"))
        self.label_3.setText(_translate("MainWindow", "EndtInterval"))
        self.label_4.setText(_translate("MainWindow", "Iterations"))
        self.Close.setText(_translate("MainWindow", "Close graphic"))
        self.Apply.setText(_translate("MainWindow", "Apply"))
