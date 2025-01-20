# 입력값 N = 입력받을 개수, arr = 입력받은 기둥정보 배열[[위치, 높이]]
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
# 왼쪽누적합
# 최대높이 현재높이 누적합
# 0        4       4
# 4        6       14
# 6        3       14
# 6        10      42
# 10       4       42
# 10       6       42
# 10       8       42
# 오른쪽누적합
# 최대높이 현재높이 누적합
# 8        8       0
# 8        6       0
# 8        4       0
# 8        10      56
# 왼쪽 누적합 =>  오른쪽 누적합 => 
# => [0,1,3,6]
# (arr[i+1][0]-arr[i][0])*arr[i][1]
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key= lambda x: x[0])
left = 0
left_max_height = 0
left_max_location = 0
for i in range(N):
  if arr[i][1] >= left_max_height:
    left += left_max_height * (arr[i][0] - left_max_location - 1) + arr[i][1]
    left_max_location = arr[i][0]
    left_max_height = arr[i][1]

right = 0
right_max_hight = 0
right_max_location = 0
for i in range(N-1,-1,-1):
  if arr[i][1] > right_max_hight:
    right += right_max_hight * abs(arr[i][0]-right_max_location)
    right_max_location = arr[i][0]
    right_max_hight = arr[i][1]

print(left+right)
