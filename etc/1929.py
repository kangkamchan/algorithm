#M 이상 N 이하 소수 모두 출력
M, N = map(int,input().split())
array = [True for _ in range(N+1)]
array[1] = False
for i in range(2,int(N**0.5)+1):
    if array[i]:
        j = 2
        while i*j <= N:
            array[i*j] = False
            j += 1
for i in range(M,N+1):
    if array[i]:
        print(i)

