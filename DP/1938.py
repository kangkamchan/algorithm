#입력 N => map 의 크기 (N X N)
#map = N 개 씩 N 줄의 정보
import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999999)
N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]
def recursion(i,j,value):
  if i < 0 or j < 0 or i >= N or j >= N:
    return 0
  if map[i][j] <= value:
    return 0
  if dp[i][j] != -1:
    return dp[i][j]
  dp[i][j] = max(recursion(i-1,j,map[i][j]),recursion(i,j-1,map[i][j]),recursion(i+1,j,map[i][j]),recursion(i,j+1,map[i][j])) + 1
  return dp[i][j]
for i in range(N):
  for j in range(N):
    recursion(i,j,0)
print(max(max(row) for row in dp))