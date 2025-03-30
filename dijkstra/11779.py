#입력값
#n = 도시의수
#m = 경로의수
#s, e, w = 각 경로의 출발, 도착, 비용
#graph = [], graph[i] = [[비용, 도착지]] i 에서 갈 수 있는 경로 리스트
#start, end = 출발도시, 도착도시
#출발도시에서 도착도시로 가는데 최소 비용, 경로에 포함된 도시 수, 방문 도시들을 출력
import sys
input = sys.stdin.readline
import heapq
n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int,input().strip().split())
    graph[s].append([e,w])
start, end = map(int,input().strip().split())
distances = [1e9 for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
q = []
distances[start] = 0
heapq.heappush(q,[distances[start],start])
while q:
    distance, node = heapq.heappop(q)
    if distance > distances[node]:
        continue
    for next, weight in graph[node]:
        if distances[next] > distances[node] + weight:
            distances[next] = distances[node] + weight
            parent[next] = node
            heapq.heappush(q,[distances[next], next])
node = end
route = []
while True:
    route.append(node)
    if node == start:
        break
    node = parent[node]
print(distances[end])
print(len(route))
print(*route.reverse())
