import time


class Buffer:
    """
    Klasa buforowa dla danych dostarczanych z "samolotu",
    zapisuje dane albo pojedynczo albo zzbiorczo z listy lub tabeli
    """
    def __init__(self):
        # druga wartosc w tabelach okresla ile razy nastapil zapis, a musi wystapic dokladnie raz
        # gdy jeden komponent odswieza czesciej niz inny to wartosci nadmiarowe beda porzucane
        self.time = [0, 0]
        self.lo = [0, 0]
        self.la = [0, 0]
        self.alt = [0, 0]
        self.roll = [0, 0]
        self.pitch = [0, 0]
        self.heading = [0, 0]
        #okresla czy chcemy czekac na komplet danych
        self.wait_for_data = True
        #okresla czas jednego cyklu oczekiwania
        self.wait_time = 0.1
        #ilosc cykli oczekiwania, total w8 time = wait_time * wait_cycle
        self.wait_cycle = 10

        self.accumulate = [self.time, self.lo, self.la, self.alt, self.roll, self.pitch, self.heading]

    def set_data(self, data):
        """
        Funkcja zapisujaca dane z tabeli, w przypadku kiedy dane czytane np z pliku
        :param data: tablica 7 wartosci w postaci [self.time, self.lo, self.la, self.alt, self.roll, self.pitch, self.heading]
        :return:
        """
        self.set_time(data[0])
        self.set_longitude(data[1])
        self.set_altitude(data[2])
        self.set_alt(data[3])
        self.set_roll(data[4])
        self.set_pitch(data[5])
        self.set_heading(data[6])

    def set_time(self, timex):
        self.time[0] = timex
        self.time[1] = 1

    def set_longitude(self, lo):
        self.lo[0] = lo
        self.lo[1] = 1

    def set_altitude(self, la):
        self.la[0] = la
        self.la[1] = 1

    def set_alt(self, alt):
        self.alt[0] = alt
        self.alt[1] = 1

    def set_roll(self, roll):
        self.roll[0] = roll
        self.roll[1] = 1

    def set_pitch(self, pi):
        self.pitch[0] = pi
        self.pitch[1] = 1

    def set_heading(self, hd):
        self.heading[0] = hd
        self.heading[1] = 1

    def get_data(self):
        """
        Zwraca wartosci w tablicy w postaci [self.time, self.lo, self.la, self.alt, self.roll, self.pitch, self.heading]
        w przypadku braku jakiejs wartosci w buforze usypia program na 1/10 s i sprawdza ponownie, max 1 sek
        :return: lista wartosci
        """
        is_poss = True
        count = 0
        while is_poss:
            if self.wait_for_data:
                if self.ready_to_send():
                    return [i[0] for i in self.accumulate]
                elif count < self.wait_cycle:
                    count += 1
                    time.sleep(self.wait_time)
                else:
                    break
            else:
                return [i[0] for i in self.accumulate]
        return False

    def ready_to_send(self):
        """
        Funkcja sprawdzajaca czy dla wszystkich w zmiennych zostala wpisana przynajmniej jedna wartosc
        :return: bool , true jesli buffor jest pelny, false w przeciwnym wypadku
        """
        flag = True
        for i in self.accumulate:
            if i[1] < 1:
                flag = False
        return flag
