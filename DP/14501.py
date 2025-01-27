#입력값 N 남은 일수
#T_i, P_i : i일 걸리는 시간, 금액
#schedule = [] 입력받은 시간, 금액

def recursion(idx):
  global m
  m += 1
  print(m)
  if idx == N+1:
    return 0
  if idx > N+1:
    return -99999999
  if dp[idx] != -1:
    return dp[idx]
  dp[idx] = max(recursion(idx+1),recursion(idx+schedule[idx][0])+schedule[idx][1])
  return dp[idx]
N = int(input())
schedule = [0]
for i in range(N):
  a,b = map(int,input().split())
  schedule.append([a,b])
dp = [-1 for _ in range(N+1)]
m = 0
print(recursion(1))