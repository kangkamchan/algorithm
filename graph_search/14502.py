# 입력 N, M = 그래프 크기
# graph = [] 2차원 배열, 0은 빈칸 1은 벽 2는 바이러스
# 바이러스는 상하좌우 인접한 칸에 퍼질 수 있음
# 벽을 3개 추가했을 때 안전영역의 최댓값
from collections import deque
import copy
import sys
input = sys.stdin.readline
move = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs(M,N,graph,visited,virus_array,safe_count):
    q = deque(virus_array)
    count = safe_count
    while q:
        ty, tx = q.popleft()
        for dy, dx in move:
            ny, nx = dy+ty, dx+tx
            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx] == 0:
                    if graph[ny][nx] == 0:
                        visited[ny][nx] = 1
                        graph[ny][nx] = 2
                        count -= 1
                        q.append([ny,nx])
    return count
def find(M,N,graph,visited,virus_array,safe_array):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                visited[i][j] = 1
                virus_array.append([i,j])
            if graph[i][j] == 0:
                safe_array.append([i,j])
def count_safe(graph):
    count = 0
    for row in graph:
        for ele in row:
            if ele == 0:
                count +=1
    return count
N, M = map(int,input().strip().split())
graph = [list(map(int,input().strip().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
virus_array = []
safe_array = []
find(M,N,graph,visited,virus_array,safe_array)
safe_count = len(safe_array)
answer = 0
for i in range(safe_count-2):
    for j in range(i+1,safe_count-1):
        for k in range(j+1,safe_count):
            temp_graph = copy.deepcopy(graph)
            temp_visited = copy.deepcopy(visited)
            temp_graph[safe_array[i][0]][safe_array[i][1]] = 1
            temp_graph[safe_array[j][0]][safe_array[j][1]] = 1
            temp_graph[safe_array[k][0]][safe_array[k][1]] = 1
            answer = max(answer,bfs(M,N,temp_graph,temp_visited,virus_array,safe_count-3))
print(answer)