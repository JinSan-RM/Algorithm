import sys

N, M = input().split()
N, M = int(N), int(M)

A = []
B = []


for i in range(N):
    element = sys.stdin.readline().split()
    A.append(element)


for i in range(N):  
    element = sys.stdin.readline().split()
    B.append(element)


for i in range(N):
    for j in range(M):
        result = int(A[i][j]) + int(B[i][j])
        print(result, end=' ')
    print() 
