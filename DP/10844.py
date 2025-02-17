#쉬운 계단수
#입력 N = 자릿수
#출력 N자리 계단수의 개수
N = int(input())
def recursion(i,n):
  if i == -1 or i == 10:
    return 0
  if n == N:
    return 1
  if dp[i][n] != 0:
    return dp[i][n]
  dp[i][n] = recursion(i-1,n+1) + recursion(i+1,n+1)
  return dp[i][n]
dp = [[0 for _ in range(N)] for _ in range(10)]
answer = 0
for i in range(1,10):
  answer += recursion(i,1)
print(answer%1000000000)