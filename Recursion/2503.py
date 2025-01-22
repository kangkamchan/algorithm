# 숫자야구 재귀함수로 풀기
import sys
sys.setrecursionlimit(9999999)
def recursion(hint_idx,number):
  global answer
  if hint_idx == N:
    answer += 1
    recursion(0,number+1)
    return
  if number == 1000:
    return
  if number_baseball(hint[hint_idx],number):
    recursion(hint_idx+1,number)
  else:
    recursion(0,number+1)

def number_baseball(hint, number):
  hint_number = hint[0]
  hint_strike = hint[1]
  hint_ball = hint[2]
  hint_h, hint_t, hint_o = map(int,str(hint_number))
  number_h, number_t, number_o = map(int,str(number))
  if number_h == 0 or number_t == 0 or number_o == 0:
    return False
  if number_h == number_t or number_t == number_o or number_o == number_h:
    return False
  strike = 0
  ball = 0
  if hint_h == number_h :
    strike += 1
  if hint_t == number_t:
    strike += 1
  if hint_o == number_o:
    strike += 1
  if hint_h == number_t or hint_h == number_o:
    ball += 1
  if hint_t == number_h or hint_t == number_o:
    ball += 1
  if hint_o == number_h or hint_o == number_t:
    ball += 1
  if strike == hint_strike and ball == hint_ball:
    return True
  return False

N = int(input())
hint = [list(map(int,input().split())) for _ in range(N)]
answer = 0
recursion(0,100)
print(answer)