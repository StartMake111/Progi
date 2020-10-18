a = input().split()
b=0
for i in a:
    i = list(i)
    if len(i) != 9 :
        continue
    else :
        if i[0] == 'a' and i[4] == '5' and i[5] == '5' and i[6] == '6' and i[7] == '6' and i[8] == '1':
            print(''.join(map(str, i)))
            b += 1
if b ==0 : print(-1)