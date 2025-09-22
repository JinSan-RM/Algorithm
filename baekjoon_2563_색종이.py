import sys
N = int(input())

res = []
for i in range(N):
    vector_low = list(map(int, sys.stdin.readline().split()))
    res.append(vector_low)


for i in range(0, len(res) - 1):
    print(res[i])
        
    
    
