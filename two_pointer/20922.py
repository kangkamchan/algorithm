#입력값 N = 수열의 길이, K = 같은수최댓값, array = [수열]
#길이가 N인 array 에서 같은 수가 K개 이하인 부분수열 길이의 최댓값 출력
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
array = list(map(int,input().split()))
count_array = [0] * 200001
s = 0
e = 0
answer = 0
while e < N:
    if count_array[array[e]] == K:
        answer = max(answer, e - s)
        count_array[array[s]] -= 1
        s += 1
        continue
    if e == N - 1:
        answer = max(answer,e - s + 1)
    count_array[array[e]] += 1
    e += 1
print(answer)