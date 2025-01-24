#입력될 재료의 개수 N, 신맛 S 쓴맛 B
#신맛은 곱해지고 쓴맛은 더해짐
#재료는 1개 이상 사용해야만 함
#재료중 신맛과 쓴맛의 차이가 가장 작은 경우에서 차이를 출력
#최초 신맛 S=1 쓴맛 B=0 사용한수 U=0
#재료 사용시 S = S * s, B = B + b, U += 1
#재료 미사용시 S = S, B = B, U = U
#N회 반복후 answer = min(answer,abs(S-B))
import sys
input = sys.stdin.readline

def recursion(index, S, B, U):
  global answer
  if index == N:
    if U == 0:
      return
    answer = min(answer,abs(S-B))
    return
  recursion(index+1, S*ingredients[index][0], B+ingredients[index][1], U+1)
  recursion(index+1, S, B, U)

N = int(input())
ingredients = [list(map(int,input().split())) for _ in range(N)]
answer = 99999999999999
recursion(0,1,0,0)
print(answer)