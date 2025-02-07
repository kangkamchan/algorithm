#포도주 시식
#입력값 n : 포도주 수, wine : n 개의 포도주 양 
#연속해서 3잔을 마실 수 없음
#마실 수 있는 양의 최댓값 출력
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n = int(input())
wine = [0]+[int(input()) for _ in range(n)]
#dp = [[안마심,마심1잔째,마심2잔째]] => i번째 잔 안마실경우, 1잔째 마실경우, 2잔째 마실경우
dp = [[-1,-1,-1] for _ in range(n+1)]
def recursion(i,j):
  if i >= n+1:
    return 0
  if dp[i][j] != -1:
    return dp[i][j]
  if j == 0:
    dp[i][j] = max(recursion(i+1,0),recursion(i+1,1))
    return dp[i][j]
  if j == 1:
    dp[i][j] = max(wine[i]+recursion(i+1,0),wine[i]+recursion(i+1,2))
    return dp[i][j]
  if j == 2:
    dp[i][j] = max(wine[i]+recursion(i+2,0),wine[i]+recursion(i+2,1))
    return dp[i][j]
recursion(0,0)
print(max(dp[1]))