import random
import numpy as np
from Calculator import calc
from FileWriter import *
n = int(raw_input("Please write the number of samples \n"))
m = int(raw_input("Please write the number of numbers in one sample \n"))
s_zakres = float(raw_input("Please write the lowest random number You want \n"))
e_zakres = float(raw_input("Please write the highest random number You want \n"))

rnd_numbers = [[random.uniform(s_zakres, e_zakres) for k in range(m)] for i in range(n)]
write_gen_to_file(rnd_numbers)
write_mean_to_file(calc(rnd_numbers))
