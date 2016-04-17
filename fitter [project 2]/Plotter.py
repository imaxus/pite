import matplotlib.pyplot as plt
import matplotlib as mpl


class Plotter:
    @staticmethod
    def plot_data_points(data):
        """
        Funkcja rysujaca wykres punktow
        :param data: lista punktow w postaci krotki : x_values, y_values
        :return: void
        """
        plt.plot(data[0], data[1], 'ro')
        plt.xlabel('czas')
        plt.ylabel('cos')
        plt.title('Wylosowane punkty')
        plt.show()
