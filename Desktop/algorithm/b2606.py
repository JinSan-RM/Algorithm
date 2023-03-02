com = int(input())  # 컴퓨터 수 (정점)
N = int(input())    # 컴퓨터간의 연결수 (간선)
graph = [[] for _ in range(com+1)]
visited = [False for _ in range(com+1)]
cnt = -1

for _ in range(N):  # 간선정보 입력
    s, e = map(int, input().split())
    graph[s].append(e)

def dfs(graph, v, visited):gi
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(cnt)