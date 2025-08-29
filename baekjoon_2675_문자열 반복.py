import sys
input = sys.stdin.readline

n = int(input())



for i in range(n):
    a = []
    R, S = input().split()
    R = int(R)

    for j in S:
        S = j * R
        a.append(S)
    print(''.join(a))
    
