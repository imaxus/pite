from DataGenerator import DataGenerator
from Plotter import Plotter
from Fitter import Fitter
import math
import numpy as np


generator = DataGenerator()
generator.change_number_of_periods(4)
generator.change_framerate(44100)
generator.change_frequency(100)
generator.change_noise(200)
data_points = generator.generate_data_points(math.sin)


def my_sin(x, freq, amplitude, offset):
    return np.sin(x * freq) * amplitude + offset
p0 = [1,1,1]

fit_data_y = Fitter.fit(my_sin, p0, data_points)
fit_data = [data_points[0], fit_data_y]
print len(data_points[0])
print len(fit_data_y)
plot = Plotter()
plot.plot_data_points(data_points)
plot.plot_fit_curve(fit_data)
plot.show_plot()

