#입력
#n, m, r = 지역수, 수색범위, 길의수
#t = 각구역 아이템 수 n개 공백으로 구분
#items[i] = t 구역 i의 아이템수 t
#a, b, l = 연결된지역번호 a와b, 거리 l r회 반복
#graph[i] = [[j,w]] i에 연결된 j, 거리 w
#각 지역 중 수색범위 내 아이템이 최대인 곳의 아이템 개수 출력
import sys
input = sys.stdin.readline
import heapq
n, m , r = map(int,input().strip().split())
items =[0] + list(map(int,input().strip().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int,input().strip().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

def dijkstra(i,n,m):
    distances = [1e9 for _ in range(n+1)]
    distances[i] = 0
    q = []
    heapq.heappush(q,[distances[i],i])
    while q:
        distance, node = heapq.heappop(q)
        if distance > m:
            continue
        for next, weight in graph[node]:
            if distance + weight <= m and distances[next] > distance + weight:
                distances[next] = distance + weight
                heapq.heappush(q,[distances[next],next])
    count = 0
    for i in range(1,n+1):
        if distances[i] <= m:
            count += items[i]
    return count

print(max(dijkstra(i,n,m) for i in range(1,n+1)))