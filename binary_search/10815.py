#입력값
#N = 카드 개수
#array_1 = [] 가지고있는 카드 리스트
#M = 찾아야할 개수
#array_2 = [] 찾아야할 카드 리스트
#array_2의 요소가 array_1에 존재하면 1 존재하지않으면 0 을 공백으로 구분해서 출력

import sys
input = sys.stdin.readline
#list의 기본 탐색기능 활용 => 선형탐색 O(n)
# N = int(input())
# array_1 = list(map(int,input().split()))
# M = int(input())
# array_2 = list(map(int,input().split()))
# answer = []
# for number in array_2:
#     if number in array_1:
#         answer.append(1)
#     else:
#         answer.append(0)
# print(*answer)

#set의 기본 탐색기능 활용 => 해시 탐색 O(1)
# N = int(input())
# array_1 = set(list(map(int,input().split())))
# M = int(input())
# array_2 = list(map(int,input().split()))
# answer = []
# for number in array_2:
#     if number in array_1:
#         answer.append(1)
#     else:
#         answer.append(0)
# print(*answer)

#이진탐색 => O(logN)
N = int(input())
array_1 = sorted(list(map(int,input().split())))
M = int(input())
array_2 = list(map(int,input().split()))
answer = []
for number in array_2:
    s = 0
    e = N - 1
    while True:
        if e < s :
            answer.append(0)
            break
        mid = (e + s) // 2
        if number == array_1[mid]:
            answer.append(1)
            break
        elif number > array_1[mid]:
            s = mid + 1
        else :
            e = mid - 1
print(*answer)