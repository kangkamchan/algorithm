#입력값
#T = 실행 횟수
#X,Y,K = 가로길이, 세로길이, 배추개수
#x, y = 배추위치 K 번
#graph = [] Y*X 2차원 리스트, 0 : 배추없음, 1 : 배추
def bfs(X,Y,K):
    graph = [[0 for _ in range(X)] for _ in range(Y)]
    visited = [[0 for _ in range(X)] for _ in range(Y)]
    for _ in range(K):
        x, y = map(int,input().split())
        graph[y][x] = 1
    count = 0
    for y in range(Y):
        for x in range(X):
            if graph[y][x] == 1 and visited[y][x] == 0:
                q = deque()
                q.append([y,x])
                count += 1
                while q:
                    ty, tx = q.popleft()
                    for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                        ny, nx = ty+dy, tx+dx
                        if 0<=ny<Y and 0<=nx<X:
                            if graph[ny][nx]==1 and visited[ny][nx]==0:
                                q.append([ny,nx])
                                visited[ny][nx] = 1
    print(count)
from collections import deque
T = int(input())
for _ in range(T):
    X,Y,K = map(int,input().split())
    bfs(X,Y,K)
