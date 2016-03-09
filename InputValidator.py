#!/usr/bin/env python


class InputValidator:
    @staticmethod
    def validate(file_name):
        """
        funkcja sprawdzajaca poprawnosc danych w pliku, przyjmuje jako argument nazwe pliku
        sprawdza czy ilosc argumentow w kazdej lini sie zgadza, zwraca true jesli tak lub false jesli nie,
        okresla rowniez czy argumenty sa liczbami,
        zwraca jak drugi argument ilosc ukladow
        :param file_name: string, nazwa pliku z danymi
        :return: tuple (bool,int), okresla czy plik poprawny oraz zwraca ilosc lini w pliku
        :return: tuple (bool,int), okresla czy plik poprawny oraz zwraca ilosc lini w pliku
        """
        counter = 0
        line_count = 0
        is_okay = True
        try:
            with open(file_name, 'r') as f:
                for lines in f:
                        counter += 1
                        temp = lines.split(',')
                        for s in temp:
                            line_count += 1
                            if InputValidator.is_number(s):
                                continue
                            else:
                                is_okay = False
                                print "Niepoprwne dane w pliku, badz zle formatowanie"
                                exit()
                        if line_count != 3:
                            print "nieodpowiednia ilosc argumentow w lini %d " % counter
                            exit()
                        else:
                            line_count = 0
            return is_okay, counter
        except:
            print "wystapil problem podczas otwierania pliku, \n" \
                  "sprawdz czy nazwa jest poprawna i sprobuj ponownie"
            return False, 0

    @staticmethod
    def is_number(number):
        """
        :param number: string ktory chcemy sprawdzic czy jest liczba
        :return: tak jesli argument jest liczba, nie jesli nie jest
        """
        try:
            float(number)
            return True
        except ValueError:
            return False
