# 확인하고자 하는 수의 개수 n
# 확인할 수 s
# s가 2이상 1000000이하의 소인수를 가지면 NO, 아니면 YES 출력

n = int(input())
for _ in range(n):
    s = int(input())
    for i in range(2,1000002):
        if(i==1000001):
            print("YES")
        if(s%i==0): 
            print("NO")
            break
