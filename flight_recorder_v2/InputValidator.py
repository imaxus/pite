class InputValidator:
    """
    Klasa sprawdzajaca poprawnosc wprowadzonych danych
    """
    @staticmethod
    def input_val(data):
        """
        Metoda sprawdzajaca czy wszystkie wprowadzone dane to liczby,
        oraz czy buffor nie zwrocil wartosci False okreslajacej brak danych
        :param data: tablica lub lista o 7 pozycjach, tylko numery
        :return:
        """
        if not data:
            print "Bufor nie uzyskal danych w okreslonym czasie, " \
                  "najprawdopodobniej ktores z urzadzen pomiarowych dziala niepoprawnie"
            return False
        flag = True
        for i in data:
            #sprawda czy w tablicy znajduja sie tlyko liczby
            if not isinstance(i, (int, long, float, complex)):
                flag = False
        return flag

