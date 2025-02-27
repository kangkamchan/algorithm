#공유기 설치
#입력값 
#N = 집의수, C = 공유기의 수
#houses = [] 집 좌표 리스트
#N개의 집에 C개의 공유기를 설치할 때 가장 인접한 공유기 사이 거리의 최댓값 출력
N, C = map(int,input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
print(houses)
first = houses[0]
print(first)
last = houses[N-1]
print(last)
s = 0
e = N-1
answer = 0
while s <= e:
    mid = (s+e)//2
    print(s,e,mid,answer)
    distance_from_first = houses[mid] - first
    distance_from_last = last - houses[mid]
    if distance_from_first < distance_from_last:
        answer = max(answer,distance_from_first)
        s = mid+1
    else:
        answer = max(answer,distance_from_last)
        e = mid-1
print(answer)