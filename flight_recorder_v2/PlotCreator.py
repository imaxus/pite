import matplotlib.pyplot as plt
import matplotlib as mpl
from DataOperation import DataOperation
from mpl_toolkits.mplot3d import Axes3D

class PlotCreator:
    """
    Klasa tworzaca wykresy z posiadanych danych
    """
    def __init__(self, data, time_interval):
        """
        Przy kazdej funkcji nalezy w argumencie podac True jesli chcemy zeby wyswietlila plot
        i False jesli chcemy tylko obiekt pyplot.figure np do wyswietlenia w oknie pyqt
        :param data: dane z pliku .txt zapisanego przez program
        :param time_interval: interwal czasowy - jednostka czasu
        :return:
        """
        self.data = data

        self.time = data[:, 0]
        self.lo = data[:, 1]
        self.la = data[:, 2]
        self.alt = data[:, 3]
        self.roll = data[:, 4]
        self.pitch = data[:, 5]
        self.heading = data[:, 6]
        self.time_interval =  time_interval

    def altitude_time(self, show_or_not):
        fig = plt.figure()
        plt.plot(self.time, self.alt)
        plt.xlabel('time (s)')
        plt.ylabel('wysokosc (m n.p.m)')
        plt.title('Zmiany wysokosci')
        plt.grid(True)
        plt.savefig("img/alt.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig

    def position_time(self, show_or_not):
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(self.lo, self.la, self.alt, label='parametric curve')
        ax.set_zlabel('wysokosc (m n.p.m)')
        ax.title.set_color('red')
        ax.set_xlabel('dl. geograficzna')
        ax.set_ylabel('sz. geograficzna')
        ax.legend()
        plt.title('Trasa samolotu')
        plt.savefig("img/path.png")
        if show_or_not:
            plt.show()
        return fig

    def pitch_time(self, show_or_not):
        fig = plt.figure()
        plt.plot(self.time, self.pitch)
        plt.xlabel('time (s)')
        plt.ylabel('kat wznoszenia (stopnie)')
        plt.title('Zmiany kata wznoszenia')
        plt.grid(True)
        plt.savefig("img/pitch.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig

    def roll_time(self, show_or_not):
        fig = plt.figure()
        plt.plot(self.time, self.roll)
        plt.xlabel('time (s)')
        plt.ylabel('przechyl boczny (stopnie) lewo<--->prawo')
        plt.title('Zmiany przechylu')
        plt.grid(True)
        plt.savefig("img/roll.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig

    def dst_accu_time(self, show_or_not):
        dst = DataOperation.geo_m(self.data)
        fig = plt.figure()
        plt.plot(self.time[1:], dst)
        plt.xlabel('time (s)')
        plt.ylabel('pokonana odleglosc (km)')
        plt.title('Odleglosc pokonana w danej sekundzie')
        plt.grid(True)
        plt.savefig("img/dst.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig

    def dst_time(self, show_or_not):
        dst = DataOperation.geo_m_accumulate(self.data)
        fig = plt.figure()
        plt.plot(self.time[1:], dst)
        plt.xlabel('time (s)')
        plt.ylabel('pokonana odleglosc (m)')
        plt.title('Sumaryczna odleglosc pokonana w czasie')
        plt.grid(True)
        plt.savefig("img/dst_accu.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig

    def speed_time(self, show_or_not):
        speed = DataOperation.speed(self.data, self.time_interval)
        fig = plt.figure()
        plt.plot(self.time[1:], speed)
        plt.xlabel('time (s)')
        plt.ylabel('ppredkosc (km/h)')
        plt.title('Predkosc w czasie')
        plt.grid(True)
        plt.savefig("img/speed.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig

    def acceleration_time(self, show_or_not):
        acc = DataOperation.acceleration(self.data, self.time_interval)
        fig = plt.figure()
        plt.plot(self.time[1:], acc)
        plt.xlabel('time (s)')
        plt.ylabel('pprzyspieszenie (m/s)')
        plt.title('Przyspieszenie w czasie')
        plt.grid(True)
        plt.savefig("img/acceleration.png")
        if show_or_not:
            plt.show()
        plt.close()
        return fig
