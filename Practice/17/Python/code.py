a=1
maxmas, Max = -1, 0
N = [0]*37
red, black = 0, 0
while a > 0:
    a = int(input())
    if a > 36 : exit(0)
    N[a] += 1
    y = [a]
    if (a == 1 or a == 3 or a == 5 or a == 7 or a == 9 or a == 12 or a == 14 or a == 16 or a == 18 or a == 19 or a == 21 or a == 23 or a == 25 or a == 27 or a == 30 or a == 32 or a == 34 or a == 36): red+=1
    else: black+=1;
    for i in range (37):
        if N[i] > Max : Max = N[i]
    for i in range (36):
        maxmas+=1
        if N[i] == Max : print(maxmas, sep = ' ' '\n')
    maxmas = -1
    print((set(range(36)) - set(y)))
    print(red, black)