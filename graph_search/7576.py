#M = 가로, N = 세로
#graph = [] 0 안익은거 1 익은거 -1 없는곳
#익은거 상하좌우 인접한 곳은 다음날 익음
#모두 익는데 걸리는 최소 일수 출력
#처음부터 모두 익어있으면0, 모두익을 경우의수가 없으면 -1
#day = 0 카운트
#total = 달성해야할개수
#now = 현재개수
#visited = [] 방문여부
#temp_q = [] 이번 반복에 확인할 위치
#next_q = [] 다음 반복에 확인할 위치
#1 0 0
#0 0 0
#0 0 1
#초기화 : 모든 위치 확인해서 1 인 것 next_q에 append now+=1, 0 이나 1인 것 있으면 total+=1
#next_q에 확인할 게 있으면
#temp_q에 next_q 복사, next_q 요소 모두 삭제
#day+=1
#temp_q 확인 
#graph 1로 변경, now += 1
#방문 안했고 graph 0이면 방문처리하고 next_q에 append
#모든 반복 종료 후 now == total 이면 day 출력, 아니면 -1 출력
import sys
input = sys.stdin.readline
from collections import deque
import copy
M, N = map(int,input().strip().split())
graph = [list(map(int,input().strip().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dif = [[1,0],[0,1],[-1,0],[0,-1]]
day = 0
total = 0
now = 0
temp_q = deque()
next_q = deque()
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            next_q.append([y,x])
            visited[y][x] = 1
            now += 1
            total += 1
            continue
        if graph[y][x] == 0:
            total += 1
print("initial",next_q,now,total)
while next_q:
    print(day, "graph")
    print(graph)
    print(day, "temp_q")
    print(next_q)
    if now == total:
        break
    temp_q = copy.deepcopy(next_q)
    next_q.clear()
    while temp_q:
        temp_y, temp_x = temp_q.popleft()
        for dy, dx in dif:
            next_y, next_x = temp_y + dy, temp_x + dx
            if 0<=next_y<N and 0<=next_x<M:
                if visited[next_y][next_x] == 0 and graph[next_y][next_x] == 0:
                    visited[next_y][next_x] = 1
                    graph[next_y][next_x] = 1
                    now+=1
                    next_q.append([next_y,next_x])
        print(day, "next_q")
        print(next_q)
    day += 1
print("final")
print(graph)
print(total)
print(now)
if now == total:
    print(day)
else:
    print(-1)