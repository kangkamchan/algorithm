#동전2
#n = 동전 개수
#k = 가치
#coins = [] n개의 동전의 가치
#가치의 합이 k가 되는 동전의 수의 최솟값을 출력
#같은 가치 동전을 여러번 사용할 수 있음
#n = 3, k = 15, coins = [1,5,12] 일 때
#일반 재귀
import sys
sys.setrecursionlimit(10000000)
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
# answer = 100000000
# call_cnt = 0
# def recursion(count,sum):
#     global n, k, answer, call_cnt
#     call_cnt += 1
#     if sum == k:
#         answer = min(answer,count)
#         return 
#     if sum > k:
#         return
#     for j in range(n):
#         recursion(count+1,sum+coins[j])
# recursion(0,0)
# print(call_cnt)
# print(answer)

#DP - memoization
#dp = []  dp[i] 는 가치가 i인 동전의 수 최솟값
#n = 2, k = 7, coins = [1,5]
#dp = [0 0 0 0 0 0 0 0]
#recursion(k)
#k 를 만드는 동전의 수 최솟값 출력
#return min(1+recursion(k-1),1+recursion(k-5))
#7

# dp = [9999999 for _ in range(100001)]
# for coin in coins:
#     dp[coin] = 1
# dp_call_cnt = 0
# def recursion(k):
#     global dp_call_cnt
#     dp_call_cnt+=1
#     if k <= 0:
#         return 9999999
#     if dp[k] != 9999999:
#         return dp[k]
#     dp[k] = min([1+recursion(k-coin) for coin in coins])
#     return dp[k]
# answer = recursion(k)
# print(answer if answer < 9999999 else -1)

#DP - tabulation
dp = [9999999 for _ in range(100001)]
for coin in coins:
    if coin > k:
        continue
    dp[coin] = 1
    for i in range(coin+1,k+1):
        dp[i] = min(dp[i],1+dp[i-coin])
answer = dp[k]
if answer == 9999999:
    print(-1)
else:
    print(answer)