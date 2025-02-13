#입력 M = 지도의 행 수, N = 지도의 열 수
#map = M X N 각 칸의 높이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
M, N = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
def recursion(i,j,height):
  if i < 0 or i >= M or j < 0 or j >= N:
    return 0
  if height >= map[i][j]:
    return 0
  if i == 0 and j == 0:
    return 1
  if dp[i][j] != -1:
    return dp[i][j]
  temp_height = map[i][j]
  dp[i][j] = recursion(i-1,j,temp_height) + recursion(i,j-1,temp_height) + recursion(i+1,j,temp_height) + recursion(i,j+1,temp_height)
  return dp[i][j]
print(recursion(M-1,N-1,0))