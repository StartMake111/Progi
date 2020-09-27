from array import *
s1 = array('i', [0,1])
s2 = array('i', [0,1])
s, s1[0], s1[1], s2[0], s2[1] =map(int, input().split())
if (pow(10,-15) > s, s1[0], s1[1], s2[0], s2[1]) or (s, s1[0], s1[1], s2[0], s2[1] > pow(10,15)):
    exit(0)
if s1[0] > s1[1] or s2[0] > s2[1]:
    exit(0)
if s1[0] + s2[1] == s or s1[0] + s2[0] == s :
    print(s1[0] , + s - s1[0])
    exit(0)
if s1[1] + s2[0] == s or s1[1] + s2[1] == s :
    print(s1[1] , + s - s1[1])
    exit(0)
else :
    print("-1")