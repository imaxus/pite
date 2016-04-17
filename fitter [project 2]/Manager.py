from DataGenerator import DataGenerator
from Plotter import Plotter
import math


generator = DataGenerator()
generator.change_number_of_periods(4)
generator.change_framerate(44100)
generator.change_frequency(100)
generator.change_noise(200)
data_points = generator.generate_data_points(math.sin)
Plotter.plot_data_points(data_points)

