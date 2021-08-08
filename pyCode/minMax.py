#!/usr/bin/env python3
import numpy

N,M = map(int,input().split())
A = []
for i in range(N):
  A.append([int(x) for x in input().split()])

A = numpy.array(A)
A = numpy.min(A,axis =1)
A = numpy.max(A)
print(A)

