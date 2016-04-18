import numpy as np


class StatAnalyser:
    @staticmethod
    def chi2(mesured_y, teoretical_y, parameter_number):
        """
        Test chi^2 dla wygenerowanych danych i fitu
        :param mesured_y: wartosci wygenerowane przez DataGenerator
        :param teoretical_y: wartosci obliczone przy wykorzystaniu parametrow z fitowania
        :param parameter_number: liczba parametrow estymowanych przez fitter
        :return: wartosc testu chi^2 i wartosc znormalizowana chi^2
        """
        mes_y = np.array(mesured_y)
        teo_y = np.array(teoretical_y)
        chi = np.sum(((mes_y - teo_y)/np.std(teo_y))**2)
        normalized_chi = float(chi)/float(len(mes_y)-parameter_number)
        return chi, normalized_chi
