import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Search import Search_Dialog

class Search_Dialog(QDialog, Search_Dialog):
    def __init__(self, parent = None):
        super(Search_Dialog, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyMainWindow = Search_Dialog()
    MyMainWindow.show()

    sys.exit(app.exec_())