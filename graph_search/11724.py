#입력
#N, M = 정점의 개수, 간선의 개수
#graph = [] graph[i] = i와 연결된 정점 리스트
#그래프 안의 연결요소의 수를 출력
#연결요소 : 서로 연결되어있는 정점 집합
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int,input().strip().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(graph,N):
    visited = [0 for _ in range(N+1)]
    count = 0
    for i in range(1,N+1):
        if visited[i] == 0:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                temp_node = q.popleft()
                next_nodes = graph[temp_node]
                for next_node in next_nodes:
                    if visited[next_node] == 0:
                        q.append(next_node)
                        visited[next_node] = 1
            count += 1
    return count
print(bfs(graph,N))