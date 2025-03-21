#입력
#Y, X = y축, x축
#map = [] Y*X 2차원 배열
#1은 이동가능 0은 이동 불가
#1,1에서 N,M 이동할 때 최소 칸 수 인접한 칸으로만 이동 가능
import sys
sys.setrecursionlimit = 1000000000
from collections import deque
Y, X = map(int,input().split())
map = [list(map(int,list(input().strip()))) for _ in range(Y)]
visited = [[0 for _ in range(X)] for _ in range(Y)]
distance = [[1 for _ in range(X)] for _ in range(Y)]
q = deque()
answer = 0
q.append([0,0])
def bfs():        
    y,x = q.popleft()
    if y == Y-1 and x == X-1:
        print(distance[y][x])
        return
    for dy,dx in [[1,0],[0,1],[-1,0],[0,-1]]:
        ey,ex = y+dy,x+dx
        if 0<=ey<Y and 0<=ex<X:
            if map[ey][ex] == 1:
                if visited[ey][ex] == 0:
                    visited[ey][ex] = 1
                    q.append([ey,ex])
                    distance[ey][ex] = distance[y][x]+1
    bfs()
bfs()