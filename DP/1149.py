#RGB거리
#N 개의 집이 있음, RGB 색상 중 하나로 집을 색칠, 색깔별 비용이 집마다 주어짐
#조건
#1번집의 색 != 2번집의 색
#N번집의 색 != N-1번집의 색
#i(2<=i<=N-1)번 집의 색 != i-1, i+1 번집의 색
#즉, 연속해서 같은 색의 집이 나오면 안됨

N = int(input())
RGB = [list(map(int,input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
dp[0] = RGB[0]
for i in range(1,N):
  for j in range(3):
    dp[i][j] = RGB[i][j] + min(dp[i-1][j-1],dp[i-1][j-2])
    # if j == 0:
    #   dp[i][j] = RGB[i][j] + max(dp[i-1][1],dp[i-1][2])
    # if j == 1:
    #   dp[i][j] = RGB[i][j] + max(dp[i-1][2],dp[i-1][0])
    # if j == 2:
    #   dp[i][j] = RGB[i][j] + max(dp[i-1][0],dp[i-1][1])
print(min(dp[N-1]))