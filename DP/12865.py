#입력 N, K = 물건개수, 최대무게
#W_i, V_i = 각 물건의 무게, 가치
#최대무게를 만족하면서 가치합의 최대값 출력
#items = []
#dp[idx][weight] = idx 번째 일 때 무게가 weight 일 때 가치치
#파라미터 idx, 무게
#탈출조건 idx == N 이면 return 0, 무게가 K 보다 크면 return -999999, dp[idx] =! -1 이면 return dp[idx]
#dp[idx][weight] = max(물건넣음,물건안넣음)

import sys
input = sys.stdin.readline
N, K = map(int,input().split())
items = []
for i in range(N):
  w, v = map(int,input().split())
  items.append([w,v])
#top-down DP
# def recursion(idx, w):
#   if w > K:
#     return -999999
#   if idx == N:
#     return 0
#   if dp[idx][w] != -1:
#     return dp[idx][w]
#   dp[idx][w] = max(recursion(idx+1,w),recursion(idx+1,w+items[idx][0])+items[idx][1])
#   return dp[idx][w]
# dp = [[-1 for _ in range(100001)] for _ in range(N)]
# answer = recursion(0,0)
# print(answer)
#bottom-up DP
dp = [[0 for _ in range(K+1)] for _ in range(N)]
dp[0][items[0][0]] = items[0][1]
for i in range(1,N):
  for w in range(K+1):
    if w-items[i][0] < 0:
      dp[i][w] = dp[i-1][w]
    else:
      dp[i][w] = max(items[i][1]+dp[i-1][w-items[i][0]],dp[i-1][w])
print(dp)