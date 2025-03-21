#단지번호붙이기
#입력
#N = 정사각형크기
#graph = [] 2차원 배열, 1: 집, 0: 집없음
#단지 : 서로 다른 집끼리 상하좌우로 연결되어있는것
#단지의 개수, 단지의 크기를 오름차순으로 출력
#그래프 모든 요소를 탐색
#각 요소별로 카운트 변수에 저장
#방문하지 않았고 집이면 방문처리 카운트증가
from collections import deque
N = int(input())
graph = [list(map(int,list(input()))) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
complexes = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            if visited[i][j] == 0:
                visited[i][j] = 1
                q = deque()
                q.append([i,j])
                count = 1
                while q:
                    ei, ej = q.popleft()
                    for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                        ni, nj = ei+di, ej+dj
                        if 0<=ni<N and 0<=nj<N:
                            if graph[ni][nj] == 1:
                                if visited[ni][nj] == 0:
                                    visited[ni][nj] = 1
                                    count += 1
                                    q.append([ni,nj])
                complexes.append(count)   
print(len(complexes))
for complex in sorted(complexes):
    print(complex)