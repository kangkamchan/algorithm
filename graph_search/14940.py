#입력
#n = 지도세로크기, m = 지도가로크기
#map = [] 2차원 배열, 0 갈수없음 / 1 갈수있음 / 2 목표
#distances = [] 2차원 배열, 각 위치에서 목표까지 갈 수 있는 최단거리
#bfs 정의
#y, x, map, distances 입력
#q에 y, x append
#visited = []
#while q
#ty, tx = q.popleft
#map[ty][tx] 가 2이면 distances[y][x] = min(distance,distances[y][x])
#상하좌우 이동 ny, nx
#범위 확인
#방문 확인
#방문 처리
import sys
input = sys.stdin.readline
from collections import deque
move = [[1,0],[0,1],[-1,0],[0,-1]]
n, m = map(int,input().strip().split())
graph = [list(map(int,input().strip().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
destination = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            destination.append(i)
            destination.append(j)
            destination.append(0)
            continue
        if graph[i][j] == 0:
            visited[i][j] = 0
q = deque()
q.append(destination)
visited[destination[0]][destination[1]] = 0
while q:
    ty, tx, td = q.popleft()
    for dy, dx in move:
        ny, nx, nd = ty+dy, tx+dx, td+1
        if 0<=ny<n and 0<=nx<m:
            if visited[ny][nx] == -1:
                if graph[ny][nx] != 0:
                    visited[ny][nx] = nd
                    q.append([ny,nx,nd])
for row in visited:
    print(*row)


def bfs(y,x,graph,distances):
    global n, m
    if graph[y][x] == 0:
        distances[y][x] = 0
        return
    q = deque()
    q.append([y,x,0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        ty, tx, td = q.popleft()
        if graph[ty][tx] == 2:
            distances[y][x] = min(td, distances[y][x])
            break
        for dy, dx in move:
            ny, nx, nd = ty+dy, tx+dx, td+1
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0 and graph[ny][nx] != 0:
                    visited[ny][nx] = 1
                    q.append([ny,nx,nd])