#보물섬
#입력 Y = 세로 크기, X = 가로 크기, map = 바다W육지L로 표시된 2차원 list
#상하좌우 이웃한 육지로만 이동이 가능
#육지 사이에 최단거리가 가장 큰 곳에 보물이 숨겨져 있음
#보물이 있는 육지 사이의 최단거리를 출력
import sys
input = sys.stdin.readline
from collections import deque
Y, X = map(int,input().split())
map = [list(input().strip()) for _ in range(Y)]
answer = 0
for y in range(Y):
    for x in range(X):
        if map[y][x] == 'L':
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            distance = [[0 for _ in range(X)] for _ in range(Y)]
            q = deque()
            q.append([y,x])
            visited[y][x] = 1
            while q:
                ey, ex = q.popleft()
                for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ny, nx = ey + dy, ex + dx
                    if 0<=ny<Y and 0<=nx<X:
                        if map[ny][nx] == 'L':
                            if visited[ny][nx] == 0:
                                q.append([ny,nx])
                                visited[ny][nx] = 1
                                distance[ny][nx] = distance[ey][ex] + 1
                                answer = max(answer,distance[ny][nx])
print(answer)