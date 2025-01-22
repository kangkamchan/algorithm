# 1~N 자연수 중 M 개를 고른 수열 중복 없이 오름차순
# 반복문 반복 횟수는 number로 체크
# 반복문 시작값을 입력해줌
# 첫 반복시 1부터 2번째 2부터 3번째 3부터 M번째 M부터

def recursion(start, number):
  if number==M:
    print(*arr)
    return
  for i in range(start,N-M+number+2):
    if i in arr:
      continue
    arr.append(i)
    recursion(i+1, number+1)
    arr.pop()
N,M = map(int,input().split())
arr = []
recursion(1,0)