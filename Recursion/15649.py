# 입력 N, M 1 부터 N 까지 자연수 중 M 개를 고른 수열을 중복 없이 모두 출력

# N = 4 M = 4
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# N, M = map(int,input().split())
# numbers = [i for i in range(1,N+1)]
# 그냥 완전탐색 => for문을 반복하는게 제한됨
# for i in range(1,N+1):
#   for j in range(1,N+1):
#     if i == j:
#       continue
#     for k in range(1,N+1):
#       if i == k:
#         continue
#       if j == k:
#         continue
#       for l in range(1,N+1):
#         if i == l:
#           continue
#         if j == l:
#           continue
#         if k == l:
#           continue
#         print(i,j,k,l)

def recursion(number):
  if number == M:
    print(*arr)
    return
  for i in range(1,N+1):
    if i in arr:
      continue
    arr.append(i)
    recursion(number+1)
    arr.pop()
N, M = map(int,input().split())
arr = []
recursion(0)