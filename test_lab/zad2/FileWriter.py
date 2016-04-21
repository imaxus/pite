import numpy as np


def write_gen_to_file(tab):
    temp_array = list(tab)
    with open("gen.txt", 'w') as f:
        for n in temp_array:
            string = ""
            for m in n:
                string = string + str(m)+ " "
            f.write(string+"\n")



def write_mean_to_file(tab):
    temp_array = list(tab)
    with open("means.txt", 'w') as f:
        for ind, val in enumerate(temp_array):
            string = "Row "+ str(ind+1) + " mean value is " + str(val)+"\n"
            f.write(string)
