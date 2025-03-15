#합분해
#0부터 N까지 정수 K개를 더해 N이 되는 경우의 수를 1000000000으로 나눈 값 출력
#중복 가능, 숫자 순서가 다른면 다른 경우(1+2 와 2+1은 다른 경우)
#dp[n][k] = n, k 일 때 경우의 수
#dp[0][?] = 1
#dp[i][j] = dp[i-1][j] + dp[i][j-1]
N, K = map(int,input().split())
dp = [[1 if j == 1 or i == 0 else 0 for j in range(K+1)] for i in range(N+1)]
for i in range(1,N+1):
    for j in range(2,K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[N][K])