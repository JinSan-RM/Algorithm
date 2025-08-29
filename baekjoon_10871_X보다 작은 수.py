import sys
N, X = sys.stdin.readline().split()
A = sys.stdin.readline().split()

res = []

for i in A:
    if int(X) > int(i):
        print(i, end=' ')
