# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Izanagi\Documents\GitHub\pite\flight_recorder_v2\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_FlightRecorder(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        FlightRecorder = QtGui.QMainWindow()
        FlightRecorder.setObjectName(_fromUtf8("FlightRecorder"))
        FlightRecorder.resize(986, 684)
        FlightRecorder.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(FlightRecorder)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dane = QtGui.QPushButton(self.centralwidget)
        self.dane.setGeometry(QtCore.QRect(50, 20, 141, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Download-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dane.setIcon(icon)
        self.dane.setIconSize(QtCore.QSize(32, 32))
        self.dane.setObjectName(_fromUtf8("dane"))
        self.acceleration = QtGui.QPushButton(self.centralwidget)
        self.acceleration.setGeometry(QtCore.QRect(50, 120, 91, 41))
        self.acceleration.setObjectName(_fromUtf8("acceleration"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 190, 971, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.speed = QtGui.QPushButton(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(170, 120, 81, 41))
        self.speed.setObjectName(_fromUtf8("speed"))
        self.dst_accu = QtGui.QPushButton(self.centralwidget)
        self.dst_accu.setGeometry(QtCore.QRect(280, 120, 91, 41))
        self.dst_accu.setObjectName(_fromUtf8("dst_accu"))
        self.dst = QtGui.QPushButton(self.centralwidget)
        self.dst.setGeometry(QtCore.QRect(400, 120, 151, 41))
        self.dst.setObjectName(_fromUtf8("dst"))
        self.altitude = QtGui.QPushButton(self.centralwidget)
        self.altitude.setGeometry(QtCore.QRect(580, 120, 81, 41))
        self.altitude.setObjectName(_fromUtf8("altitude"))
        self.path = QtGui.QPushButton(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(690, 120, 81, 41))
        self.path.setObjectName(_fromUtf8("path"))
        self.roll_pitch = QtGui.QPushButton(self.centralwidget)
        self.roll_pitch.setGeometry(QtCore.QRect(800, 120, 131, 41))
        self.roll_pitch.setObjectName(_fromUtf8("roll_pitch"))
        FlightRecorder.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FlightRecorder)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FlightRecorder.setStatusBar(self.statusbar)

        self.retranslateUi(FlightRecorder)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, FlightRecorder):
        FlightRecorder.setWindowTitle(_translate("FlightRecorder", "Flight Recorder", None))
        self.dane.setText(_translate("FlightRecorder", "Za+éaduj Dane", None))
        self.acceleration.setText(_translate("FlightRecorder", "Przyspieszenie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("FlightRecorder", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("FlightRecorder", "Tab 2", None))
        self.speed.setText(_translate("FlightRecorder", "Pr¦Ödko+Ť¦ç", None))
        self.dst_accu.setText(_translate("FlightRecorder", "Przebyta droga", None))
        self.dst.setText(_translate("FlightRecorder", "Droga na jednostk¦Ö czasu", None))
        self.altitude.setText(_translate("FlightRecorder", "Wysoko+Ť¦ç", None))
        self.path.setText(_translate("FlightRecorder", "Tor lotu", None))
        self.roll_pitch.setText(_translate("FlightRecorder", "Wychylenia samolotu", None))
