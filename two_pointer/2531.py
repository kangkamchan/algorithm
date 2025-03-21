#회전초밥
#입력값 N, d, k, c = 접시수, 가짓수, 연속수, 쿠폰번호
#N개 수로 이루어진 수열, k개 연속된 부분 수열 중 c를 포함해서 숫자 가짓수의 최댓값
import sys
input = sys.stdin.readline
N, d, k, c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k]
answer = 0
s = 0
e = k - 1
answer = 0
while s <= N - 1:
    sushi_set = set(sushi[s:e+1])
    sushi_set.add(c)
    answer = max(answer,len(sushi_set))
    s += 1
    e += 1
print(answer)