#입력값
#V, E = 정점의 개수, 간선의 개수
#K = 시작 정점의 번호
#graph = [] grapn[i] = i번째 노드의 [[다음노드,가중치],[],,,]
#첫번째 줄부터 V번째 줄까지 시작노드부터 각 노드까지 최단거리를 출력
import sys
import heapq
input = sys.stdin.readline
V, E = map(int,input().strip().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().strip().split())
    graph[u].append([v,w])
distance = [1e9 for _ in range(V+1)]
q = []
heapq.heappush(q,[0,K])
distance[K] = 0
while q:
    weight, node = heapq.heappop(q)
    for next, next_weight in graph[node]:
        if distance[node] + next_weight < distance[next]:
             distance[next] = distance[node] + next_weight
             heapq.heappush(q,[distance[next],next])

for i in range(1,V+1):
    if distance[i] == 1e9:
          print("INF")
    else:
         print(distance[i])