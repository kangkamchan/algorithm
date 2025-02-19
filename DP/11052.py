#입력
#N = 구매할 카드 수, 1개 ~ N개 들어있는 카드팩의 가격
#cards = [], cards[i] => i개 들어있는 카드팩의 가격
#dp = [0 for _ in range(N+1)]
#N = 4
#cards = 1, 5, 6, 7
#dp[1] = 1
#dp[2] = max(card[2],dp[1]+dp[1])
#dp[3] = max(card[3],dp[2]+dp[1],dp[1]+dp[1]+dp[1]) = max(card[3],dp[2]+dp[1],dp[1]+dp[2])
#dp[4] = max(card[4],dp[3]+dp[1],dp[2]+dp[2],dp[2]+dp[1]+dp[1],dp[1]+dp[1]+dp[1]+dp[1]) = max(card[4],dp[2]+dp[2],dp[1]+dp[3])
#dp[5] = max(card[5],dp[4]+dp[1],dp[3]+dp[2],dp[3]+dp[1]+dp[1],dp[]) = max(card[5],dp[4]+dp[1],dp[3]+dp[2])
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]
dp[1] = cards[1]
for i in range(2,N+1):
  dp[i] = max([cards[i]] + [dp[i-j]+dp[j] for j in range(1,i//2+1)])
print(dp[N])