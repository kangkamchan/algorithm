#top-down i번째칸 => max(i+1번째칸, i+2번째칸) => 마지막에 N번째칸 넘어가면 폐기
#bottom-up N에서 시작 => max(N-1,N-2)
#맨마지막칸 무조건 밟아야함
import sys
input = sys.stdin.readline
N = int(input())
stairs = [0]+[int(input()) for _ in range(N)]
#top-down 
#dp[i][0] i번째칸 밟음 연속1번 => stair[i]+max(recur(i+1),recur(i+2))
#dp[i][1] i번째칸 밟음 연속2번 => recur(i+2)
dp = [[-1,-1] for _ in range(N+1)]
def recursion(i,j):
  if i >= N+1:
    return 0
  if dp[i][j] != -1:
    return dp[i][j]
  if i == 0:
    dp[i][j] = max(recursion(i+1,0),recursion(i+2,0))
    return dp[i][j]
  if j == 0:
    dp[i][j] = stairs[i] + max(recursion(i+1,1),recursion(i+2,0))
    return dp[i][j]
  if j == 1:
    if i == N-1:
      return 0
    dp[i][j] = stairs[i] + recursion(i+2,0)
    return dp[i][j]
print(recursion(0,0))