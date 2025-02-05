#입력 n = 정수 삼각형 높이
#n 줄, 각 줄마다 n개의 숫자 주어짐
#맨 위에서부터 바로 오른쪽 또는 왼쪽 아래에 있는 수 한개만 선택하며 내려갈 때 최댓값
#dp = [[0 for _ in range(i)] for i in range(501)]
#dp[i][j] =>1층부터 i층의 j번째 까지 더한 값 저장
#재귀함수 정의
#입력값 floor=>현재 몇층인지, idx=>현재 층의 인덱스, sum=>현재까지 합
#dp[floor][idx] != 0 => dp[floor][idx] = max()
#0이면 바로저장
#floor += 1
#sum += 왼쪽값 또는 오른쪽값, 왼쪽값 idx 오른쪽값 idx+1 => 왼쪽,오른쪽 각각 재귀함수 총 2번 호출
#탈출조건 floor > n
import sys
input = sys.stdin.readline
n = int(input())
triangle = [0]
for _ in range(n):
  triangle.append(list(map(int,input().split())))
dp = [[0 for _ in range(i)] for i in range(n+1)]
def max_sum(floor, idx, sum):
  if idx < 0 or idx >= floor:
    return -999999
  if dp[floor][idx] != 0:
    return dp[floor][idx]
# print(dp)
# print(triangle)
for i in range(n-1,0,-1):
  for j in range(i):
    triangle[i][j] = max(triangle[i][j]+triangle[i+1][j],triangle[i][j]+triangle[i+1][j+1])
print(triangle)

