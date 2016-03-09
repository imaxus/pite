#!/usr/bin/env python
import InputReader
import InputValidator
import Solver
import sys

# plik wejsciowy nalezy formatowac jak w przykladzie "test" oraz podac go jako argument wywolania programu

input_read = InputReader.InputReader()
if len(sys.argv) <= 1:
    print "za malo argumentow, podaj nazwe odpowiednio sformatowanego pliku jako argument"
else:
    isOkay, size = InputValidator.InputValidator.validate(sys.argv[1])
    if isOkay:
        print Solver.Solver.solve_this(input_read.read_input(sys.argv[1], size))
    else:
        print " program zakonczyl dzialanie, bez obliczania"
