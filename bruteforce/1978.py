n = int(input())
numbers = list(map(int,input().split()))

answer = 0
for number in numbers:
    for i in range(2,number+1):
        if i == number:
            answer += 1
            break
        if number % i == 0:
            break
print(answer)