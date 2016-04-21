import numpy as np

def calc(samples):
    ret_means =[]
    temp_array = np.array(samples)
    print temp_array
    for ind, val in enumerate(temp_array):
        ret_means.append(val.mean())
        print "Mean value for ", ind, " sample is ", val.mean()
    return ret_means