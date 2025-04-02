#입력
#N, M = 노드, 간선(양방향) 수
#a, b, c = a 와 b 사이 가중치 c 총 M번
import sys
input = sys.stdin.readline
import heapq
N, M = map(int,input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int,input().strip().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
distances = [1e9 for _ in range(N+1)]
distances[1] = 0
q = []
heapq.heappush(q, [distances[1],1])
while q:
    distance, node = heapq.heappop(q)
    if distance > distances[node]:
        continue
    for next, weight in graph[node]:
        if distances[next] > distances[node] + weight:
            distances[next] = distances[node] + weight
            heapq.heappush(q,[distances[next],next])
print(distances[N])
