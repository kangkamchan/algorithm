#입력값 N 남은 일수
#T_i, P_i : i일 걸리는 시간, 금액
#schedule = [] 입력받은 시간, 금액
import sys
input = sys.stdin.readline
N = int(input())
# schedule = [[0,0]]
# for i in range(N):
#   a,b = map(int,input().split())
#   schedule.append([a,b])
# 탑다운DP
# def recursion(idx):
#   if idx == N+1:
#     return 0
#   if idx > N+1:
#     return -99999999
#   if dp[idx] != -1:
#     return dp[idx]
#   dp[idx] = max(recursion(idx+1),recursion(idx+schedule[idx][0])+schedule[idx][1])
#   return dp[idx]
# dp = [-1 for _ in range(N+1)]
# print(recursion(1))

# 바텀업 DP
schedule = []
for i in range(N):
  a,b = map(int,input().split())
  schedule.append([a,b])
dp = [0 for _ in range(N+1)]
for i in range(N)[::-1]:
  if schedule[i][0] + i > N:
    dp[i] = dp[i+1]
  dp[i] = max(dp[schedule[i][0]+i]+schedule[i][1],dp[i+1])
print(dp)