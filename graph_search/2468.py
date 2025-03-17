#N = 그래프 크기
#graph = N * N 리스트, 원소는 해당위치의 높이
#비의 양에 따라 특정 높이 이하의 지점이 모두 물에 잠김, 물에 잠기지 않은 구역의 수의 최댓값 출력
#안전구역 = 물에 잠기지 않은 구역이 상하좌우로 인접한 경우
#rain = 비의 양 1부터 증가시킴
#answer = 출력할 최대 높이
import sys
input = sys.stdin.readline
from collections import deque
N = int(input().strip())
graph = [list(map(int,input().strip().split())) for _ in range(N)]
move = [[1,0],[0,1],[-1,0],[0,-1]]
rain = 1
answer = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(N):
            if graph[y][x] > rain and visited[y][x] == 0:
                q = deque()
                q.append([y,x])
                visited[y][x] = 1
                count += 1
                while q:
                    ty,tx = q.popleft()
                    for dy,dx in move:
                        ny,nx = ty+dy,tx+dx
                        if 0<=ny<N and 0<=nx<N:
                            if visited[ny][nx] == 0 and graph[ny][nx] > rain:
                                q.append([ny,nx])
                                visited[ny][nx] = 1
    if count <= 0:
        break
    answer = max(count,answer)
    rain += 1
print(answer)