#!/usr/bin/python
import time
import math
import threading

class Plane(threading.Thread):
    def __init__(self, drawer, saver):
        threading.Thread.__init__(self)
        print "Welcome to airlines"
        self.velocity = 0
        self.height = 0
        self.angle = 0
        self.acceleration = 1.44 #m/s^2
        self.timeStart = None
        self.timeStop = 0
        self.velocity_p = 0
        self.takeoff = False
        self.distance = 0
        self.timeTakeOFF = 0
        self.distanceRunway = 0
        self.flying = False
        #obiekt gui potrzebny do przekazania argumentow w celu zmiany wartosci
        #musi tak byc bo to jest obiekt watku i w przypadku proby wywolania w glownym watku bedzie czekac na zakonczenie
        #dzialania symulatora
        self.drawer = drawer
        self.saver = saver
        #zmienna do wyliczania wysokosci
        self.up_time = 0

    #a'ka plane_start
    def run(self):
        self.timeStart = time.time()
        self.flying = True
        Plane.update(self)

    def planeStop(self):
        self.timeStop = time.time()
        self.flying = False
        print (self.timeStop - self.timeStart)

    def update(self):
        try:
            while self.flying:
                self.upvelocity()
                self.upDistance()
                self.up_height()
                speed = self.velocity * 3.6
                self.drawer.change_speed(speed)
                self.drawer.change_alt(self.height)
                self.saver.save_data([speed, self.height, 0, 0, 0, 0])
                if self.takeoff == False:
                    self.ifTakeOFF()
                else:
                    self.FlihtMode()
                time.sleep(0.2)
        except KeyboardInterrupt:
            print "Ewakuacja, lot odwolany"

    def ifTakeOFF(self):
        if self.velocity > 80:
            if self.takeoff == False:
                print "Samolot wystartowal"
            self.takeoff = True
            self.timeTakeOFF = time.time()

    def upvelocity(self):
        if self.velocity*3.6 < 900:
            self.velocity = self.velocity_p + self.acceleration*(time.time() - self.timeStart)*0.2

    def upDistance(self):
        if self.takeoff == False:
            self.distanceRunway = (self.acceleration*self.getTime()*self.getTime())/2
        else:
            self.distance += self.velocity*math.cos(math.radians(self.angle))

    def FlihtMode(self):
        if (self.height < 2000) & (self.angle < 40):
            self.angle += 0.1
        self.height += self.velocity*math.sin(math.radians(self.angle))

    def getTime(self):
        return time.time() - self.timeStart

    def getTimeTakeoff(self):
        return time.time() - self.timeTakeOFF

    def printLogs(self):
        print '-------------------'
        print 'Czas',time.time() - self.timeStart
        print 'Speed ',self.velocity * 3.6,"km/h   //  ",self.velocity,"m/s"
        print 'Dystans', self.distance
        print 'Dystans na pasie', self.distanceRunway
        print 'height ',self.height
        print 'Kat wznoszenia',self.angle

    def up_height(self):
        #60 metrow na minute to srednia predkosc wznoszenia sie boeinga 737
        if self.velocity*3.6 > 40:
            # bo 60 metrow na minute wiec 1 m na sek, a sprawdzamy co 0.2
            self.height += 0.2
