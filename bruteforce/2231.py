#분해합
#N 의 분해합 = N + N의 각자리수 합
#M 의 분해합이 N일 경우 M은 N의 생성자
#입력값 N 의 가장 작은 생성자를 출력
N = int(input())
answer = 0
for i in range(N):
    num_arr = list(map(int,str(i)))
    if i + sum(num_arr) == N:
        answer = i
        break
print(answer)