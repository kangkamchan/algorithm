#입력
#N = 그래프크기
#graph = [list(map(int,input().strip().split())) for _ in range(N)]
#graph 각 칸 = 가중치
#0,0 에서 N-1,N-1 까지 가는 최소 비용 출력
#N = 0 입력되면 반복 종료
import heapq
import sys
input = sys.stdin.readline
move = [[1,0],[0,1],[-1,0],[0,-1]]
def dijkstra(graph, N):
    distances = [[1e9 for _ in range(N)] for _ in range(N)]
    distances[0][0] = graph[0][0]
    q = []
    heapq.heappush(q,[distances[0][0],0,0])
    while q:
        distance, y, x = heapq.heappop(q)
        if distance > distances[y][x]:
            continue
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N:
                nw = graph[ny][nx]
                if distances[ny][nx] > distances[y][x] + nw:
                    distances[ny][nx] = distances[y][x] + nw
                    heapq.heappush(q,[distances[ny][nx],ny,nx])
    return distances[N-1][N-1]
count = 0
while True:
    count += 1
    N = int(input().strip())
    if N == 0:
        break
    graph = [list(map(int,input().strip().split())) for _ in range(N)]
    print("Problem ",end="")
    print(count,end="")
    print(": ",end="")
    print(dijkstra(graph, N))
