from FileSaver import FileSaver
from Buffer import Buffer
from CSVReader import CsvReader
from InputValidator import InputValidator
from DataOperation import DataOperation

#przeplyw danych csvReader -> podzial na wiersze -> buffer -> InputValidation - >fileSaver
buff = Buffer()
file_name = raw_input("Podaj nazwe pliku z danymi w formacie csv \n")
data = CsvReader.read_from_file(file_name)
data = DataOperation.change_time_relative(data)
for d in data:
    buff.set_data(d)
    buffered_data = buff.get_data()
    if InputValidator.input_val(buffered_data):
        FileSaver.save_data(buffered_data, "dane.txt")

