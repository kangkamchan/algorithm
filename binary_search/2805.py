#입력값
#N = 나무의 수, M = 필요한 나무의 높이
#trees = [] 나무 높이 리스트
#필요한 높이 M 을 얻기 위한 절단 높이 최댓값 출력
N, M = map(int,input().split())
trees = list(map(int,input().split()))
s = 0
e = max(trees)
answer = 0
while True:
    if s > e:
        break
    result = 0
    mid = (s + e) // 2
    for tree in trees:
        if tree > mid:
            result += tree - mid
    if result == M:
        answer = mid
        break
    elif result > M:
        answer = max(answer,mid)
        s = mid + 1
    else:
        e = mid - 1
print(answer)