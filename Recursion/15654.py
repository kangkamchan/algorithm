# N, M 을 입력받음
# N개의 자연수를 입력받음
# 입력받은 N 개 중에서 M개를 고른 수열

def recursion(number):
  if number == M:
    print(*arr)
    return
  for i in range(0,N):
    if N_arr[i] in arr:
      continue
    arr.append(N_arr[i])
    recursion(number+1)
    arr.pop()
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
N_arr = list(map(int,input().split()))
N_arr.sort()
arr = []
recursion(0)