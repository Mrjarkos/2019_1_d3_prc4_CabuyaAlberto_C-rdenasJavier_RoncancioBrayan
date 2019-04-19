# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog, QWidget, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer,QRegExp
from PyQt5.QtGui import QPixmap,QImage,QRegExpValidator
import threading


class BankOfficer(QMainWindow):
    def __init__(self):
    	super(BankOfficer,self).__init__(None)
    	loadUi('bankofficial.ui',self)
    	pass
app= QApplication(sys.argv)
ui=BankOfficer()
ui.setWindowTitle('Test')
ui.show()
ret= app.exec_()
sys.exit(ret)