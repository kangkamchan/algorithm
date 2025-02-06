#입력 n = 정수 삼각형 높이
#n 줄, 각 줄마다 n개의 숫자 주어짐
#맨 위에서부터 바로 오른쪽 또는 왼쪽 아래에 있는 수 한개만 선택하며 내려갈 때 최댓값
#dp = [[0 for _ in range(i)] for i in range(501)]
#dp[i][j] =>1층부터 i층의 j번째 까지 더한 값 저장
#재귀함수 정의
#입력값 floor=>현재 몇층인지, idx=>현재 층의 인덱스, sum=>현재까지 합
#dp[floor][idx] != 0 => dp[floor][idx] = max()
#0이면 바로저장
#floor += 1
#sum += 왼쪽값 또는 오른쪽값, 왼쪽값 idx 오른쪽값 idx+1 => 왼쪽,오른쪽 각각 재귀함수 총 2번 호출
#탈출조건 floor > n
# 재귀함수만 활용
# dp = [[0 for _ in range(i)] for i in range(n+1)]
# def triangle_max_sum(i,j):
#   if i == n-1:
#     return triangle[i][j]
#   return triangle[i][j] + max(triangle_max_sum(i+1,j),triangle_max_sum(i+1,j+1))
# print(max(dp[n]))

#DP 메모이제이션
#삼각형 꼭대기(=> 0층이라 함)에서 시작
#0층 0번째합 => 1층 0번째까지 합, 1층 1번째까지 합 중 큰거 + 0층 0 번째값
#1층 0번째합 => 2층 0번째까지 합, 2층 1번째까지 합 중 큰거 + 1층 0 번째 값
#i층 j번째 합 => i+1층 j번째까지 합, i+1층 j+1번째까지 합 중 큰거 + i 층 j 번째 값
#i층 j번째 합 => dp[i][j]
#i층 j번째 값 => triangle[i][j]
#재귀함수 작성
#dp[i][j]에 값이 존재하면 dp[i][j]반환
#존재하지 않으면 dp[i][j]=triangle[i][j] + max([i+1][j] 까지합,[i+1][j+1]까지 합)하고 dp[i][j]반환
#탈출조건 i == 마지막층 이면 마지막층까지 합은 마지막층 값이므로 => dp[i][j] 에 triangle[i][j] 넣고 dp[i][j]반환
# def triangle_max_sum(i,j):
#   if i == n-1:
#     dp[i][j] = triangle[i][j]
#     return dp[i][j]
#   if dp[i][j] is not None:
#     return dp[i][j]
#   dp[i][j] = triangle[i][j] + max(triangle_max_sum(i+1,j),triangle_max_sum(i+1,j+1))
#   return dp[i][j]
# n = int(input())
# triangle = [list(map(int,input().split())) for _ in range(n)]
# dp = [[None] * (i+1) for i in range(n)]
# print(triangle_max_sum(0,0))
#DP 타뷸레이션션
import sys
input = sys.stdin.readline
n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]
for i in range(n-2,-1,-1):
  for j in range(i+1):
    triangle[i][j] = max(triangle[i][j]+triangle[i+1][j],triangle[i][j]+triangle[i+1][j+1])
print(triangle[0][0])
