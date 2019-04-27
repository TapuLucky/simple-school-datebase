# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
conn = pymysql.connect(host = 'localhost', user = "root", password = "", database = "school")
cursor = conn.cursor()

class Search_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 384)
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
        self.tabWidget_.setGeometry(QtCore.QRect(20, 80, 421, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.tabWidget_.setFont(font)
        self.tabWidget_.setObjectName("tabWidget_")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 15, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_id.setGeometry(QtCore.QRect(150, 10, 161, 31))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.pushButton_grades = QtWidgets.QPushButton(self.tab)
        self.pushButton_grades.setGeometry(QtCore.QRect(330, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_grades.setFont(font)
        self.pushButton_grades.setObjectName("pushButton_grades")
        self.textBrowser_Grades = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_Grades.setGeometry(QtCore.QRect(20, 50, 371, 191))
        self.textBrowser_Grades.setObjectName("textBrowser_Grades")
        self.tabWidget_.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_project = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_project.setGeometry(QtCore.QRect(330, 10, 56, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_project.setFont(font)
        self.pushButton_project.setObjectName("pushButton_project")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 15, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_id2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_id2.setGeometry(QtCore.QRect(180, 9, 131, 31))
        self.lineEdit_id2.setObjectName("lineEdit_id2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 50, 361, 191))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget_.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_class = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_class.setGeometry(QtCore.QRect(330, 10, 56, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.pushButton_class.setFont(font)
        self.pushButton_class.setObjectName("pushButton_class")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 15, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_ClassID = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_ClassID.setGeometry(QtCore.QRect(170, 10, 141, 31))
        self.lineEdit_ClassID.setObjectName("lineEdit_ClassID")
        self.textBrowser_class = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_class.setGeometry(QtCore.QRect(20, 50, 361, 191))
        self.textBrowser_class.setObjectName("textBrowser_class")
        self.tabWidget_.addTab(self.tab_3, "")
		
        self.pushButton_back.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        self.tabWidget_.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_class.clicked.connect(self.search_class)
        self.pushButton_project.clicked.connect(self.search_project)
        self.pushButton_grades.clicked.connect(self.search_grades)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "数据库查找"))
        self.pushButton_back.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "请选择需要查询的内容"))
        self.label_2.setText(_translate("Dialog", "请输入学号："))
        self.pushButton_grades.setText(_translate("Dialog", "查询"))
        self.tabWidget_.setTabText(self.tabWidget_.indexOf(self.tab), _translate("Dialog", "成绩查询"))
        self.pushButton_project.setText(_translate("Dialog", "查询"))
        self.label_3.setText(_translate("Dialog", "请输入学号："))
        self.tabWidget_.setTabText(self.tabWidget_.indexOf(self.tab_2), _translate("Dialog", "项目查询"))
        self.pushButton_class.setText(_translate("Dialog", "查询"))
        self.label_4.setText(_translate("Dialog", "请输入课程编号："))
        self.tabWidget_.setTabText(self.tabWidget_.indexOf(self.tab_3), _translate("Dialog", "教室查询"))
    
    def search_class(self, Dialog):
        temp = self.lineEdit_ClassID.text()
        string = "select class_id from course where course.course_id = '"+temp+"'"
        cursor.execute(string)
        data = cursor.fetchall()
        result = ''
        for key in data:
            for value in key:
                result = result + value
        result = '教室号：' + result
        self.textBrowser_class.setText(result)

    def search_project(self, Dialog):
        temp = self.lineEdit_id2.text()
        string = "select project_id from student_project where student_project.std_id = '"+temp+"'"
        cursor.execute(string)
        data = cursor.fetchall()
        result = ''
        for key in data:
            for value in key:
                result = result + value
        result = '项目号：' + result
        self.textBrowser_2.setText(result)
    
    def search_grades(self, Dialog):
        temp = self.lineEdit_id.text()
        string = "select course.course_id,course.course_name,course.course_grade from course,student_course "
        string += "where course.course_id = student_course.course_id and student_course.std_id = '"+temp+"'"
        cursor.execute(string)
        data = cursor.fetchall()
        result = ''
        for key in data:
            for value in key:
                result += '  ' + str(value)
        result = '课程号、课程名、分数分别为：' + result
        self.textBrowser_Grades.setText(result)
        

