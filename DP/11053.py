#LIS Longest Increasing Subsequence 가장 긴 증가하는 부분수열
#입력값 N = 입력받을 수열 길이
#A = 수열
#A 에서 가장 긴 증가하는 부분 수열의 길이를 출력
#A = [10,20,10,30,20,50] 일 때
#0 <= i <= N-1
#dp[0] = 1
#i => i-1 ~ 0 j 확인해서 A[j] 가 A[i] 보다 작은 j 중 dp[j] 가 가장 큰 값 + 1 을 dp[i] 에 대입
#없으면 dp[i] = 1
#10 20 10 15 11 25 20 30 40 60 20 50
#1  2  1  2  2  3  3  4  5  6  4  6  
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [1 for _ in range(N)]
for i in range(1,N):
  for j in range(0,i):
    if A[j] < A[i]:
      dp[i] = max(dp[i],dp[j]+1)
print(dp)