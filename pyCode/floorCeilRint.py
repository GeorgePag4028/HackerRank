#!/usr/bin/env python3

import numpy

numpy.set_printoptions(legacy='1.13')

A =[float(x) for x in input().split()]

A = numpy.array(A)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
