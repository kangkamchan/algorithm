#입력값 N = 데이터수, M = 저장공간수, data = [] N개의 데이터 용량 리스트
#데이터를 M개의 저장공간에 나누어담아야 할 때 저장공간의 최소 용량을 출력
#데이터는 순서대로 넣어야함

N,M = map(int,input().split())
data = list(map(int,input().split()))
s = max(data)
e = sum(data)
answer = 1000000000
while s<=e:
    mid = (s+e)//2
    count = 1
    temp_sum = 0
    for d in data:
        temp_sum += d
        if temp_sum > mid:
            count += 1
            temp_sum = d
        if count > M:
            break
    if count > M:
        s = mid + 1
    else:
        answer = min(mid,answer)
        e = mid - 1
print(answer)