#입력값
#N = 전체용액 수
#array = [] 입력값 리스트
#입력값 : -1,000,000,000 이상 1,000,000,000 이하 정수 오름차순
#두 값을 골라 더했을 때 0에 가장 가까운 조합을 출력
N = int(input())
array = list(map(int,input().split()))
s = 0
e = N-1
answer = [0,0]
sum = 2000000001
while s <= e:
    temp_sum = array[s] + array[e]
    if abs(temp_sum) < sum:
        answer[0] = array[s]
        answer[1] = array[e]
        sum = abs(temp_sum)
    if temp_sum < 0:
        s += 1
    elif temp_sum > 0:
        e -= 1
    else:
        break
print(*answer)
