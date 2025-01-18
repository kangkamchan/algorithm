n = int(input())
i = 2
while n>1 :
    while n % i == 0:
        print(i)
        n //= i
    i += 1
    if i * i > n:
        if n != 1:
            print(n)
        break