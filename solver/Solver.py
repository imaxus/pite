#!/usr/bin/env python
import numpy as np


class Solver:
    @staticmethod
    def solve_this(data):
        which_solver = raw_input("Wow ten program posiada dwa solvery, ktorego chcesz uzyc ?\n"
                                 "1-super hiper solver, 2-numpy solver ->>>>  ")
        if which_solver == "2":
            Solver.np_solve(data)
        elif which_solver == "1":
            Solver.super_solve(data)
        else:
            print "Podales zly numer, program sie obrazil"
            exit()

    @staticmethod
    def np_solve(data):
        """
        :param data: numpy array
        :return: two floats, wynik rozwiazania
        """
        print np.linalg.lstsq(data[:, [0, 1]], data[:, [2]])[0]

    @staticmethod
    def super_solve(data):
        """
        :param data: numpy array
        :return: two floats, wynik rozwiazania
        """
        wg = data[0][0]*data[1][1] - data[0][1]*data[1][0]
        wx = data[0][2]*data[1][1] - data[0][1]*data[1][2]
        wy = data[0][0]*data[1][2] - data[0][2]*data[1][0]

        if wg == 0.0 and wx == 0.0 and wy == 0.0:
            print "uklad jest nieoznaczony"
            exit()
        elif wg == 0.0 and wx != 0.0 and wy != 0.0:
            print "uklad jest sprzeczny"
            exit()
        else:
            a = float(wx/wg)
            b = float(wy/wg)
            print a, "  ", b
