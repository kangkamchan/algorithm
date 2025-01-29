#입력값
#T = 입력횟수
#N = 입력값
#N 번째 피보나치수를 구할 때 0과 1이 출력되는 횟수를 출력
#dp = [[0,0] for _ in range(41)]
#dp[0] = [1,0]
#dp[1] = [0,1]
#dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
import sys
input = sys.stdin.readline
dp = [[0,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,41):
  dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
T = int(input())
N = [int(input()) for _ in range(T)]
for i in N:
  print(*dp[i])