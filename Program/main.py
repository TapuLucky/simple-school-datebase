import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MyMainWindow
from Search import Search_Dialog
from Add import Add_Dialog
from Delete import Delete_Dialog
from Change import Change_Dialog

import pymysql
conn = pymysql.connect(host = 'localhost', user = "root", password = "", database = "school")
cursor = conn.cursor()

class MyMainWindow(QDialog, MyMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

class Search_Dialog(QDialog, Search_Dialog):
    def __init__(self, parent = None):
        super(Search_Dialog, self).__init__(parent)
        self.setupUi(self)

class Add_Dialog(QDialog, Add_Dialog):
    def __init__(self, parent = None):
        super(Add_Dialog, self).__init__(parent)
        self.setupUi(self)

class Delete_Dialog(QDialog, Delete_Dialog):
    def __init__(self, parent = None):
        super(Delete_Dialog, self).__init__(parent)
        self.setupUi(self)

class Change_Dialog(QDialog, Change_Dialog):
    def __init__(self, parent = None):
        super(Change_Dialog, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyMainWindow = MyMainWindow()
    Search_Dialog = Search_Dialog()
    Add_Dialog = Add_Dialog()
    Delete_Dialog = Delete_Dialog()
    Change_Dialog = Change_Dialog()
    MyMainWindow.show()

    MyMainWindow.pushButton_search.clicked.connect(Search_Dialog.show)
    MyMainWindow.pushButton_add.clicked.connect(Add_Dialog.show)
    MyMainWindow.pushButton_delete.clicked.connect(Delete_Dialog.show)
    MyMainWindow.pushButton_change.clicked.connect(Change_Dialog.show)

    sys.exit(app.exec_())