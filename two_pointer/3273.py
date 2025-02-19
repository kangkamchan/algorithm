#n개의 서로다른 양의 정수로 이루어진 수열, 수열의 2 수를 더해서 x를 만족하는 경우의 수를 구하기
#입력 n = 수열의 크기, array = [] 수열, x = 조건수
#완전탐색
# n = int(input())
# array = list(map(int, input().split()))
# x = int(input())
# answer = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if array[i] + array[j] == x:
#             answer += 1
# print(answer)

#투포인터
#1. 정렬
#2. 맨앞, 맨뒤에 각각 포인터를 두고 탐색
#3. 합이 조건보다 크면 => 맨 뒤의 포인터를 앞으로 이동
#   합이 조건보다 작으면 => 맨 앞의 포인터를 뒤로 이동
#   합이 조건과 같으면 => count += 1, 앞, 뒤 포인터를 둘다 한칸씩 이동
n = int(input())
array = list(map(int, input().split()))
x = int(input())
array.sort()
i = 0
j = n - 1
answer = 0
while(True):
    if i >= j:
        break
    if array[i] + array[j] == x:
        answer += 1
        i += 1
        j -= 1
    elif array[i] + array[j] > x:
        j -= 1
    elif array[i] + array[j] < x:
        i += 1
print(answer)