#2개의 병을 반납하면 min(A+B+X/2, X) 용량의 하나의 병으로 교환해줌
#입력 N = 병의 개수, X = 용량, array = [i번째 병의 남은 양]
#구할 수 있는 가득찬 병의 최댓값 출력
import sys
input = sys.stdin.readline
N, X = map(int,input().split())
array = sorted(list(map(int,input().split())))
remains = 0
s = 0
e = N-1
answer = 0
while s <= e:
    if e == s:
        remains += 1
        break
    if array[e] >= X:
        answer += 1
        e -= 1
        continue
    if array[e] + array[s] >= X/2:
        answer += 1
        e -= 1
        s += 1
    else:
        remains += 1
        s += 1
print(answer+remains//3)
