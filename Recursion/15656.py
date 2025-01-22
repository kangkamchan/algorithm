# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
def recursion(number):
  if number == M:
    print(*arr)
    return
  for i in range(N):
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