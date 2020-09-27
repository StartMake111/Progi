N = int(input())
k = 1
i = 1
if N < 0 or N>pow(10,9):
    exit(0)
while i < N+1:
    k *= i
    i += 1
print(k)