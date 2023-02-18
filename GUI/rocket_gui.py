#TODO: GET PY QT DESIGNER TO MAKE IT EASY TO MAKE THE GUI

from PyQt6.QtCore import QThread, pyqtSignal, QMetaObject
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
from PyQt6 import uic, QtCore
from serial import Serial, unicode

from serial_thread import SerialThread


class UI(QWidget):

    writeToSerial = pyqtSignal(bytes)

    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("gui.ui", self)

        # Initiate serial port
        self.serial_port = Serial(None, 9600, dsrdtr=True)
        self.serial_port.port = "COM4"

        # Initiate Serial Thread
        self.serialThread = SerialThread(self.serial_port, write_signal=self.writeToSerial)
        self._thread = QThread()
        self.serialThread.moveToThread(self._thread)

        # Find the output box
        self.outputBox = self.findChild(QTextEdit, "outputBox")


        #Connect our function to the serial thread signal
        self.serialThread.dataReceived.connect(self.on_dataReceived)





        #start serial thread
        self._thread.started.connect(self.serialThread.run)
        self._thread.start()

    @QtCore.pyqtSlot(bytes)
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