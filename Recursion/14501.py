#입력값 N 남은 일수
#T_i, P_i : i일 걸리는 시간, 금액
#schedule = [] 입력받은 시간, 금액
#max_price = -1 최대 금액
#파라미터 idx, price
#탈출조건 idx >= N , 이때 max_price 갱신
#상담하면 idx += schedule[idx][0], price+=scedule[idx][1] 입력
#상담안하면 다음거로 idx += 1
import sys
input = sys.stdin.readline
N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]
max_price = 0
m = 0
def recursion(idx, price):
  global max_price
  global m
  m += 1
  print(m)
  if idx == N:
    max_price = max(max_price, price)
    return
  if idx > N:
    return
  #상담을 했을 때
  recursion(idx+schedule[idx][0],price+schedule[idx][1])
  #상담을 안했을떄
  recursion(idx+1,price)
recursion(0,0)
print(max_price)