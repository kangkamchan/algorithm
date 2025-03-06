#입력
#N = 정점의 개수, M = 간선의 개수, V = 탐색 시작 번호
#graph = [], graph[i] = i번 정점과 연결되어있는 정점 리스트
#첫째줄에 DFS 수행결과 둘째줄에 BFS 수행결과 출력
from collections import deque
N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
for i in range(N+1):
    graph[i].sort()
visited = [0 for _ in range(N+1)]
#DFS
DFS = []
def dfs(i):
    visited[i] = 1
    DFS.append(i)
    for next in graph[i]:
        if visited[next] == 0:
            dfs(next)
dfs(V)
print(*DFS)

#BFS
visited = [0 for _ in range(N+1)]
q = deque()
BFS = []
q.append(V)
visited[V] = 1
while q:
    node = q.popleft()
    BFS.append(node)
    for next in graph[node]:
        if visited[next] == 0:
            q.append(next)
            visited[next] = 1
print(*BFS)