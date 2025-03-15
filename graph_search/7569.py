#입력
#M, N, H = 상자의 가로, 세로, 높이
#graph = [] M * N * H 3차원 배열, 1 익은 토마토 0 익지않은 토마토 -1 토마토 없음
#1일이 지나면 익은 토마토 주위 상하좌우위아래 6개의 방향에 있는 토마토가 익는다
#graph의 모든 토마토가 익을 때 까지 걸리는 일 수를 출력, 모두 익지 못하는 경우 -1 출력
import sys
input = sys.stdin.readline
from collections import deque
M, N, H = map(int,input().strip().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
temp = 0
result = 0
q = deque()
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                result += 1
            if graph[i][j][k] == 1:
                result += 1
                temp += 1
                q.append([i,j,k,0])
                visited[i][j][k] = 1
move = [[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
answer = 0
while q:
    tz,ty,tx,td = q.popleft()
    answer = max(answer,td)
    for dz,dy,dx in move:
        nz, ny, nx, nd = tz+dz, ty+dy, tx+dx, td+1
        if 0<=nz<H and 0<=ny<N and 0<=nx<M:
            if visited[nz][ny][nx] == 0 and graph[nz][ny][nx] == 0:
                visited[nz][ny][nx] = 1
                graph[nz][ny][nx] = 1
                temp += 1
                q.append([nz,ny,nx,nd])
if temp == result :
    print(answer)
else :
    print(-1)