#입력
#N = 테스트케이스 개수
#I = 체스판 한 변의 길이
#start = [y,x] 현재 칸
#end = [y,x] 이동하려는 칸
#나이트가 start에서 end까지 최소 몇 번 만에 갈 수 있는지 출력
import sys
input = sys.stdin.readline
from collections import deque
move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
def bfs(I, start, end):
    visited = [[0 for _ in range(I)] for _ in range(I)]
    q = deque()
    q.append(start)
    answer = float("inf")
    while q:
        ty, tx, tc = q.popleft()
        if ty == end[0] and tx == end[1]:
            answer = min(answer,tc)
        for dy, dx in move:
            ny, nx, nc = ty + dy, tx + dx, tc + 1
            if 0<=ny<I and 0<=nx<I:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny,nx,nc])
    return answer
N = int(input().strip())
for _ in range(N):
    I = int(input().strip())
    start = list(map(int,input().strip().split()))
    end = list(map(int,input().strip().split()))
    start.append(0)
    print(bfs(I,start,end))
