import sys
sys.stdin = open('inputb2644.txt')
T = int(input())
from collections import deque

for tc in range(1, T+1):
     N = int(input())
     S, E = list(map(int, input().split()))
     iter = int(input()) #관계
     edge = [[] for  in range(N+1)]


     for i in range(iter):
         parent, child =list(map(int,input().split()))
         edge[parent].append(child)
         edge[child].append(parent)
     print(edge)

    #큐의 반대방향개념, 꼬리물고 올라가기
     def bfs():
          visited = [False]* (N+1)
          to_visits = deque()
          to_visits.append(S)
          cnt = 0

          while to_visits:
              current = to_visits.popleft()
              if not visited[current]:
                  print(current)
                  visited[current] = True
                  if current == E:
                      break
                  for i in (sorted(edge[current],reverse=True)):
                      to_visits.appendleft(i)
                  #스텍에 담을 때 앞쪽에 붙여주기
                  cnt +=1

          # E가 방문처리가 안되있으면 -1 리턴
          if visited[E]:
              print('answer:',cnt)
          else:
              print('answer:',-1)
     bfs()