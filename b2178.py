import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())
a = []

for _ in range(N):
    a.append(list(map(int, input().rstrip())))
row = [-1,1,0,0]
col = [0,0,-1,1]

def bfs(x, y):
    Q = deque()
    Q.append((x,y))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            idx = x + row[i]
            idy = y + col[i]

            if 0 <= idx < N and 0 <= idy < M and a[idx][idy] == 1:
                Q.append((idx, idy))
                a[idx][idy] = a[x][y] + 1

    return a[N - 1][M - 1]
print(bfs(0,0))





