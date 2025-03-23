#N = 정점수
#M = 간선수
#i, j, w = 간선 시작, 종료, 가중치 총 M번 입력
#graph = [] graph[i] = [[목적지,가중치]] i에서 갈 수 있는 목적지와 가중치 리스트
#start, end = 출발, 목적지
import sys
input = sys.stdin.readline
import heapq
N = int(input().strip())
M = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j, w = map(int,input().strip().split())
    graph[i].append([j,w])
print(graph)
distance = [1e9 for _ in range(N+1)]
start, end = map(int,input().strip().split())
distance[start] = 0
q = []
heapq.heappush(q,[0,start])
while q:
    weight, node = heapq.heappop(q)
    print(q)
    if node == end:
        print(weight)
        break
    for next, next_w in graph[node]:
        distance[next] = min(distance[next],distance[node]+next_w)
        heapq.heappush(q, [distance[next], next])

    