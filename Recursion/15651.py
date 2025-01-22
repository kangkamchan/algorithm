# 1~N 자연수 중 M 개를 고른 수열 중복 허용

def recursion(number):
  if number == M:
    print(*arr)
    return
  for i in range(1,N+1):
    arr.append(i)
    recursion(number+1)
    arr.pop()

N,M=map(int,input().split())
arr=[]
recursion(0)
