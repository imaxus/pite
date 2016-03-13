import psycopg2
from Data_saver import DataSaver

try:
    conn = psycopg2.connect("dbname='pg23138_flight_recorder' user='pg23138_flight_recorder'"
                            " host='23138.p.tld.pl' password='flight4Reco'")
except:
    print "I am unable to connect to the database"
    quit()

#stworzenie obiektu zapisujacego
saver = DataSaver(conn)

data = [1, 2.15, 0.1, 3, 4, 99]
saver.save_data(data)

#dodac czas lotu i jakos emulowac predkosc
