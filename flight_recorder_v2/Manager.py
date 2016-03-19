from FileSaver import FileSaver
from Buffer import Buffer
from CSVReader import CsvReader
from InputValidator import InputValidator
from DataOperation import DataOperation
from PlotCreator import PlotCreator
from UI import MainWindow

import sys

#przeplyw danych csvReader -> podzial na wiersze -> buffer -> InputValidation - >fileSaver
#utworzenie bufora
buff = Buffer()

file_name = raw_input("Podaj nazwe pliku z danymi w formacie csv \n")
#wczytanie danych z pliku csv
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
visualizer = PlotCreator(r_data, 1)
fig = visualizer.acceleration_time(True)
#visualizer.speed_time()
#visualizer.dst_time()
#visualizer.dst_accu__time()
#visualizer.altitude_time()
#visualizer.position_time()
#visualizer.pitch_time()
#visualizer.roll_time()
