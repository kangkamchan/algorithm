# 입력값 A: 입력개수, B: 간격, arr: 더할 숫자 배열
# A = 10, B = 2, arr = 3 -2 -4 -9 0 3 7 13 8 -3 이라고하면
# 누적합 배열 : prefix = A+1의 길이만큼 0으로 채워서 만들기 [0 for _ in range(A+1)] => prefix = [0,0,0,0,0,0,0,0,0,0,0]
# for i in range(A+1) prefix[i+1] = prefix[i] + arr[i] => prefix = [0, 3, 1, -3, -12, -12, -9, -2, 11, 19, 16]
# 간격만큼 더한값은 B 부터 A+1 까지 돌면서  prefix[i] - prefix[i-B] 

A, B = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0 for _ in range(A+1)]
for i in range(A):
  prefix[i+1] = prefix[i] + arr[i]
answer = 0
for i in range(B,A+1):
  temp = prefix[i] - prefix[i-B]
  if i == B:
    answer = temp
  else:
    answer = max(temp,answer)
print(answer)