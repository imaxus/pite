import wx
import wx.lib.agw.speedmeter as SM
import time
import wx.gizmos as gizmos
from airplane_simulator import Plane


class MyFrame(wx.Frame):

    def __init__(self, parent, saver):
        pi = 3.1415
        self.start_flight_time = 0
        wx.Frame.__init__(self, parent, -1, "Flight Recorder", size=(800, 600))
        #tworzy "layout" programu
        self.panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER, size=(400, 300))
        self.panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER, pos=(400, 0), size=(400, 300))
        self.panel3 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER, pos=(0, 300), size=(400, 300))
        self.panel4 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER, pos=(400, 300), size=(400, 300))
        self.panel1.SetBackgroundColour("LIGHT GREY")
        self.panel2.SetBackgroundColour("LIGHT GREY")
        self.panel3.SetBackgroundColour("LIGHT GREY")
        self.panel4.SetBackgroundColour("LIGHT GREY")
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.panel1, 2, wx.EXPAND)
        box.Add(self.panel2, 1, wx.EXPAND)
        #predkosciomierz
        self.speed = SM.SpeedMeter(self.panel2, agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|
                                                         SM.SM_DRAW_SECONDARY_TICKS, pos=(0, 30), size=(400, 300))

        # Set The Region Of Existence Of SpeedMeter (Always In Radians!!!!)
        self.speed.SetAngleRange(-pi/6, 7*pi/6)

        # Create The Intervals That Will Divide Our SpeedMeter In Sectors
        intervals = range(0, 901, 50)
        self.speed.SetIntervals(intervals)

        # Assign The Same Colours To All Sectors (We Simulate A Car Control For Speed)
        # Usually This Is Black
        colours = [wx.BLACK]*18
        self.speed.SetIntervalColours(colours)

        # Assign The Ticks: Here They Are Simply The String Equivalent Of The Intervals
        ticks = [str(interval) for interval in intervals]
        self.speed.SetTicks(ticks)
        # Set The Ticks/Tick Markers Colour
        self.speed.SetTicksColour(wx.WHITE)
        # We Want To Draw 5 Secondary Ticks Between The Principal Ticks
        self.speed.SetNumberOfSecondaryTicks(5)

        # Set The Font For The Ticks Markers
        self.speed.SetTicksFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))

        # Set The Text In The Center Of SpeedMeter
        self.speed.SetMiddleText("Km/h")
        # Assign The Colour To The Center Text
        self.speed.SetMiddleTextColour(wx.WHITE)
        # Assign A Font To The Center Text
        self.speed.SetMiddleTextFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD))

        # Set The Colour For The Hand Indicator
        self.speed.SetHandColour(wx.Colour(255, 50, 0))

        # Do Not Draw The External (Container) Arc. Drawing The External Arc May
        # Sometimes Create Uglier Controls. Try To Comment This Line And See It
        # For Yourself!
        self.speed.DrawExternalArc(False)

        # Set The Current Value For The SpeedMeter
        self.speed.SetSpeedValue(1)

        #wysokosciomierz
        self.alt = SM.SpeedMeter(self.panel3, agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|
                                                       SM.SM_DRAW_SECONDARY_TICKS, pos=(0, 0), size=(350, 250))

        # Set The Region Of Existence Of SpeedMeter (Always In Radians!!!!)
        self.alt.SetAngleRange(-pi, pi)

        # Create The Intervals That Will Divide Our SpeedMeter In Sectors
        intervals = range(0, 11, 1)
        self.alt.SetIntervals(intervals)

        # Assign The Same Colours To All Sectors (We Simulate A Car Control For Speed)
        # Usually This Is Black
        colours = [wx.BLACK]*10
        self.alt.SetIntervalColours(colours)

        # Assign The Ticks: Here They Are Simply The String Equivalent Of The Intervals
        ticks = [str(interval) for interval in intervals]
        self.alt.SetTicks(ticks)
        # Set The Ticks/Tick Markers Colour
        self.alt.SetTicksColour(wx.WHITE)
        # We Want To Draw 5 Secondary Ticks Between The Principal Ticks
        self.alt.SetNumberOfSecondaryTicks(5)

        # Set The Font For The Ticks Markers
        self.alt.SetTicksFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))

        # Set The Text In The Center Of SpeedMeter
        self.alt.SetMiddleText("0")
        # Assign The Colour To The Center Text
        self.alt.SetMiddleTextColour(wx.WHITE)
        # Assign A Font To The Center Text
        self.alt.SetMiddleTextFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        # Set The Colour For The Hand Indicator
        self.alt.SetHandColour(wx.Colour(255, 255, 0))

        # Do Not Draw The External (Container) Arc. Drawing The External Arc May
        # Sometimes Create Uglier Controls. Try To Comment This Line And See It
        # For Yourself!
        self.alt.DrawExternalArc(False)

        # Set The Current Value For The SpeedMeter
        self.alt.SetSpeedValue(0)


        #kompass
        self.com = SM.SpeedMeter(self.panel4, agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|
                                                       SM.SM_DRAW_SECONDARY_TICKS, pos=(0, 0), size=(350, 250))

        # Set The Region Of Existence Of SpeedMeter (Always In Radians!!!!)
        self.com.SetAngleRange(-pi, pi)

        # Create The Intervals That Will Divide Our SpeedMeter In Sectors
        intervals = range(0, 9, 1)
        self.com.SetIntervals(intervals)

        # Assign The Same Colours To All Sectors (We Simulate A Car Control For Speed)
        # Usually This Is Black
        colours = [wx.BLACK]*8
        self.com.SetIntervalColours(colours)

        # Assign The Ticks: Here They Are Simply The String Equivalent Of The Intervals
        ticks = ["W", "WS", "N", "NE", "E", "EW", "S", "SN", ""]
        self.com.SetTicks(ticks)
        # Set The Ticks/Tick Markers Colour
        self.com.SetTicksColour(wx.GREEN)
        # We Want To Draw 5 Secondary Ticks Between The Principal Ticks
        self.com.SetNumberOfSecondaryTicks(2)

        # Set The Font For The Ticks Markers
        self.com.SetTicksFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))

        # Set The Text In The Center Of SpeedMeter
        self.com.SetMiddleText("")
        # Assign The Colour To The Center Text
        self.com.SetMiddleTextColour(wx.WHITE)
        # Assign A Font To The Center Text
        self.com.SetMiddleTextFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        # Set The Colour For The Hand Indicator
        self.com.SetHandColour(wx.Colour(255, 0, 0))

        # Do Not Draw The External (Container) Arc. Drawing The External Arc May
        # Sometimes Create Uglier Controls. Try To Comment This Line And See It
        # For Yourself!
        self.com.DrawExternalArc(False)

        # Set The Current Value For The SpeedMeter
        self.com.SetSpeedValue(2)

        #zegar led pokazujacy czas lotu
        self.led = gizmos.LEDNumberCtrl(self.panel1, -1, pos=(10, 30), size=(350, 80), style=gizmos.LED_ALIGN_LEFT)
        # default colours are green on black
        self.led.SetBackgroundColour("black")
        self.led.SetForegroundColour("yellow")
        #self.on_timer(None)
        self.timer = wx.Timer(self, -1)
        # update clock digits every second (1000ms)
        self.timer.Start(1000)
        MyFrame.start_flight(self, time.time())
        self.Bind(wx.EVT_TIMER, self.since_start)

        #wywolanie obiektu plane i wystartowanie jako watku, czyli wlaczenie symulatoa
        self.plane = Plane(self, saver)
        self.plane.start()

    def change_dir(self, dir):
        """
        Funkcja zmianiajaca kierunek
        :param dir: kierunek ktory chcemy ustawic
        :return:
        """
        self.com.SetSpeedValue(dir)
        self.panel4.Layout()

    def change_speed(self, sp):
        """
        Funkcja zmianiajaca predkosc
        :param sp: predkosc ktora chcemy ustawic
        :return:
        """
        self.speed.SetSpeedValue(sp)
        self.panel2.Layout()

    def change_alt(self, alt):
        """
        Funkcja zmianiajaca wysokosc
        :param alt: wysokosc ktora chcemy ustawic
        :return:
        """
        wys = int(alt/10)
        self.alt.SetSpeedValue(alt - wys*10)
        self.alt.SetMiddleText(str(int(alt)) + "m")
        self.panel3.Layout()

    def since_start(self, event):
        """
        funkcja ustawia na zegarze czas ktory minal od wywolania funkcji start_flight()
        :param event:
        :return:
        """
        #dodane 82800 bo to jest 23h *3600 sec, czas w pythonie dziala dziwnie, i przy odejmowaniu
        #czasu terazniejszego od poczatkowego dodawal godzine
        current = time.localtime(time.time() - self.start_flight_time +82800 )
        # time string can have characters 0..9, -, period, or space
        ts = time.strftime("%H %M %S", current)
        self.led.SetValue(ts)

    def start_flight(self, time_str):
        """
        Funkcja ustawie czas poczatku lotu ktory jest potrzebny do obliczenia trwania lotu
        :param time_str:
        :return:
        """
        self.start_flight_time = time_str

    @staticmethod
    def show_gui(saver):
        """
        Metoda statyczna do uruchamiania gui
        :param saver: obiekt zapisujacy klasy DataSaver
        :return:
        """
        app = wx.App()
        frame = MyFrame(None, saver)
        app.SetTopWindow(frame)
        frame.Show()
        app.MainLoop()
        return frame

    def get_plane(self):
        """
        Zwraca obiekt symulatora samolotu, zeby mozna bylo z niego pobierac dane
        :return: obiekt symulatora samolotu
        """
        return self.plane
