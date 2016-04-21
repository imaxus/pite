import sys
from ParaProcessor import Process


args = sys.argv[1:]
pas_args = []
if len(args) > 3:
    print " Too many arguments"
    sys.exit()
for a in args:
    if type(a) == int:
        pas_args.append(a)
    if type(a) == float:
        pas_args.append(a)
    if type(a) == str:
        pas_args.append(a)
if len(pas_args) == 0:
    print "Please provide the program with 3 parameters : int number and/or float number and/or string"
    sys.exit()
Process.proc(pas_args)
