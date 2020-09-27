N = int(input())
i = 1
c = 0
while True:
    if i<N:
        c +=1
        i*=2
    else:
        break
print(c)