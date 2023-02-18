# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:25:46 2017

@author: glassbox
"""

"""Module importation"""
import serial

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import serial
"""Opening of the serial port"""

arduino = serial.Serial("COM4", 9600)


"""Initialising variables"""
rawdata = []
count = 0

"""Receiving data and storing it in a list"""
'''k = True
while k:'''

rawdata.append(int(str(arduino.readline())[7:10]))

print(rawdata)

'''
def clean(L):  # L is a list
    newl = []  # initialising the new list
    for i in range(len(L)):
        temp = L[i][2:]
        newl.append(temp[:-5])
    return newl


cleandata = clean(rawdata)


def write(L):
    file = open("data.txt", mode='w')
    for i in range(len(L)):
        file.write(L[i] + '\n')
    file.close()


write(cleandata)'''