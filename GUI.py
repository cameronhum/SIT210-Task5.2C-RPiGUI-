from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def clicked(pin):
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)

    GPIO.output(pin,GPIO.HIGH)

def exitfunc():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    win.close

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("RGB GUI")
    
    label = QtWidgets.QLabel(win)
    label.setText("RGB GUI")
    label.move(125,25)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("exit")
    b1.clicked.connect(exitfunc)
    b1.move(100,200)

    r1 = QtWidgets.QRadioButton(win)
    r1.setText("red light")
    r1.clicked.connect(lambda: clicked(19))
    r1.move(100,75)
    
    r2 = QtWidgets.QRadioButton(win)
    r2.setText("green light")
    r2.clicked.connect(lambda: clicked(21))
    r2.move(100,100)
    
    r3 = QtWidgets.QRadioButton(win)
    r3.setText("blue light")
    r3.clicked.connect(lambda: clicked(23))
    r3.move(100,125)
    
    win.show()
    sys.exit(app.exec_())

window()

