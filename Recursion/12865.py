#입력 N, K = 물건개수, 최대무게
#W_i, V_i = 각 물건의 무게, 가치
#최대무게를 만족하면서 가치합의 최대값 출력
#items = []
#파라미터 idx, 무게, 가치
#물건 넣으면 idx+1, 무게 += 무게, 가치 += 가치
#물건 안넣으면 idx+1, 무게, 가치
#탈출조건 idx == N 이면 최대가치 갱신 
import sys
input = sys.stdin.readline

def recursion(idx, w, v):
  global max_value
  if w > K:
    return
  if idx == N:
    max_value = max(max_value, v)
    return
  #물건 넣음
  recursion(idx+1, w+items[idx][0], v+items[idx][1])
  #물건 안넣음
  recursion(idx+1, w, v)


N, K = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(N)]
max_value = 0
recursion(0,0,0)
print(max_value)