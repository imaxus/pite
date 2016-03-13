import wx
import wx.lib.agw.speedmeter as SM
import time
import wx.gizmos as gizmos


class MyFrame(wx.Frame):

    def __init__(self, parent):
        pi = 3.1415
        wx.Frame.__init__(self, parent, -1, "Flight Recorder", size=(800, 600))

        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER, size=(400, 300))
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER, pos=(400, 0), size=(400, 300))
        panel1.SetBackgroundColour("LIGHT GREY")
        panel2.SetBackgroundColour("LIGHT GREY")
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 2, wx.EXPAND)
        box.Add(panel2, 1, wx.EXPAND)
        self.speed = SM.SpeedMeter(panel2, agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|
                                                  SM.SM_DRAW_SECONDARY_TICKS, pos=(0, 30), size=(400, 300))

        # Set The Region Of Existence Of SpeedMeter (Always In Radians!!!!)
        self.speed.SetAngleRange(-pi/6, 7*pi/6)

        # Create The Intervals That Will Divide Our SpeedMeter In Sectors
        intervals = range(0, 401, 20)
        self.speed.SetIntervals(intervals)

        # Assign The Same Colours To All Sectors (We Simulate A Car Control For Speed)
        # Usually This Is Black
        colours = [wx.BLACK]*20
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

        self.led = gizmos.LEDNumberCtrl(panel1, -1, pos=(0, 100), size=(350, 80), style=gizmos.LED_ALIGN_LEFT)
        # default colours are green on black
        self.led.SetBackgroundColour("black")
        self.led.SetForegroundColour("yellow")
        self.on_timer(None)
        self.timer = wx.Timer(self, -1)
        # update clock digits every second (1000ms)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.on_timer)
        #self.Centre()

    def change_speed(self, sp):
        self.speed = sp

    def on_timer(self, event):
        # get current time from computer
        current = time.localtime(time.time())
        # time string can have characters 0..9, -, period, or space
        ts = time.strftime("%H %M %S", current)
        self.led.SetValue(ts)


app = wx.App()
frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()