#L = 문자열길이
#str = 문자열
#영문 소문자 a ~ z 로 이루어진 문자열 해시값으로 출력
#a = 1, b = 2 ... z = 26으로 변환
#각 자리수마다 31의 거듭제곱을 곱해서 더한 후 1234567891로 나눈 나머지
L = int(input())
str = input()
array = list(map(lambda x: ord(x)-96,str))
print(array)
hash = 0
for i in range(L):
    hash += array[i] * (31**i)
print(hash%1234567891)