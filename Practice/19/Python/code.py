import itertools
x = int(input())
a = input()
if len(str(a)) < x :
    a = list(a)
    a += a[0]
    a = ''.join(map(str, a))
result = ''.join(map(str, itertools.permutations(a, x)))
print(result)