import csv
import numpy as np
class CsvReader:
    @staticmethod
    def read_from_file(file_name):
        """
        metoda wczytujaca dane z pliku csv do tabeli numpy
        :param file_name: nazwa pliku, z ktorego beda wczytane dane
        :return: dane bez pierwszego wiersza, ktory jest naglowkiem
        """
        try:
            with open(file_name, 'rb') as csvfile:
                data = np.genfromtxt(csvfile, delimiter=',')
        except:
            print "nie udalo sie wczytac pliku, prosze sprobowac ponownie"
        if data[0].size == 7:
            #zwraca od drugiego wiersza bo pierwszy jest naglowkowy
            return data[1:]
        else:
            print "plik niewlasciwie sformatowany"
            quit()
