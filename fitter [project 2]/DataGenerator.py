import random
import math


class DataGenerator:
    def __init__(self):
        self.number_data_points = 4
        self.offset = 0
        self.frequency = 100
        self.frame_rate = 4000
        self.amplitude = 0.5
        self.noise = 10

    def set_multiple_data(self, dat, fq, fr, amp, off, ns):
        """
        Funkcja umozliwiajaca ustawienie wszystkich parametrow na raz
        :param dat: ilosc okresow
        :param fq: czestotliwosc
        :param fr: frame rate
        :param amp: amplituda
        :param off: offset
        :param ns: noise level
        :return: void
        """
        self.number_data_points = dat
        self.offset = off
        self.frequency = fq
        self.frame_rate = fr
        self.amplitude = amp
        self.noise = ns

    def generate_data_points(self, func, p0):
        """
        Funkcja generujaca losowe punkty w oparciu o fale sinusoidalna (dzwiek)
        :param func: funkcja ktorej ma uzyc generator
        :param p0: function argument list
        :return: lista punktow w postaci krotki : x_values, y_values
        """
        period = int(self.frame_rate / self.frequency)
        #tworzymy jeden okres danych wejsciowych dla sinusa, czyli wartosci x dla pierwszych 2pi
        datax = [(2.0*math.pi*float(self.frequency)*(float(i % period)/float(self.frame_rate)) + self.offset)
                 for i in xrange(period)]
        #powielamy jeden okres razy zadana ilosc okresow "+(i/period)*2.0*math.pi" jest przesunieciem
        datax = [datax[i % period]+(i/period)*2.0*math.pi for i in range(int(period * self.number_data_points))]
        # szum dodany dwa razy zeby i wartosci x'owe i y'owe sie zmienialy
        datay = [float(self.amplitude) * func(x + self.white_noise(), *p0)+self.white_noise() for x in datax]
        return datax, datay

    def white_noise(self):
        """
        Funkcja generujaca szum, szum nalezy ustawic w granicach 100-300 zeby byl widoczny,
        ale zeby nie zaburzal funkcji.
        :return: losowa wartosc szumu
        """
        return float(self.amplitude) * random.uniform(-float(self.noise)/2.0/100, float(self.noise)/2.0/100)

    def change_framerate(self, fr):
        """
        Funkcja zmieniajaca wartosc frame rate
        :param fr: nowa wartosc frame rate
        :return: void
        """
        self.frame_rate = fr

    def change_offset(self, off):
        """
        Funkcja zmieniajaca offset
        :param off: nowa wartosc offsetu
        :return: void
        """
        self.offset = off

    def change_noise(self, ns):
        """
        Funkcja zmieniajaca szum
        :param ns: nowa wartosc szumu
        :return: void
        """
        self.noise = ns

    def change_amplitude(self, amp):
        """
        Funkcja zmieniajaca amplitude
        :param amp: nowa wartosc amplitudy
        :return: void
        """
        self.amplitude = amp

    def change_number_of_periods(self, number):
        """
        Funkcja zmieniajaca ilosc okresow
        :param number: nowa ilosc okresow
        :return: void
        """
        self.number_data_points = number

    def change_frequency(self, fq):
        """
        Funkcja zmieniajaca czestotlliwosc
        :param fq: nowa wartosc czestotliwosci
        :return: void
        """
        self.frequency = fq
