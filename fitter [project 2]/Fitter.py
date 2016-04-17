from scipy.optimize import curve_fit
import scipy as sy

class Fitter:
    @staticmethod
    def fit(func, data):
        p0 = sy.array([1, 1, 1])
        coeffs, matcov = curve_fit(func, data[0], data[1], p0)
        out_data = func(data[0], coeffs[0], coeffs[1], coeffs[2])
        return out_data

