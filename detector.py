#This tests the files for correctness

import numpy

def detect_problems(filename):
    data = numpy.loadtxt(fname=filename, delimiter=",")
    if data.max(axis=0)[-1] == 20:
        print("Something is wrong with the maxima")
    elif data.min(axis=0).sum() > 1:
        print("Minima add up to zero")
    else:
        print("The file looks good.")
