#analysis.py

import sys
import numpy
import detector

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    detector.detect_problems(filename)
    data = numpy.loadtxt(fname=filename, delimiter=",")
    print(data.mean())

main()