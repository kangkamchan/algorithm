"""
입력값: N = 표의크기 , M : 합을 구해야할 횟수
arr = 입력된 표
answer_arr = 답을 구할 시작값, 종료값 배열
"""

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
question_arr = [list(map(int,input().split())) for _ in range(M)]
print(arr)
print(question_arr)
prefix = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
  for j in range(1,N+1):
    prefix[i][j] = prefix[i][j-1]+prefix[i-1][j]-prefix[i-1][j-1] + arr[i-1][j-1]
print(prefix)
for question in question_arr:
  start_x = question[0]
  start_y = question[1]
  end_x = question[2]
  end_y = question[3]
  answer = prefix[end_x][end_y] - prefix[end_x][start_y-1] - prefix[start_x-1][end_y] + prefix[start_x-1][start_y-1]
  print(answer)