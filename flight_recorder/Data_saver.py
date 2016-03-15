import psycopg2


class DataSaver:
    def __init__(self, conn):
        """
        :param cur: polaczenie do bazy danych
        :return: void
        """
        self.conn = conn
        self.speed = 0
        self.alt = 0
        self.climb = 0
        self.direction = 0
        self.banking = 0
        self.fuel = 0

    def save_data(self, data):
        """
        Funkcja zapisujaca dane do bazy
        :param data: tablica zawierajaca wszystkie potrzebne wartosci
        :return: true jesli sie powiodlo, false jesli byl blad w bazie
        """
        DataSaver.save_speed(self, data[0])
        DataSaver.save_alt(self, data[1])
        DataSaver.save_climb(self, data[2])
        DataSaver.save_dir(self, data[3])
        DataSaver.save_bank(self, data[4])
        DataSaver.save_fuel(self, data[5])
        #stworzenie kursora bazy danych
        cur = self.conn.cursor()
        try:
            statement = 'INSERT INTO flight (speed,alt,climb,direction,banking,fuel) ' \
                        'VALUES (%s, %s, %s, %s, %s, %s);' % \
                        (self.speed, self.alt, self.climb, self.direction, self.banking, self.fuel)
            #print statement
            cur.execute(statement)
            self.conn.commit()
            cur.close()
        except:
            print "there was an error during data sending"
            return False
        return True

    def save_speed(self, sp):
        self.speed = sp

    def save_alt(self, alt):
        self.alt = alt

    def save_climb(self, climb):
        self.climb = climb

    def save_dir(self, dire):
        self.direction = dire

    def save_bank(self, bank):
        self.banking = bank

    def save_fuel(self, ful):
        self.fuel = ful

    @staticmethod
    def connect_to_db():
        try:
            conn = psycopg2.connect("dbname='pg23138_flight_recorder' user='pg23138_flight_recorder'"
                                    " host='23138.p.tld.pl' password='flight4Reco'")
        except:
            print "I am unable to connect to the database"
            quit()
        return conn

    @staticmethod
    def debug_mode_no_internet():
        return 0