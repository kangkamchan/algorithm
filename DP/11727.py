#2Xn 타일링2
#2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수 출력
#입력값 n
#n      answer
#1      1
#2      3
#3      a2 + 2*a1 = 5
#4      a3 + 2*a2 = 11

n = int(input())
dp = [0] * 10000
dp[1] = 1
dp[2] = 3
for i in range(3,n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n]%10007)