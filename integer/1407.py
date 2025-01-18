#2로 몇 번 나누어질까
#아이디어
#모든 수는 1로 나누어 떨어진다 => 입력값 * 1
#이 중 2로 나누어 떨어지는 수의 개수 만큼 1씩 더한다 => 입력값 // 2 * 1
#이 중 4로 나누어 떨이지는 수의 개수 만큼 2씩 더한다 => 입력값 // 4 * 2
# ...
#2**n < 입력값 일 때 까지 2**n 으로 나누어 떨어지는 수의 개수 만큼 2**(n-1) 씩 더한다 
#입력값 former, latter
#나누는 수 div

former, latter = map(int,input().split())

def sum_max_power_of_two(input):
    sum = input
    div = 2
    while div <= input:
        sum += (input//div) * (div//2)
        div *= 2
    return sum
print(sum_max_power_of_two(latter)-sum_max_power_of_two(former-1))
