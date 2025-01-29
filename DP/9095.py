#입력값
#T = 입력횟수
#N = 입력값
#N 을 1, 2, 3의 합으로 나타내는 방법의 수
#dp = [0 for _ in range(11)]
#dp[1] = 1 => 1
#dp[2] = 1 + 1 / 2 => 2
#dp[3] = 1 + 1 + 1 / 1 + 2 / 2 + 1 / 3 => 4
#dp[N] = N일 때 결과 = dp[N-3] + dp[N-2] + dp[N-1]

T = int(input())
dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,11):
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
for i in range(T):
  N = int(input())
  print(dp[N])