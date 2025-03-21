#N = 현재위치
#K = 탐색위치
#현재 위치가 X 일 때 1초 후 위치는 X+1, X-1, 2X 중 하나
#K를 찾는 최단 시간
from collections import deque
N, K = map(int,input().split())
visited = [0 for _ in range(100001)]
temp_q = deque()
next_q = deque()
next_q.append(N)
visited[N] = 1
T = 0
while next_q:
    temp_q = next_q.copy()
    next_q.clear()
    while temp_q:
        x = temp_q.popleft()
        if x == K:
            print(T)
            next_q.clear()
            break
        for dx in [1,-1,x]:
            nx = x + dx
            if 0<=nx<=100000:
                if visited[nx] == 0:
                    visited[nx] = 1
                    next_q.append(nx)
    T += 1