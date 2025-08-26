from collections import deque
com = int(input())  # 컴퓨터 수 (정점)
N = int(input())    # 컴퓨터간의 연결수 (간선)
graph = [[] for _ in range(com+1)]
visited = [False for _ in range(com+1)]


for _ in range(N):  # 간선정보 입력
    s, e = map(int, input().split())
    graph[s].append(e)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True) - 1)





n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시
Q=deque([1])
while Q:
    c=Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
print(sum(visited)-1)