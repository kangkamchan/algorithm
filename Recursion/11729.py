#하노이의 탑
#입력값 N 옮겨야할 탑의 층수
#출력값 최소 이동 횟수와 이동 과정
#이동횟수 = 2^N - 1
#이동과정
#N층을 1번에서 3번으로 옮기려면 개수N 시작s 도착e 경유v
#N-1층을 2번에 만들고(개수N-1 시작s 도착v 경유e) N번째거를 1 -> 3으로 한 후(print(시작,도착)) N-1층을 3번에 만들어야함(개수N-1 시작v 도착e 경유s)
#f => if N==1 print(s,e) else f(N-1,s,v,e) print(s,e) f(N-1,v,e,s)

def hanoi(number, start, end, via):
  if number == 1:
    print(start, end)
    return
  else:
    hanoi(number-1, start, via, end)
    print(start, end)
    hanoi(number-1, via, end, start)

N = int(input())
print(2**N - 1)
hanoi(N,1,3,2)


