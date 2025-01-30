#T = 횟수
#1<= k = 층 n = 호 <= 14


dp = [[0 for _ in range(15)] for _ in range(15)]
dp[0] = [i for i in range(15)]
dp[1][1] = 1
for i in range(1,15):
  for j in range(1,15):
    dp[i][j] = dp[i][j-1] + dp[i-1][j]

T = int(input())
arr = []
for i in range(T):
  k = int(input())
  n = int(input())
  arr.append([k,n])
for ele in arr:
  print(dp[ele[0]][ele[1]])