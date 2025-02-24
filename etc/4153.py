#직각삼각형
#입력 공백으로 구분된 숫자 3개
#세 변의 길이로 직각삼각형 여부에 따라 right, wrong 출력
#0 0 0 입력되면 종료

while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    a *= a
    b *= b
    c *= c
    if 2 * max(a,b,c) == a + b + c:
        print("right")
    else:
        print("wrong")