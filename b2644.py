import sys
sys.stdin = open('input.txt')

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(m+1)]
visited = [False for _ in range(m+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            

#입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

