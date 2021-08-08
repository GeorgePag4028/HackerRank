#!/usr/bin/env python3
import numpy 

N,M = map(int,input().split())
A = []
B = []
for i in range(N) :
  A .append([int(x) for x in input().split()])

for i in range(N) :
  B .append([int(x) for x in input().split()])

A = numpy.array(A,int)
B = numpy.array(B,int)
#print(A)
#print(B)
print(str(A+B))
print(str(A-B))
print(str(A*B))
print(str(A//B))
print(str(A%B))
print(str(A**B))
