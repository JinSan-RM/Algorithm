import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(range(1, N+1))

for k in range(M):
    temp = 0
    i, j = map(int, sys.stdin.readline().split())
    temp = lst[i - 1 : j]
    temp.reverse()
    lst[i - 1 : j] = temp
    
for p in lst:
    print(p, end=' ')
