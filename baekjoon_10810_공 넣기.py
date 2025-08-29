import sys
N, M = map(int, sys.stdin.readline().split())
lst = [0] * N

for i in range(M):
    C = list(map(int, sys.stdin.readline().split()))
    start_p, end_p, variable_num = C[0], C[1], C[2]
    
    for j in range(start_p - 1, end_p):
        lst[j] = variable_num
        
for k in lst:
    print(k, end=' ')
