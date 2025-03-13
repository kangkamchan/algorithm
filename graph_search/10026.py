# 입력값
# N = N X N 그리드 크기
# nomal = [] N X N 그리드, R G B 중 하나의 값을 가지는 2차원배열
# special = [] N X N 그리드, R B 중 하나의 값을 가지는 2차원배열
# 적록색약 R 이랑 G 구분 못함
# 영역 = 같은 색으로 이루어진 구역
# 적록색약인 사람이 보는 영역의 개수 아닌 사람이 보는 영역의 개수 
# is_grouped_nomal 영역여부 = [1 영역에 포함됨 0 영역에포함안됨]
# is_grouped_special 영역여부 = [1 영역에 포함됨 0 영역에포함안됨]
# 모든 y, x 을 탐색
# is_grouped 가 0이면
# q = deque()
# 정상 기준칸 색깔 = nomal[y][x]
# 영역 += 1
# q에 [y,x] append
# while q:
#   next_y, next_x = q.popleft()
#   색깔 같으면 영역처리
#   상하좌우 탐색
#       정상범위면 방문처리
#       큐에 append
import sys
input = sys.stdin.readline
from collections import deque
N = int(input().strip())
normal = []
spetial = []
for _ in range(N):
    row = input().strip()
    normal.append(list(row))
    spetial.append(list(row.replace("G","R")))
is_grouped_normal = [[0 for _ in range(N)] for _ in range(N)]
is_grouped_spetial = [[0 for _ in range(N)] for _ in range(N)]
normal_cnt = 0
spetial_cnt = 0
move = [[1,0],[0,1],[-1,0],[0,-1]]
def search(map,y,x,is_grouped):
    cnt = 0
    if is_grouped[y][x] == 0:
        color = map[y][x]
        cnt += 1
        q = deque()
        q.append([y,x])
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[y][x] = 1
        while q:
            temp_y, temp_x = q.popleft()
            if map[temp_y][temp_x] == color:
                is_grouped[temp_y][temp_x] = 1
                for dy,dx in move:
                    next_y, next_x = temp_y + dy, temp_x + dx
                    if 0<=next_y<N and 0<=next_x<N:
                        if visited[next_y][next_x] == 0:
                            if is_grouped[next_y][next_x] == 0:
                                visited[next_y][next_x] = 1
                                q.append([next_y,next_x])
    return cnt
for y in range(N):
    for x in range(N):
        normal_cnt += search(normal,y,x,is_grouped_normal)
        spetial_cnt += search(spetial,y,x,is_grouped_spetial)
print(normal_cnt, spetial_cnt)

