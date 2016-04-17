import matplotlib.pyplot as plt
import matplotlib as mpl


class Plotter:
    def __init__(self):
        self.var = 1

    def plot_data_points(self, data):
        """
        Funkcja rysujaca wykres punktow
        :param data: lista punktow w postaci krotki : x_values, y_values
        :return: void
        """
        plt.plot(data[0], data[1], 'ro')

    def plot_fit_curve(self, data):
        plt.plot(data[0], data[1])

    def show_plot(self):
        plt.show()