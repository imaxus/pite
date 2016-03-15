import psycopg2
from Data_saver import DataSaver
from Drawer import MyFrame
from airplane_simulator import Plane
import wx
import threading
from threading import Thread

try:
    conn = psycopg2.connect("dbname='pg23138_flight_recorder' user='pg23138_flight_recorder'"
                            " host='23138.p.tld.pl' password='flight4Reco'")
except:
    print "I am unable to connect to the database"
    quit()

#stworzenie obiektu zapisujacego
saver = DataSaver(conn)
#wywolanie gui
gui = MyFrame.show_gui(saver)

#dodac czas lotu i jakos emulowac predkosc
