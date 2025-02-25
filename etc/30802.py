#입력
#N = 참가자 수
#T_array = [] 사이즈별 티셔츠 수
#T, P = 묶음으로 구매할 수 있는 티셔츠, 연밀 수
#티셔츠는 사이즈멸 묶음으로만 구매 가능
#연필은 묶음 + 개별로 구매 가능
#티셔츠를 총 몇묶음 주문해야하는지
#연필은 몇묶음, 개별로 몇개 주문해야하는지 출력

N = int(input())
T_array = list(map(int,input().split()))
T, P = map(int,input().split())
T_result = 0
for t in T_array:
    T_result += (t-1)//T + 1
print(T_result)
print(N//P, N%P)