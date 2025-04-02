#입력
#N, M = 세로, 가로 칸수
#graph = [[]], graph[i][j] = 현재상태, 0바다 1~10 빙산높이
#빙산은 1년마다 상하좌우 인접한 바다 칸 수만큼 줄어듬
#빙산이 2조각 이상으로 분리되는 최소 년수를 출력

import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().strip().split())
graph = [list(map(int,input().strip().split())) for _ in range(N)]
move = [[1,0],[0,1],[-1,0],[0,-1]]
#1,1 부터 순회
#1 이상이면 조각수 1 증가 bfs로 연결된 1이상인 부분 방문처리, 감소할 숫자 저장
#그래프 숫자 감소 처리 후 년 카운트 1 증가
#다시 1,1부터 순회
#조각 수가 2 이상이면 루프 끝내고 출력
def iceburg():
    global N, M
    year = 0
    while True:
        count = 0
        visited = [[0 for _ in range(M)] for _ in range(N)]
        melt_count = [[0 for _ in range(M)] for _ in range(N)]
        print(year)
        for row in graph:
            print(row)
        for i in range(1,N-1):
            for j in range(1,M-1):
                if visited[i][j] == 1 or graph[i][j] == 0:
                    continue
                if graph[i][j] >= 1:
                    count += 1
                    if count >= 2:
                        return year
                    q = deque()
                    q.append([i,j])
                    visited[i][j] = 1
                    while q:
                        y, x = q.popleft()
                        for dy, dx in move:
                            ny, nx = y + dy, x + dx
                            if 0<=ny<N and 0<=nx<M:
                                if graph[ny][nx] == 0:
                                    melt_count[y][x] += 1
                                    continue
                                if visited[ny][nx] == 0:
                                    visited[ny][nx] = 1
                                    q.append([ny,nx])
        if count == 0:
            return 0
        for i in range(1,N-1):
            for j in range(1,M-1):
                graph[i][j] = max(0,graph[i][j] - melt_count[i][j])
        year += 1
print(iceburg())