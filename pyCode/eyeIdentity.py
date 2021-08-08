#!/usr/bin/env python3

import numpy 
numpy.set_printoptions(legacy='1.13')

N,M = map(int,input().split())
print( numpy.eye(N,M))
