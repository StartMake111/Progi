import itertools as it
otvet = []
dlinna = int(input())
slovo = input()
slovo = list(slovo)
lk = len(slovo)
op = []
if dlinna > len(slovo):
    lish = dlinna - len(slovo)
    b = list(it.permutations(slovo, lish))
    for i in b:
        for j in i:
            slovo.append(j)
        a = [el for el in it.permutations(slovo, dlinna)]
        for i in range (len(a)):
            otvet.append(''.join(map(str, a[i])))
        del slovo[lk::]
    h = list(set(otvet))
    for g in range(len(h)):
        print(h[g], end=' ')
else:
    for i in list(it.permutations(slovo, dlinna)):
        print(''.join(map(str, i)), end=' ')