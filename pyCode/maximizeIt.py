#!/usr/bin/env python3
from sys import stdin
K,M = map(int,input().split())

print(K,M)
A = []
B = []
for i in range(K):

  A.append([int(x) for x in input().split()])
for i in range(len(A)):
  C = []
  for j in range(1,len(A[i])):
    C.append(A[i][j]*A[i][j])
  B.append(C)
print(B)

for i in range(len(B)):
  for item0
  
