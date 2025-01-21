# 1~N 자연수 중 M 개를 고른 수열 중복 없이 오름차순

def recursion(number):
  if number==M:
    print(*arr)
    return
  for i in range(number+1,N-M+number+2):
    if i in arr:
      continue
    arr.append(i)
    recursion(number+1)
    arr.pop()
N,M = map(int,input().split())
arr = []
recursion(0)