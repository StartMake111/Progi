#! /usr/bin/env python
# -*- coding: utf-8 -*-
N = int(input())
i=1
k=0
if N > pow(10,9) or N<1:
    exit(0)
while (i < 10):
    i+=1
    if (N%2==0):
        k+=1
if k>0:
    print('Составное')
else:
    print('Простое')