#! /usr/bin/env python
# -*- coding: utf-8 -*-
a,c = map(int, input().split(':'))
a1,c1 = map(int, input().split(':'))
T1 = 60 * a + c
T2 = 60 * a1+ c1
if a > 24 or c > 60 or a1 > 24 or c1 > 60 or a < 0 or c < 0 or a1<0 or c1 < 0:
    exit(0)
if abs(T1-T2)>0 and abs(T1-T2)<16 :
    print('Встреча состоится')
else :
    print('Встреча не состоится')