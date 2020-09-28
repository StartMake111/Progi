N = int(input())
k = 1
i = 1
while i < N+1:
    k *= i
    i += 1
if k < 0 or k>pow(10,9):
    exit(0)
print(k)