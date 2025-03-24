#입력
#N, M, X = 노드수, 간선수, 목적지
#start, end, time = 간선의 시작, 끝, 시간 M번
#graph = [] graph[i] = [[시간,j]] i에서 갈 수 있는 간선, 시간 리스트
#간선은 단방향
#모든 노드에서 최단거리로 목적지로 갔다가 제자리로 돌아와야함
#가장 시간이 오래 걸리는 노드의 시간을 출력

import sys
input = sys.stdin.readline
import heapq
N, M, X = map(int,input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int,input().strip().split())
    graph[start].append([time,end])
def move_from_i_to_j(i,j,N,graph):
    time = [1e9 for _ in range(N+1)]
    time[i] = 0
    q = []
    heapq.heappush(q,[time[i],i])
    while q:
        weight, node = heapq.heappop(q)
        if node == j:
            return weight
        for next_time, next in graph[node]:
            if time[next] > time[node] + next_time:
                time[next] = time[node] + next_time
                heapq.heappush(q,[time[next],next])
answer = 0
for i in range(1,N+1):
    answer = max(answer,move_from_i_to_j(i,X,N,graph)+move_from_i_to_j(X,i,N,graph))
print(answer)