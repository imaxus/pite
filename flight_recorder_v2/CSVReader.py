import csv
import numpy as np


class CsvReader:
    @staticmethod
    def read_from_file(file_name, head=0):
        """
        metoda wczytujaca dane z pliku csv do tabeli numpy
        :param file_name: nazwa pliku, z ktorego beda wczytane dane
        :param head: okresla ile lini od poczatku ma zostac pominietych, domyslnie 0, przydatne gdy jest naglowek
        :return: dane bez pierwszego wiersza, ktory jest naglowkiem
        """
        try:
            with open(file_name, 'rb') as csvfile:
                data = np.genfromtxt(csvfile, delimiter=',')
        except:
            print "nie udalo sie wczytac pliku, prosze sprobowac ponownie"
        if data[0].size == 7:
            #zwraca od drugiego wiersza bo pierwszy jest naglowkowy
            return data[head:]
        else:
            print "plik niewlasciwie sformatowany"
            quit()
