# 이모스법 : 장애물이 시작하는 칸에 1, 끝나는 칸 뒤에 -1을 입력 => 각 칸별 입력된 숫자를 모두 더함 => 누적합을 계산 => 각 레인별 장애물 수
# 입력값 : N = 길이(짝수), H = 높이, obstacles = 장애물 높이 배열 석순(시작 0 끝 크기) - 종유석(시작 H  - 1 - 크기 끝 H - 1) 순 
# arr = 장애물 시작 1 끝 -1 작성된 배열 길이 = H
# prefix = 누적합 배열
# N = 6, H - 7
# obstacles = [1, 5, 3, 3, 5, 1]
#   0   0   0  1
#   0   0      -1
#   0   0 0    1
#   0     0    -1
#   0 0   0    1
#     0   0    -1
# 0   0   0    3       
# arr = [3,-1,1,-1,1,-1,1,-3]
# prefix = [3, 2, 4, 3, 4, 3, 3]
# import sys
# input = sys.stdin.readline  
# 이거 한줄 추가한다고 속도가 매우 빨라졌다.........?
import sys
input = sys.stdin.readline 
N, H = map(int, input().split())
obstacles = [int(input()) for _ in range(N)]
arr = [0 for _ in range(H+1)]
for i in range(N):
  if i % 2 == 0:
    arr[0] += 1
    arr[obstacles[i]] -= 1
  else:
    arr[H - obstacles[i]] += 1
    arr[H] -= 1
for i in range(1,H):
  arr[i] += arr[i-1]
arr = arr[:H]
min_val = min(arr)
count = arr.count(min_val)
print(min_val, count)