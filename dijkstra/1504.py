#입력
#N, E = 노드수, 간선수
#graph = [] grpah[i] = [[j,w]] i와 이어진 노드와 가중치 리스트
#a, b, c = a 정점 에서 b정점 가는 가중치 c 총 E개 주어짐
#v_1, v_2 = 반드시 거쳐야하는 2개의 정점
#1번 정점에서 N번 정점으로 가는데 반드시 2개의 정점을 지나는 최단거리 출력
#경로가 없으면 -1 출력
#1에서 v_1, v_2 가는 최단거리 구하기 d1, d2
#v1에서 v2, v1에서 N 가는 최단거리 구하기 d3, d4
#v2에서 N가는 최단거리 구하기 d5
#d1+d3+d5 와 d2+d3+d4 중 작은값 출력
import sys
import heapq
input = sys.stdin.readline
N, E = map(int,input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int,input().strip().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v_1, v_2 = map(int,input().strip().split())
def dijkstra(i,j,N,graph):
    distances = [1e9 for _ in range(N+1)]
    distances[i] = 0
    queue = []
    heapq.heappush(queue,[distances[i],i])
    while queue:
        weight, node = heapq.heappop(queue)
        if node == j:
            return weight
        for next, next_weight in graph[node]:
            if distances[next] > distances[node] + next_weight:
                distances[next] = distances[node] + next_weight
                heapq.heappush(queue,[distances[next],next])
    return 1e9

d1 = dijkstra(1,v_1,N,graph)
d2 = dijkstra(1,v_2,N,graph)
d3 = dijkstra(v_1,v_2,N,graph)
d4 = dijkstra(v_1,N,N,graph)
d5 = dijkstra(v_2,N,N,graph)
answer = min(d1+d3+d5,d2+d3+d4)
if answer >= 1e9:
    print(-1)
else:
    print(answer)