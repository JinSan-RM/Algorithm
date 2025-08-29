import sys
P = sys.stdin.readline().split()

res = [1, 1, 2, 2, 2, 8]

for i in range(len(P)):
    if int(P[i]) > res[i]:
        res[i] = res[i] - int(P[i])
    elif int(P[i]) == res[i]:
        res[i] = 0
    elif int(P[i]) < res[i]:
        res[i] = res[i] - int(P[i])

print(*res, sep=' ')
    
