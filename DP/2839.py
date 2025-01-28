#N = 무게
#3 과 5를 조합해서 정확히 N 을 만들 수 있는 최소 개수 출력
import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)
#완전탐색
# N = int(input())
# answer = 30000
# for i in range(1668):
#   if i*3 > N:
#     break
#   for j in range(1001):
#     if i*3 + j*5 > N:
#       break
#     if i*3 + j*5 == N:
#       answer = min(answer,i+j)
# if answer == 30000:
#   print(-1)
# else:
#   print(answer)
#DP
#
#dp = [2000 for _ in range(5001)] => dp[i] 는 N = i 일 때 결과
#i 일때 결과는 i - 3 일 때 또는 i - 5 일 때 결과가 있다면 둘중 작은거 + 1 개(3아니면 5 하나만 추가하면됨) 
#초기 값 N이 3 또는 5이면 1개이므로 dp[3] = 1 dp[5] = 1 으로 설정
#i - 3 일때 또는 i - 5 일때 결과가 없다면 i 일때도 불가능
# N = int(input())
# dp = [2000 for _ in range(5001)]
# dp[3] = 1
# dp[5] = 1
# for i in range(6,N+1):
#   if dp[i-3] < 2000 or dp[i-5] < 2000:
#     dp[i] = min(dp[i-3],dp[i-5]) + 1
# answer = dp[N]
# print(answer)

def recursion(i):
  if N < 6:
    return
  if i == N + 1:
    return
  #이전결과가 있다면
  if dp[i-3] < 2000 or dp[i-5] < 2000:
    dp[i] = min(dp[i-3],dp[i-5]) + 1
  recursion(i+1)
N = int(input())
dp = [2000 for _ in range(5001)]
dp[3] = 1
dp[5] = 1
recursion(6)
answer = dp[N] if dp[N] < 2000 else -1
print(answer)