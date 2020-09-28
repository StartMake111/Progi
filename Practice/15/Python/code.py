#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
print('Здоровеньки булы')
A = random.randint(0,100)
a=0
while (True):
    N = int(input())
    if N > A :
        print('Загаданное число меньше')
        a+=1
    else :
        print('Загаданное число больше')
        a+=1
    if A == N:
        print('Поздравляю! Вы угадали\nХотите начаит сначала(1 - Да)')
        p = int(input())
        if p == 1:
            a = 0
            A = random.randint(0,100)
        else:
            exit(0)
    if a == 5:
        print('Вы не угадали\n Загаданное число:'), (A),('\nХотите начаит сначала(1 - Да)')
        p = int(input())
        if p == 1:
            a = 0
            A = random.randint(0,100)
        else:
            exit(0)
