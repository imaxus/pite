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
        self.acceleration = 0.3 #m/s^2 bylo 1.44
        self.timeStart = None
        self.timeStop = 0
        self.velocity_p = 0
        self.takeoff = False
        self.distance = 0
        self.timeTakeOFF = 0
        self.distanceRunway = 0
        self.flying = False
        #okresla co ile dokonujemy sprawdzenia wartosci i ich zmiany
        self.second_factor = 0.2
        #wspolczynnik przyspieszenia, im szybciej lecimy tym wolniej przyspieszamy
        self.acc_factor = 1.1
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
                speed = self.velocity * 3.6
                self.drawer.change_speed(speed)
                self.drawer.change_alt(self.height)
                #self.saver.save_data([speed, self.height, 0, 0, 0, 0])
                if self.takeoff == False:
                    self.ifTakeOFF()
                else:
                    self.FlihtMode()
                time.sleep(self.second_factor)
        except KeyboardInterrupt:
            print "Ewakuacja, lot odwolany"

    def ifTakeOFF(self):
        if self.velocity > 40:
            if self.takeoff == False:
                print "Samolot wystartowal"
            self.takeoff = True
            self.timeTakeOFF = time.time()

    def upvelocity(self):
        if self.velocity*3.6 < 700:
            self.up_acc()
            print self.acceleration
            self.velocity = self.velocity_p + self.acceleration*(time.time() - self.timeStart)*self.second_factor

    def upDistance(self):
        if self.takeoff == False:
            self.distanceRunway = (self.acceleration*self.getTime()*self.getTime())/2
        else:
            self.distance += self.velocity*math.cos(math.radians(self.angle))

    def FlihtMode(self):
        if (self.height < 4000) and (self.angle < 30) and self.velocity < 100:
            self.angle += 0.3
        if (self.height < 4000) and (self.angle < 30) and self.velocity >= 100:
            self.angle -= 0.2
        if self.height > 4000:
            self.angle = 0
        self.height += self.second_factor*(self.angle/10)

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

    #def up_height(self):
     #   #60 metrow na minute to srednia predkosc wznoszenia sie boeinga 737
      #  if self.velocity*3.6 > 120 and self.height < 10000:
       #     # bo 60 metrow na minute wiec 1 m na sek, a sprawdzamy co second_factor wiec tak tez ustawiamy
        #    self.height += self.second_factor

    def up_acc(self):
        if self.acceleration < 9.0 and self.velocity < 65:
            self.acceleration += 0.15
        #if self.velocity > 75 and self.acceleration > 3.0:
         #   self.acceleration -= 0.1
