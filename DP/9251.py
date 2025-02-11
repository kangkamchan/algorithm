#입력 문자열 2개
import sys
input = sys.stdin.readline
str1 = input().strip()
str2 = input().strip()
n, m = len(str1),len(str2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
  for j in range(m):
    if str1[i] == str2[j]:
      dp[i+1][j+1] = dp[i][j] + 1
    else:
      dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
print(dp)
print(str1,str2)