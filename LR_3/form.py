# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 236)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonApply = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonApply.setObjectName("ButtonApply")
        self.gridLayout.addWidget(self.ButtonApply, 0, 0, 1, 1)
        self.Button3DG = QtWidgets.QPushButton(self.centralwidget)
        self.Button3DG.setObjectName("Button3DG")
        self.gridLayout.addWidget(self.Button3DG, 0, 1, 1, 1)
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setObjectName("ButtonExit")
        self.gridLayout.addWidget(self.ButtonExit, 0, 2, 1, 1)
        self.ButtonProj = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonProj.setObjectName("ButtonProj")
        self.gridLayout.addWidget(self.ButtonProj, 0, 3, 1, 1)
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(1)
        self.Table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.Table, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????????? ???????????? ???3"))
        self.ButtonApply.setText(_translate("MainWindow", "APPLY"))
        self.Button3DG.setText(_translate("MainWindow", "3D Graphic"))
        self.ButtonExit.setText(_translate("MainWindow", "EXIT"))
        self.ButtonProj.setText(_translate("MainWindow", "Projection"))
        item = self.Table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "x1"))
        item = self.Table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "x2"))
        item = self.Table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "F(x1,x2)"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
