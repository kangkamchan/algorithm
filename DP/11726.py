# 2 X n 크기의 직사각형을 1X2, 2X1 타일로 채우는 방법의 수
# 입력값 n
# n번째 만드는 경우의수
# 세로 하나짜리 + n - 1 칸
# 가로 2개 + n - 2칸
import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)