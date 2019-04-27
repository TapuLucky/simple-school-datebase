# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MyMainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(232, 164)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 2, 0, 1, 1)
        self.pushButton_change = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton_change.setFont(font)
        self.pushButton_change.setObjectName("pushButton_change")
        self.gridLayout.addWidget(self.pushButton_change, 3, 0, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "校园数据库系统"))
        self.pushButton_search.setText(_translate("Dialog", "数据查询"))
        self.label_1.setText(_translate("Dialog", "校园数据库系统主界面"))
        self.pushButton_add.setText(_translate("Dialog", "数据添加"))
        self.pushButton_change.setText(_translate("Dialog", "数据修改"))
        self.pushButton_delete.setText(_translate("Dialog", "数据删除"))
        self.label_2.setText(_translate("Dialog", "请选择需要运行的功能"))

