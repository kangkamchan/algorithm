#피보나치수열 단순 재귀함수로 구현하기 => 20번째 수 구하는데 21891번의 연산 수행
# def fibo(n):
#   global m
#   m += 1
#   print(m)
#   if n<2:
#     return n
#   else:
#     return fibo(n-1) + fibo(n-2)
# m = 0
# n = int(input())
# print(fibo(n))
#피보나치 수열 메모이제이션으로 구현하기
#fibo(n) = fibo(n-1) + fibo(n-2)
#fibo(n-1) 이 이미 있다면 그냥 사용, 없다면 fibo(n-2) + fibo(n-3)으로 저장 하고 리턴
def fibo(n):
  global m
  m += 1
  print(m)
  if n <= 2:
    return dp[n]
  if n in dp:
    return dp[n]
  else:
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
m = 0
dp = {
  0:0,
  1:1,
  2:1
}

n = int(input())
print(fibo(n))
