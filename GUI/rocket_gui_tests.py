from PyQt6.QtCore import QThread, pyqtSignal, QMetaObject
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGraphicsWidget
from PySide6.QtWidgets import QApplication
from PyQt6 import uic, QtCore
from serial import Serial, unicode

from serial_thread import SerialThread


class UI(QWidget):

    writeToSerial = pyqtSignal(bytes)

    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("testgui.ui", self)

    data = ([1,2,3],[4,5,6])
    def on_dataReceived(self, data):
        try:
            message = unicode(data, errors='ignore')
            self.outputBox.insertPlainText(message)
        except Exception as e:
            print(str(e))

app = QApplication([])
window = UI()
window.show()
app.exec()