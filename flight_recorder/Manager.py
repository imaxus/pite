from Data_saver import DataSaver
from Drawer import MyFrame

from airplane_simulator import Plane
import wx

conn = DataSaver.connect_to_db()
#conn = DataSaver.debug_mode_no_internet()
#stworzenie obiektu zapisujacego
saver = DataSaver(conn)
#wywolanie gui
gui = MyFrame.show_gui(saver)

#dodac czas lotu i jakos emulowac predkosc
