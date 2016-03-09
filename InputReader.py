#!/usr/bin/env python
import numpy as np


class InputReader:
    def __init__(self):
        self.data = np.zeros((2, 3))
        self.counter = 0

    def read_input(self, file_name, size):
        """
        :param file_name: string, nazwa pliku
        :param size: int, ilosc lini w pliku
        :return: numpy array, o wielkosci size x 3
        Metoda wczytujaca  rownania do tablic, trzeba podac argument w konsoli,
        file_name - nazwa pliku z danymi, size-ilosc wierszy """
        self.data = np.zeros((size, 3))
        self.counter = 0
        with open(file_name, 'r') as f:
            for line in f:
                self.data[self.counter] = line.split(",")
                self.counter += 1
            if size == 2:
                print "uklad jest dobrze okreslony"
            elif size > 2:
                print "uklad jest nadokreslony"
            else:
                print "uklad jest niedookreslony"
        return self.data

    def __repr__(self):
        print self.data
