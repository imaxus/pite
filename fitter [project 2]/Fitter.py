from scipy.optimize import curve_fit

class Fitter:
    @staticmethod
    def fit(func, p0, data):
        """
        Funkcja fittujaca krzywa do danych
        :param func: funkcja przyjmujaca 4 argumenty (x, freq, amplitude, phase, offset)
        :param data: lista punktow w postaci krotki : x_values[], y_values[]
        :param p0: lista wartosci p0 do funkcji
        :return: zfitowane wartosci y (bez x)
        """
        fit = curve_fit(func, data[0], data[1], p0)
        out_data = func(data[0], *fit[0])
        return out_data
