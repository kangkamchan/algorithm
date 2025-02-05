#입력 N, K = 물건개수, 최대무게
#W_i, V_i = 각 물건의 무게, 가치
#최대무게를 만족하면서 가치합의 최대값 출력
#items = []
#dp = [[무게],[무게의 가치]]
#파라미터 idx, 무게
#탈출조건 idx == N 이면 return 0, 무게가 K 보다 크면 return -999999, dp[idx] =! -1 이면 return dp[idx]
#dp[idx][weight] = max(물건넣음,물건안넣음)

import sys
input = sys.stdin.readline

def recursion(idx, w):
  if w > K:
    return -999999
  if idx == N:
    return 0
  if dp[idx][w] != -1:
    return dp[idx][w]
  dp[idx][w] = max(recursion(idx+1,w),recursion(idx+1,w+items[idx][0])+items[idx][1])
  return dp[idx][w]
N, K = map(int,input().split())
items = []
for i in range(N):
  w, v = map(int,input().split())
  items.append([w,v])
dp = [[-1 for _ in range(100001)] for _ in range(N)]
answer = recursion(0,0)
print(answer)