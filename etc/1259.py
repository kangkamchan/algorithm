#팰린드롬수 = 거꾸로 읽어도 똑같은 수 예)121, 12321, 1233321
#입력된 수가 펠린드롬수면 yes 아니면 no 출력
#0 입력시 종료

while True:
    N = input()
    if N == "0":
        break
    if N == N[::-1]:
        print("yes")
    else:
        print("no")