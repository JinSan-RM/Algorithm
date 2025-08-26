import sys
X = int(input())
N = int(input())

res = 0

for i in range(N):
    
    p = sys.stdin.readline().split()
    
    res += ( int(p[0]) * int(p[1]) )

if res == X:
    print("Yes")
else:
    print("No")
