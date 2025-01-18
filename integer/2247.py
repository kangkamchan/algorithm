#실질적 약수 : 2 ~ n ** 0.5 까지 나누어 떨어지는 수 
#SOD(n) : n의 실질적 약수들의 합 n이 소수면 0
#CSOD(n) : SOD(1) + SOD(2) + ... + SOD(n) 
#완전탐색 : 1 ~ n 까지 루프돌면서 실질적 약수 다 더하기 => n 은 최대 2억 루트n은 최대 약 15000정도?? ==> X
#
#완전탐색 ==> 1000000 정도 넘어가면 겁나 오래걸림
# n = int(input())
# csod = 0
# for i in range(1,n+1):
#     for div in range(2,int(i**0.5)+1):
#         if i % div == 0:
#             csod += div
#             if div != i//div:
#                 csod += i//div
# print(csod%1000000)

# 1 ~ n 까지 2로 나누어 떨어지는 수 => n//2 개 => csod += n//2 * 2
# 3 => n//3 개 => csod += n//3 * 3
# m => n//m 개 => csod += n//m * m
# 근데 m 이 소수면 m 을 빼줘야함 => 근데 어차피 자기 자신은 포함안시켜야해서 모든 수에서 m을 빼줘야함
# n // m 이 2가 되는 m 보다 커지면 => 가장 작은 소인수인 2를 곱해도 n을 넘어가니까 의미가 없다 
# 최종 m을 1 ~ n//2 까지 루프돌면서 csod에 (n//m - 1) * m 더해주기

# n = int(input())
# csod = 0
# for m in range(2,n//2+1):
#     csod += (n//m -1) * m
# print(csod%1000000)
# => 시간초과로 폐기

# N = n//2 => N은 더해질 구간 끝
# m 은 2 부터 N 까지 돌면서 위 과정을 하면 m 이 커지면서 n//m 이 같은 구간이 존재함
# m 이 i 일 때 n//m 이 k 이면 i 부터 n//k 까지는 n//m 이 k 로 유지됨 n//k 를 j 라고 하면
# i ~ j 까지는 (i ~ j 까지 합) * k, i ~ j 까지 합은 등차수열 합 공식으로 한번에 계산 가능
# 건너뛰는 구간이 생기므로 시간을 매우 단축시킬 수 있다
# 아이디어는 여기까지,,, 내일 구현해보자,,,
# sum(n//m*m -m) =>sum(n//m*m) - sum(m) m은 2부터이므로 => sum(n//m*m) - m*(m+1)/2 + 1
# s1=sum(n//m*m) 
# s2=sum(m)
# csod = s1 - s2

n = int(input())
N = n//2
S_1 = 0
S_2 = N*(N+1)//2 - 1
m = 2
while m <= N:
    k = n//m
    j = n//k
    S_m = j*(j+1)//2 - (m-1)*m//2
    S_1 += k*S_m
    m = j+1
csod = S_1 - S_2
print(csod%1000000)

