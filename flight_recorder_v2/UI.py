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
        #label mowiacy jakie dane mamy zaladowane
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(250, 20, 350, 51))
        self.label1.setText(_fromUtf8("Załadowane dane: "))
        self.label1.setObjectName(_fromUtf8("Label staly"))
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(350, 20, 450, 51))
        self.label2.setText("<font color='red'>Brak</font>")
        self.label2.setObjectName(_fromUtf8("Label zmienny"))
        #tworzymy przegladarke wykresow
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        #ustawiamy wymiary orzegladarki
        self.tabWidget.setGeometry(QtCore.QRect(10, 190, 971, 471))
        #nazywamy przegladarke
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        #ustawiamy mozliwosc zamkniecia zakladek
        self.tabWidget.setTabsClosable(True)
        #pozwalamy na przzesuwanie zakladek
        self.tabWidget.tabBar().setMovable(True)
        #laczymy sygnal zamkniecia z funkcja zamykajaca
        self.tabWidget.tabCloseRequested.connect(self.close_handler)
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
        self.dst_accu.clicked.connect(self.plot_dst_accu)
        #przycisk do tworzenia wykresu dystansu w jednostce czasu
        self.dst = QtGui.QPushButton(self.centralwidget)
        self.dst.setGeometry(QtCore.QRect(280, 120, 91, 41))
        self.dst.setObjectName(_fromUtf8("dst"))
        self.dst.setText(_fromUtf8("Dystans"))
        self.dst.clicked.connect(self.plot_dst)
        #przycisk do tworzenia wykresu wysokosci
        self.altitude = QtGui.QPushButton(self.centralwidget)
        self.altitude.setGeometry(QtCore.QRect(580, 120, 81, 41))
        self.altitude.setObjectName(_fromUtf8("altitude"))
        self.altitude.setText(_fromUtf8("Wysokość"))
        self.altitude.clicked.connect(self.plot_altitude)
        #przycisk do tworzenia wykresu toru lotu
        self.path = QtGui.QPushButton(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(690, 120, 81, 41))
        self.path.setObjectName(_fromUtf8("path"))
        self.path.setText(_fromUtf8("Tor lotu"))
        self.path.clicked.connect(self.plot_path)
        #przycisk do tworzenia wykresow przechylow samolotus
        self.roll_pitch = QtGui.QPushButton(self.centralwidget)
        self.roll_pitch.setGeometry(QtCore.QRect(800, 120, 131, 41))
        self.roll_pitch.setObjectName(_fromUtf8("roll_pitch"))
        self.roll_pitch.setText(_fromUtf8("Wychyły samolotu"))
        self.roll_pitch.clicked.connect(self.plot_roll_pitch)
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
        temp_file = file_name
        self.prepare_loaded_data(file_name)
        self.label2.setText("<font color='green'>%s</font>" % temp_file)

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

    def close_handler(self, index):
        """
        Funkcja zamykajaca strony QtabWidget
        :param index: index strony do zamkniecia
        :return:
        """
        print "close_handler called, index = %s" % index
        self.tabWidget.removeTab(index)

    def plot_acceleration(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            #funkcja klasy visualizer zwraca nam pyplot.figure ( czyli przyklad)
            fig = self.visualizer.acceleration_time(False)
            #tworzymy zaklwadke w przegladarce wykresow ktora jest instancja QTabWidget
            self.tab_acc = QtGui.QWidget()
            #nadajemy zakladce nazwe
            self.tab_acc.setObjectName(_fromUtf8("acc"))
            #dodajemy zakladke do przegladarki nazywajac ja Przyspieszenie
            self.tabWidget.addTab(self.tab_acc, _fromUtf8("Przyspieszenie"))
            #ustawiamy focus na nowa zakladke
            self.tabWidget.setCurrentWidget(self.tab_acc)
            #tworzymy layout strony
            layout = QtGui.QVBoxLayout()
            #przypisujemy wykres z przykladu jako layout
            layout.addWidget(FigureCanvasQTAgg(fig))
            #dodajemy layout do zakladki
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
            self.tabWidget.setCurrentWidget(self.tab_speed)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_speed.setLayout(layout)

    def plot_dst(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.dst_time(False)
            self.tab_dst = QtGui.QWidget()
            self.tab_dst.setObjectName(_fromUtf8("dst"))
            self.tabWidget.addTab(self.tab_dst, _fromUtf8("Dystans"))
            self.tabWidget.setCurrentWidget(self.tab_dst)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_dst.setLayout(layout)

    def plot_dst_accu(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.dst_accu_time(False)
            self.tab_dst_accu = QtGui.QWidget()
            self.tab_dst_accu.setObjectName(_fromUtf8("dst"))
            self.tabWidget.addTab(self.tab_dst_accu, _fromUtf8("Dystans na jednostkę"))
            self.tabWidget.setCurrentWidget(self.tab_dst_accu)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_dst_accu.setLayout(layout)

    def plot_altitude(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.altitude_time(False)
            self.tab_alt = QtGui.QWidget()
            self.tab_alt.setObjectName(_fromUtf8("dst"))
            self.tabWidget.addTab(self.tab_alt, _fromUtf8("Wysokość"))
            self.tabWidget.setCurrentWidget(self.tab_alt)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_alt.setLayout(layout)

    def plot_path(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.position_time(True)
            self.tab_path = QtGui.QWidget()
            self.tab_path.setObjectName(_fromUtf8("dst"))
            self.tabWidget.addTab(self.tab_path, _fromUtf8("Tor lotu"))
            self.tabWidget.setCurrentWidget(self.tab_path)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_path.setLayout(layout)

    def plot_roll_pitch(self):
        """
        Wrzuca plot do zakladki w gui
        :return:
        """
        if self.data_loaded:
            fig = self.visualizer.roll_time(False)
            fig2 = self.visualizer.pitch_time(False)
            self.tab_roll = QtGui.QWidget()
            self.tab_roll.setObjectName(_fromUtf8("dst"))
            self.tabWidget.addTab(self.tab_roll, _fromUtf8("Przechył boczny"))
            self.tabWidget.setCurrentWidget(self.tab_roll)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig))
            self.tab_roll.setLayout(layout)

            self.tab_pitch = QtGui.QWidget()
            self.tab_pitch.setObjectName(_fromUtf8("dst"))
            self.tabWidget.addTab(self.tab_pitch, _fromUtf8("Kąt wznoszenia"))
            self.tabWidget.setCurrentWidget(self.tab_pitch)
            layout = QtGui.QVBoxLayout()
            layout.addWidget(FigureCanvasQTAgg(fig2))
            self.tab_pitch.setLayout(layout)

if __name__ == "__main__":
    MainWindow.show_it()


