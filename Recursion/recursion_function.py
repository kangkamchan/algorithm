# 재귀함수 : 함수 안에서 그 함수를 호출함
# 활용 : 반복문을 반복시킬 때 효율적임
# 입력값 M 만큼 반복문을 돌려야하면 그냥 반복문으로 작성하기에는 제한됨
def recursion(n, recursion_end, iteration_end):
    if n == recursion_end:
      return
    for i in range(iteration_end):
        print(i)
        recursion(n+1, recursion_end, iteration_end)

recursion(0,3,3)
