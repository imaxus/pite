from DataGenerator import DataGenerator
from Plotter import Plotter
from Fitter import Fitter
import math
import numpy as np
import scipy as sy

if int(raw_input("Jesli chcesz domysle wartosci -1, jesli nie -2\n")) == 1:
    per = float(raw_input("podaj liczbe okresow\n"))
    fr = float(raw_input("podaj frame_rate\n"))
    fq = float(raw_input("podaj czestotliwosc\n"))
    ns = float(raw_input("podaj poziom szumu\n"))
    am = float(raw_input("podaj amplitude\n"))
    off = float(raw_input("podaj offset\n"))
else:
    per = 4
    fr = 44100
    fq = 200
    ns = 100
    am = 1
    off = 0
generator = DataGenerator()
generator.change_number_of_periods(per)
generator.change_framerate(fr)
generator.change_frequency(fq)
generator.change_noise(ns)
generator.change_amplitude(am)
generator.change_offset(off)


def my_sin(x, freq, amplitude, phase, offset):
    #musi byc list comprehention bo wywala blad przy mnozeniu listy przez float'a
    return np.sin([i * freq + phase for i in x]) * amplitude + offset
p0 = sy.array([1,1,1,1])


def func(x, a, b, c):
        return a*x**b + c

if int(raw_input("sin -1, weird function -2\n")) == 1:
    gen_func = math.sin
    p0 =[]
    p1 = [1, 1, 1, 1]
    fit_func = my_sin
else:
    gen_func = func
    print "dziwne rownanie a*x^b + c"
    p0 = [float(raw_input("podaj wps. a\n")), float(raw_input("podaj wps. b\n")), float(raw_input("podaj wps. c\n"))]
    fit_func = func
    p1 = [1, 1, 1]

data_points = generator.generate_data_points(gen_func, p0)

fit_data_y = Fitter.fit(fit_func, data_points, p1)
fit_data = [data_points[0], fit_data_y]

plot = Plotter()
plot.plot_data_points(data_points)
plot.plot_fit_curve(fit_data)
plot.show_plot()

