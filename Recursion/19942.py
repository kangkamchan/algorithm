#입력값 식재료의 개수 N
#다음 줄에는 단백질, 지방, 탄수화물, 비타민의 최소 영양성분을 나타내는 정수 mp,mf,ms,mv가 주어진다.
#이어지는 N개의 각 줄에는 
#i번째 식재료의 단백질, 지방, 탄수화물, 비타민과 가격이 5개의 정수 
#p_i, f_i, s_i, v_i, c_i와 같이 주어진다. 식재료의 번호는 1부터 시작한다.
import sys
input = sys.stdin.readline

N = int(input())
min_nutrients = list(map(int,input().split()))
ingredients = [list(map(int,input().split())) for _ in range(N)]

def recursion(idx, use_log, sum_nutrients, price, use):
  global answers
  global min_price
  if idx == N:
    if use == 0:
      return
    if sum_nutrients[0]>=min_nutrients[0] and sum_nutrients[1]>=min_nutrients[1] and sum_nutrients[2]>=min_nutrients[2] and sum_nutrients[3]>=min_nutrients[3]:
      if price < min_price:
        min_price = price
        temp_answer = [i+1 for i in use_log]
        answers.clear()
        answers.append(temp_answer)
      elif price == min_price:
        temp_answer = [i+1 for i in use_log]
        answers.append(temp_answer)
    return
  temp_use_log = use_log[:]
  temp_sum_nutrients = sum_nutrients[:]
  #사용안할경우 그대로 입력
  recursion(idx+1, temp_use_log[:], temp_sum_nutrients[:], price, use)
  #사용할경우 use_log 에 추가, sum_nutrients 0 ~ 3에 ingredients[idx] 0 ~ 3 추가, price에 ingredients[idx][4] 추가, use + 1
  temp_use_log.append(idx)
  for i in range(4):
    temp_sum_nutrients[i] += ingredients[idx][i]
  price += ingredients[idx][4]
  recursion(idx+1, temp_use_log[:], temp_sum_nutrients[:], price, use+1)

min_price = 1000000
answers = []
recursion(0,[],[0,0,0,0],0,0)
if min_price == 1000000:
  print(-1)
else:
  print(min_price)
  answers.sort()
  print(*answers[0])