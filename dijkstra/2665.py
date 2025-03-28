#입력값
#n = 그래프 크기
#graph = [] n * n 2차원 리스트, 1 = 방, 0 = 벽
#0,0에서 시작, 벽을 방으로 바꾸어 n-1,n-1 로 가야하는데 바꾸어야할 벽의 최소 개수
import sys
input = sys.stdin.readline
import heapq
n = int(input().strip())
graph = [list(int(i) for i in input().strip() )for _ in range(n)]
move = [[1,0],[0,1],[-1,0],[0,-1]]
def dijkstra(graph, n):
    distances = [[1e9 for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0
    q = []
    heapq.heappush(q,[distances[0][0], 0, 0])
    while q:
        weight, y, x = heapq.heappop(q)
        if weight > distances[y][x]:
            continue
        for dy, dx in move:
            ny, nx  = y + dy, x + dx
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx] == 1:
                    if distances[ny][nx] > weight:
                        distances[ny][nx] = weight
                        heapq.heappush(q,[distances[ny][nx],ny,nx])
                else:
                    if distances[ny][nx] > distances[y][x] + 1:
                        distances[ny][nx] = distances[y][x] + 1
                        heapq.heappush(q,[distances[ny][nx],ny,nx])
    return distances[n-1][n-1]
print(dijkstra(graph,n))
