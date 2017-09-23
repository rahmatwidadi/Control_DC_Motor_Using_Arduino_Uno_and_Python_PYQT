import sys, os, glob
from PyQt5 import QtCore, QtWidgets, uic
import serial, time

qtCreatorFile = "gui_tugas_pyqt_arduino.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
                QtWidgets.QMainWindow.__init__(self)
                Ui_MainWindow.__init__(self)
                self.setupUi(self)
                self.button_serial.clicked.connect(self.OpenSerial)
                self.button_exit.clicked.connect(self.AppExit)
                self.button_forward.clicked.connect(self.forward)
                self.button_turn_right.clicked.connect(self.turn_right)
                self.button_reverse.clicked.connect(self.reverse)
                self.button_turn_left.clicked.connect(self.turn_left)
                self.button_stay.clicked.connect(self.stay)
                self.button_stay.setEnabled(False)
                self.button_forward.setEnabled(False)
                self.button_turn_right.setEnabled(False)
                self.button_reverse.setEnabled(False)
                self.button_turn_left.setEnabled(False)

        def OpenSerial(self):
                if self.button_serial.text()=='Serial':
                        self.ser = serial.Serial("COM4", "9600", timeout=0.1)
                        if self.ser.isOpen():
                         self.button_serial.setText('Close Serial')
                         self.textEdit_LogMessage.append("Opening serial port... OK")
                         self.button_stay.setEnabled(True)
                         self.button_forward.setEnabled(True)
                         self.button_turn_right.setEnabled(True)
                         self.button_reverse.setEnabled(True)
                         self.button_turn_left.setEnabled(True)
                        else:
                                self.textEdit_LogMessage.append("can not open serial port")
                else:
                        if self.ser.isOpen():
                                self.ser.close()
                                self.button_serial.setText('Serial')
                                self.textEdit_LogMessage.append("Closing serial port... OK")
                                self.button_stay.setEnabled(False)
                                self.button_forward.setEnabled(False)
                                self.button_turn_right.setEnabled(False)
                                self.button_reverse.setEnabled(False)
                                self.button_turn_left.setEnabled(False)
        def stay(self):
                self.TXdata = bytearray(1)
                self.TXdata=1
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Stop")
                #time.sleep(2)
        def forward(self):
                self.TXdata = bytearray(1)
                self.TXdata=2
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Constan Forward")
                #self.textEdit_LogMessage.append("Constan Forward = %d" %(self.TXdata))
                #time.sleep(2)
                #self.bytesToRead = self.ser.inWaiting()
                #if (self.bytesToRead > 0):
                        #rxdata = self.ser.read(self.bytesToRead)
                        #self.textEdit_LogMessage.append(rxdata)
                #self.textEdit_LogMessage.setText("Forward")
                
        def turn_right(self):
                self.TXdata = bytearray(1)
                self.TXdata=3
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Constan Turn Right" )
                time.sleep(2)
                #self.bytesToRead = self.ser.inWaiting()
                #if (self.bytesToRead > 0):
                        #rxdata = self.ser.read(self.bytesToRead)
                        #self.textEdit_LogMessage.append(rxdata)
        def reverse(self):
                
                self.TXdata = bytearray(1)
                self.TXdata=4
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Constan Reverse" )
                #time.sleep(2)
##              self.bytesToRead = self.ser.inWaiting()
##              if (self.bytesToRead > 0):
##                      rxdata = self.ser.read(self.bytesToRead)
##                      self.textEdit_LogMessage.append(rxdata)
        def turn_left(self):
                
                self.TXdata = bytearray(1)
                self.TXdata=5
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Constan Turn Left" )
                #time.sleep(2)
##              self.bytesToRead = self.ser.inWaiting()
##              if (self.bytesToRead > 0):
##                      rxdata = self.ser.read(self.bytesToRead)
##                      self.textEdit_LogMessage.append(rxdata)
        def AppExit(self):
                self.textEdit_LogMessage.setText("Exit application")
                sys.exit()
        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())
