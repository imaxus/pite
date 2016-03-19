# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from FileSaver import FileSaver
from Buffer import Buffer
from CSVReader import CsvReader
from InputValidator import InputValidator
from DataOperation import DataOperation
from PlotCreator import PlotCreator
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
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


class MainWindow(QtGui.QWidget):
    """
    Klasa odpowiedzialna za wyswietlanie gui
    """
    def __init__(self):
        self.data = 0
        self.visualizer = 0
        self.data_loaded = False
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        funkcja inicjalizujaca wszystkie widgety okna
        :return: void
        """

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #przyciska do ladowania danych
        self.dane = QtGui.QPushButton(self.centralwidget)
        self.dane.setGeometry(QtCore.QRect(50, 20, 141, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Download-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dane.setIcon(icon)
        self.dane.setIconSize(QtCore.QSize(32, 32))
        self.dane.setObjectName(_fromUtf8("dane"))
        self.dane.setText(_fromUtf8("Załaduje dane"))
        self.dane.clicked.connect(self.open_file)

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 190, 971, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        #przycisk do tworzenia wykresu predkosci
        self.speed = QtGui.QPushButton(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(170, 120, 81, 41))
        self.speed.setObjectName(_fromUtf8("speed"))
        self.speed.setText(_fromUtf8("Prędkość"))
        self.speed.clicked.connect(self.plot_speed)
        #przycisk do tworzenia wykresu przebytego dystansu
        self.dst_accu = QtGui.QPushButton(self.centralwidget)
        self.dst_accu.setGeometry(QtCore.QRect(400, 120, 151, 41))
        self.dst_accu.setObjectName(_fromUtf8("dst_accu"))
        self.dst_accu.setText(_fromUtf8("Dystans w jednostce czasu"))
        #przycisk do tworzenia wykresu dystansu w jednostce czasu
        self.dst = QtGui.QPushButton(self.centralwidget)
        self.dst.setGeometry(QtCore.QRect(280, 120, 91, 41))
        self.dst.setObjectName(_fromUtf8("dst"))
        self.dst.setText(_fromUtf8("Dystans"))
        #przycisk do tworzenia wykresu wysokosci
        self.altitude = QtGui.QPushButton(self.centralwidget)
        self.altitude.setGeometry(QtCore.QRect(580, 120, 81, 41))
        self.altitude.setObjectName(_fromUtf8("altitude"))
        self.altitude.setText(_fromUtf8("Wysokość"))
        #przycisk do tworzenia wykresu toru lotu
        self.path = QtGui.QPushButton(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(690, 120, 81, 41))
        self.path.setObjectName(_fromUtf8("path"))
        self.path.setText(_fromUtf8("Tor lotu"))
        #przycisk do tworzenia wykresow przechylow samolotus
        self.roll_pitch = QtGui.QPushButton(self.centralwidget)
        self.roll_pitch.setGeometry(QtCore.QRect(800, 120, 131, 41))
        self.roll_pitch.setObjectName(_fromUtf8("roll_pitch"))
        self.roll_pitch.setText(_fromUtf8("Wychyły samolotu"))
        #przycisk do tworzenia wykresu przyspieszenia
        self.acceleration = QtGui.QPushButton(self.centralwidget)
        self.acceleration.setGeometry(QtCore.QRect(50, 120, 91, 41))
        self.acceleration.setObjectName(_fromUtf8("acceleration"))
        self.acceleration.setText(_fromUtf8("Przyspieszenie"))
        self.acceleration.clicked.connect(self.plot_acceleration)
        #ustawienia okna
        self.setObjectName(_fromUtf8("FlightRecorder"))
        self.setWindowTitle("Flight Recorder")
        self.resize(986, 684)
        self.setAcceptDrops(True)
        self.show()

    def open_file(self):
        """
        Funkcja otwierajaca file dialog
        :return: nazwa wybranego pliku
        """
        file_name = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.prepare_loaded_data(file_name)

    @staticmethod
    def show_it():
        """
        Metoda inicjalizujaca gui
        :return:
        """
        app = QtGui.QApplication(sys.argv)
        ex = MainWindow()
        sys.exit(app.exec_())

    def prepare_loaded_data(self, file_name):
        """
        Przygotowuje i wczytuje dane z pliku
        :param file_name: plik z danymi
        :return:
        """
        #utworzenie bufora
        buff = Buffer()
        data = CsvReader.read_from_file(file_name, 1)
        #zmiana czasu
        data = DataOperation.change_time_relative(data)
        #zmiana wysokosci na metry
        data = DataOperation.change_altitude_cm_m(data)
        #stworzenie zapisywacza
        saver = FileSaver("saved_data/dane.txt")

        #kazda linijke z pliku csv buforujemy osobno
        for d in data:
            buff.set_data(d)
            buffered_data = buff.get_data()
            #sprawdzamy czy kazda linijka jest poprawnie zapisana
            if InputValidator.input_val(buffered_data):
                #zapisujemy kazda linijke do nowego pliku
                saver.save_data(buffered_data)

        #odczyt danych z pliku csv i wizualizacja
        r_data = CsvReader.read_from_file(saver.get_file_name())

        #tworzymy wizualizator, drugi parametr do interwal czasowy
        self.visualizer = PlotCreator(r_data, 1)
        self.data_loaded = True
        print "Dane zaladowane"

    def plot_acceleration(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.acceleration_time(False)
            self.tab_acc = QtGui.QWidget()
            self.tab_acc.setObjectName(_fromUtf8("acc"))
            self.tabWidget.addTab(self.tab_acc, _fromUtf8("Przyspieszenie"))
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_acc.setLayout(layout)

    def plot_speed(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.speed_time(False)
            self.tab_speed = QtGui.QWidget()
            self.tab_speed.setObjectName(_fromUtf8("speed"))
            self.tabWidget.addTab(self.tab_speed, _fromUtf8("Prędkość"))
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_speed.setLayout(layout)

if __name__ == "__main__":
    MainWindow.show_it()


