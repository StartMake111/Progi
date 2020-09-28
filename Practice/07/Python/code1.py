#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
print('Viberi sposob resheniya. 1 cherez storoni , 2 cheres koordinati  ')
a = int(input())
if a == 1 :
    print ('Vvedi dlini storon v novoy stroke')
    x = int(input())
    y = int(input())
    z = int(input())
    if x==0 or y==0 or z==0 or x + y > z or x+z>y or z+y > x :
        print('Это не треугольник')
        exit(0)
    if x < 0 or y < 0 or z < 0 :
        print('Ошибкааааа, не бывает отрицательной длинны')
        exit(0)
    p = (x+y+z)/2
    S = math.sqrt(p*(p-x)*(p-y)*(p-z))
    print ('S = '), (S)
if a == 2 :
    print ('Vvedi koordinati cherez probel')
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if (x1 == x2 and y1 == y2 or x2 == x3 and y2 == y3 or x1 == x3 and x1 == x3):
        print('Ошибка, нет треугольника')
        exit(0)
    S = abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
    print('S = '), (S)
