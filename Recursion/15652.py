# 1~N 자연수 중 M개 비내림차순

def recursion(start,number):
  if number==M:
    print(*arr)
    return
  for i in range(start,N+1):
    arr.append(i)
    recursion(i,number+1)
    arr.pop()

N,M=map(int,input().split())
arr=[]
recursion(1,0)