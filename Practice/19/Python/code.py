import itertools
x = int(input())
a = input()
b = []
if len(str(a)) < x :
    a = list(a)
    a += a[0]
    a = ''.join(map(str, a))
result = [item for item in itertools.permutations(a,x)]
for i in result:
    for j in range(len(i)):
        b += i[j]
    print(''.join(map(str,b)), sep=' ', end= ' ')
    b.clear()