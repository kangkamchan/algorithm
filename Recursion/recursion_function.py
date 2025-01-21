# 재귀함수 : 함수 안에서 그 함수를 호출함
# 활용 : 반복문을 반복시킬 때 효율적임
# 입력값 M 만큼 반복문을 돌려야하면 그냥 반복문으로 작성하기에는 제한됨

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
