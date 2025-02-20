#부분합
#입력 N = 수열의길이, S = 기준, array = [수열]
#array에서 S 이상이 되는 연속된 수들의 부분합의 최소 길이
#s = 0
#e = 0
#temp_sum = 현재 부분수열의 합
#answer = 최소 길이
#array[s] ~ array[e] 합 s보다 작으면 e += 1
#array[s] ~ array[e] 합 s보다 크거나 같으면 answer = min(answer,e-s+1) s += 1
#s == e == N-1 이면 종료
import sys
input = sys.stdin.readline
N, S = map(int,input().split())
array = list(map(int,input().split()))
s = 0
e = 0
temp_sum = array[0]
answer = 1000001
while True:
    if temp_sum < S:
        if e == N - 1:
            break
        e += 1
        temp_sum += array[e]
    else:
        answer = min(answer,e-s+1)
        if s == N-1:
            break
        temp_sum -= array[s]
        s += 1
print(answer if answer < 100001 else 0)