import sys
from collections import deque
sys.stdin = open('input.txt')
F, S, G, U, D = map(int, input().split())
visited = [[False] for _ in range(F + 1)]
 # 가지치기 필요


queue = deque([S])
visited[S] = True
count = 0
while queue:
    for _ in range(len(queue)):
        current = queue.popleft()
        if current == G:
            print(count)
            exit()
        if current + U <= F and not visited[current + U]:
            queue.append(current + U)
            visited[current + U] = True

        if current - D >= 1 and not visited[current + D]:
            queue.append(current - D)
            visited[current - D] = True
    count += 1

print("use the stairs")