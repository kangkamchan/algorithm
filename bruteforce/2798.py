#입력값 N, M = 카드의수, 조건수
#cards = [] 카드 리스트
#카드 리스트에서 3장을 골라 조건수 이하의 가장 가까운 수를 출력
N, M = map(int,input().split())
cards = list(map(int,input().split()))
answer = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                answer = max(answer,sum)
print(answer)