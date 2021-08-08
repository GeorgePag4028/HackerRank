#!/usr/bin/env python3
import numpy

N,M = map(int,input().split())
A = []
for i in range(N):
  A.append([int(x) for x in input().split()])

A = numpy.array(A)
A = numpy.sum(A,axis =0)
A = numpy.prod(A)
print(A)

