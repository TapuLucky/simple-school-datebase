# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Delete.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
conn = pymysql.connect(host = 'localhost', user = "root", password = "", database = "school")
cursor = conn.cursor()

class Delete_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 410)
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(340, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget_ = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_.setGeometry(QtCore.QRect(20, 80, 431, 311))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.tabWidget_.setFont(font)
        self.tabWidget_.setObjectName("tabWidget_")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 25, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_lab_std_id = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_lab_std_id.setGeometry(QtCore.QRect(150, 20, 161, 31))
        self.lineEdit_lab_std_id.setObjectName("lineEdit_lab_std_id")
        self.pushButton_delete1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_delete1.setGeometry(QtCore.QRect(340, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete1.setFont(font)
        self.pushButton_delete1.setObjectName("pushButton_delete1")
        self.lineEdit_lab_id = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_lab_id.setGeometry(QtCore.QRect(150, 70, 161, 31))
        self.lineEdit_lab_id.setObjectName("lineEdit_lab_id")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_lab = QtWidgets.QLabel(self.tab)
        self.label_lab.setGeometry(QtCore.QRect(160, 180, 72, 15))
        self.label_lab.setText("")
        self.label_lab.setObjectName("label_lab")
        self.tabWidget_.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_project_id = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_project_id.setGeometry(QtCore.QRect(150, 75, 161, 31))
        self.lineEdit_project_id.setObjectName("lineEdit_project_id")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 75, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_project_std_id = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_project_std_id.setGeometry(QtCore.QRect(150, 25, 161, 31))
        self.lineEdit_project_std_id.setObjectName("lineEdit_project_std_id")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_delete2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_delete2.setGeometry(QtCore.QRect(340, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete2.setFont(font)
        self.pushButton_delete2.setObjectName("pushButton_delete2")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(180, 220, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_project = QtWidgets.QLabel(self.tab_3)
        self.label_project.setGeometry(QtCore.QRect(160, 180, 72, 15))
        self.label_project.setText("")
        self.label_project.setObjectName("label_project")
        self.tabWidget_.addTab(self.tab_3, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 25, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_card_std_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_card_std_id.setGeometry(QtCore.QRect(150, 20, 161, 31))
        self.lineEdit_card_std_id.setObjectName("lineEdit_card_std_id")
        self.pushButton_delete3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_delete3.setGeometry(QtCore.QRect(340, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete3.setFont(font)
        self.pushButton_delete3.setObjectName("pushButton_delete3")
        self.lineEdit_card_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_card_id.setGeometry(QtCore.QRect(150, 65, 161, 31))
        self.lineEdit_card_id.setObjectName("lineEdit_card_id")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(20, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 240, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(20, 115, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setGeometry(QtCore.QRect(150, 110, 161, 31))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_card = QtWidgets.QLabel(self.widget)
        self.label_card.setGeometry(QtCore.QRect(160, 200, 72, 15))
        self.label_card.setText("")
        self.label_card.setObjectName("label_card")
        self.tabWidget_.addTab(self.widget, "")

        self.pushButton_back.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        self.tabWidget_.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_delete1.clicked.connect(self.delete_lab)
        self.pushButton_delete2.clicked.connect(self.delete_project)
        self.pushButton_delete3.clicked.connect(self.delete_card)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "数据删除"))
        self.pushButton_back.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "请选择需要删除的内容"))
        self.label_2.setText(_translate("Dialog", "请输入学号："))
        self.pushButton_delete1.setText(_translate("Dialog", "删除"))
        self.label_4.setText(_translate("Dialog", "请输入实验室号："))
        self.tabWidget_.setTabText(self.tabWidget_.indexOf(self.tab), _translate("Dialog", "退出实验室"))
        self.label_12.setText(_translate("Dialog", "请输入项目号："))
        self.label_13.setText(_translate("Dialog", "请输入学号："))
        self.pushButton_delete2.setText(_translate("Dialog", "删除"))
        self.tabWidget_.setTabText(self.tabWidget_.indexOf(self.tab_3), _translate("Dialog", "退出项目组"))
        self.label_10.setText(_translate("Dialog", "请输入学号："))
        self.pushButton_delete3.setText(_translate("Dialog", "删除"))
        self.label_14.setText(_translate("Dialog", "请输入卡号："))
        self.label_16.setText(_translate("Dialog", "请输入密码："))
        self.tabWidget_.setTabText(self.tabWidget_.indexOf(self.widget), _translate("Dialog", "校园卡挂失"))

    def delete_lab(self, Dialog):
        temp1 = self.lineEdit_lab_std_id.text()
        temp2 = self.lineEdit_lab_id.text()
        cursor.execute('set FOREIGN_KEY_CHECKS = 0')
        string = "update student set student.lab_id = '' where student.std_id = '"+temp1+"' and student.lab_id = '"+temp2+"'"
        cursor.execute(string)
        cursor.execute('set FOREIGN_KEY_CHECKS = 1')
        conn.commit()
        self.label_lab.setText('退出实验室成功')

    def delete_project(self, Dialog):
        temp1 = self.lineEdit_project_std_id.text()
        temp2 = self.lineEdit_project_id.text()
        string = "delete from student_project where student_project.std_id = '"+temp1
        string += "' and student_project.project_id = '"+temp2+"'"
        cursor.execute(string)
        conn.commit()
        self.label_project.setText('退出项目组成功')

    def delete_card(self, Dialog):
        temp1 = self.lineEdit_card_std_id.text()
        temp2 = self.lineEdit_card_id.text()
        cursor.execute('set FOREIGN_KEY_CHECKS = 0')
        string1 = "delete from card where card.card_id = '"+temp2+"'"
        string2 = "update student set student.card_id = '' where student.std_id = '"+temp1+"' and student.card_id = '"+temp2+"'"
        cursor.execute(string1)
        cursor.execute(string2)
        cursor.execute('set FOREIGN_KEY_CHECKS = 1')
        conn.commit()
        self.label_card.setText('校园卡挂失成功')

