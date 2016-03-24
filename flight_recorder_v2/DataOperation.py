from __future__ import division
import numpy as np
import math



class DataOperation:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def change_time_relative(data_array):
        """
        Metoda zamieniajaca czas z zegarow samolotu na czas od poczatku lotu
        :param data_array: tablica z wszystkimi danymi z lotu
        :return: tablica z wszystkimi danymi z lotu
        """
        start_time = data_array[0, 0]
        data_array[:, 0] = data_array[:, 0] - start_time
        return data_array

    @staticmethod
    def change_altitude_cm_m(data_array):
        """
        Metoda zamieniajaca wysokosc w cm na wysokosc w metrach
        :param data_array: tablica z wszystkimi danymi z lotu
        :return: tablica z wszystkimi danymi z lotu
        """
        data_array[:, 3] = data_array[:, 3]*0.3048
        return data_array

    @staticmethod
    def geo_m(data_array):
        """
        funkcja przeliczajaca polozenie geograficzne na pokonana odleglosc w konkretnej sekundzie
        :param data_array:tablica z wszystkimi danymi z lotu
        :return: tablica z odleglosciami
        """
        earth_r = 12756.490 #srednica Ziemi na rowniku [km]
        delta = np.zeros(data_array.size//7-1)
        alo = data_array[0][1]
        ala = data_array[0][2]
        count = 0
        for row in data_array[1:]:
            a = (row[1] - alo) * math.cos(ala*math.pi/180.0)
            b = (row[2] - ala)
            delta[count] = math.sqrt(a*a + b*b)*math.pi*earth_r/36.0*100# wynik w m
            count += 1
            alo = row[1]
            ala = row[2]
        return delta

    @staticmethod
    def geo_m_v2(data_array):
        """
        To samo co geo_m tylko inny algorytm
        :param data_array:tablica z wszystkimi danymi z lotu
        :return:tablica z dystansem pokonanym w jednostce czasu
        """
        r = 6378.137 #promien ziemi w km
        delta = np.zeros(data_array.size//7-1)
        alo = data_array[0][1]
        ala = data_array[0][2]
        count = 0
        for row in data_array[1:]:
            dLat = (row[2] - ala) * math.pi/180.0
            dLon = (row[1] - alo) * math.pi/180.0
            a = math.sin(dLat/2.0)**2 + math.cos(ala * math.pi/180.0) * math.cos(row[2] * math.pi/180.0)\
                * math.sin(dLon/2.0)**2
            delta[count] = r * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))#w km
            count += 1
            alo = row[1]
            ala = row[2]
        return delta

    @staticmethod
    def geo_m_accumulate(data_array):
        """
        Funkcja podajadca pokonana odleglosc po czasie
        :param data_array: tablica z wszystkimi danymi z lotu
        :return: tablica z dystansem pokonanym do danej sekundy
        """
        dst = DataOperation.geo_m(data_array)
        sum = 0
        count = 0
        data = np.zeros(dst.size)
        for d in dst:
            sum += d
            data[count] = sum
            count += 1
        return data

    @staticmethod
    def speed(data_array,  time=1):
        """
        Funkcja wyliczajaca predkosc na podstawie przemieszczenia w jednej jednostce czasu
        :param data_array: tablica z wszystkimi danymi z lotu
        :param time: interwal czasowy, jedna jednostka czasu
        :return: tablica z predkoscia w danej sekundzie
        """
        dst = DataOperation.geo_m(data_array)
        speed_values = np.zeros(dst.size)
        count = 0
        for d in dst:
            speed_values[count] = d/time * 3.6# dystans jest w m, przedzial czasowy 1 s, a chcemy k/h
            count += 1
        return speed_values

    @staticmethod
    def acceleration(data_array, time=1):
        """
        Funkcja liczaca przyspieszenie w jednostce czasu ( sekundzie )
        :param data_array: tablica z wszystkimi danymi z lotu
        :param time: interwal czasowy, jedna jednostka czasu
        :return:tablica z przyspieszniem w danej sekundzie
        """
        speed = DataOperation.speed(data_array)
        acc_values = np.zeros(speed.size)
        count = 1
        acc_values[0] = 0
        for d in speed[1:]:
            acc_values[count] = (d - speed[count-1])/3.6/time
            count += 1
        return acc_values
