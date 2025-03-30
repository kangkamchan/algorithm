#입력
#N, D = 지름길수, 도로길이
#s, e, w = 시작, 끝, 가중치
import sys
input = sys.stdin.readline
import heapq
N, D = map(int,input().strip().split())
graph = [[] for i in range(10001)]
for _ in range(N):
    s, e, w = map(int,input().strip().split())
    if w < e - s and e <= D:
        graph[s].append([w,e])
distances = [1e9 for _ in range(10002)]
q = []
distances[0] = 0
heapq.heappush(q,[distances[0],0])
while q:
    distance, node = heapq.heappop(q)
    if node > D:
        continue
    if distance > distances[node]:
        continue
    print(distance, node)
    appended = False
    if len(graph[node])>0:
        for weight, next in graph[node]:
            if next > D:
                continue
            if distances[next] > distance + weight:
                distances[next] = distance + weight
                heapq.heappush(q,[distances[next],next])
                appended = True
    if distances[node+1] > distance + 1:
        distances[node+1] = distance + 1
        heapq.heappush(q,[distances[node]+1,node+1])
print(distances[D])