#! /usr/bin/env python
# -*- coding: utf-8 -*-


a,B,b = map(str, input().split())
a, b = int(str_a)
if B != '+' or B != '-' or B = '*' or B = '/':
    print('Калькулятор не понимать человека')
if B == '+':
    print(a+b)
elif B == '-':
    print(a-b)
elif B == '*':
    print(a*b)
elif B == '/':
    if b == 0:
        print('на ноль делить нельзя')
        exit(0)
    print(a/b)
else :
    print('Давай миша, все по новой')
    exit(0)


