#입력값
#N = 현재위치, K = 목표위치
#현재위치가 X라면
#걷기 = 1초 후 X-1 또는 X+1로 이동
#순간이동 = 0초 후 2X로 이동
#목표위치로 갈 수 있는 최단시간 출력
import heapq
import sys
input = sys.stdin.readline
N, K = map(int,input().strip().split())
time = [1e9 for _ in range(100001)]
time[N] = 0
q = []
heapq.heappush(q,[0,N])
count = 0
while q:
    weight, x = heapq.heappop(q)
    print(weight, x)
    if x == K:
        print(time[x])
        break
    for nw, nx in [[0,2*x], [1,x-1], [1,x+1]]:
        if 0<=nx<=100000:
            if time[nx] > time[x] + nw:
                time[nx] = time[x] + nw
                heapq.heappush(q,[time[nx],nx])