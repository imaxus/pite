#!/usr/bin/env python
import numpy as np

#dorobic wlasny solver
class Solver:
    @staticmethod
    def solve_this(data):
        """
        :param data: numpy array
        :return: two floats, wynik rozwiazania
        """
        return np.linalg.lstsq(data[:, [0, 1]], data[:, [2]])[0]
