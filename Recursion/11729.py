#하노이의 탑
#입력값 N 옮겨야할 탑의 층수
#출력값 최소 이동 횟수와 이동 과정
#이동횟수 = 2^N - 1
#이동과정
#N 층 -> 2번에 N-1층 -> 3번에 N-2층 -> 2번에 N-3층 -> ... -> N 이 짝수면 2번 홀수면 3번에 1층
# 개수,출발,도착,경유 => 개수가1이면 print(출,도) 아니면 경유를 도착으로 f(개수-1,출발,경유,도착) print(출,도) 경유를 출발로 출발을 경유로 f(개수-1,경유,도착,출발) 

def recursion(number, start, end, via):
  if number == 1:
    print(start, end)
    return
  else:
    recursion(number-1, start, via, end)
    print(start, end)
    recursion(number-1, via, end, start)

N = int(input())
print(2**N - 1)
recursion(N,1,3,2)


