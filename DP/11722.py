#가장 긴 감소하는 부분수열
N = int(input())
A = list(map(int,input().split()))
dp = [1 for _ in range(N)]
for i in range(N):
  for j in range(i):
    if A[j] > A[i]:
      dp[i] = max(dp[i],dp[j]+1)
print(dp)