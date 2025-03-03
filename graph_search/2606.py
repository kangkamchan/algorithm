#입력값
#N = 컴퓨터수
#M = 연결수
#graph = [[] for _ in range(N+1)] 연결을 표현한 그래프, graph[i] = i번째 컴퓨터와 연결된 컴퓨터 리스트
#1번 컴퓨터가 바이러스에 걸렸을 때 연결된 컴퓨터들은 모두 바이러스에 걸림
#바이러스에 걸린 컴퓨터 수를 출력
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#BFS
#가까운 곳에서부터 탐색하기 위해 FIFO 자료구조가 필요함
from collections import deque
q = deque()
q.append(1)
visited[1] = True
answer = 0
while len(q) > 0:
    node = q.popleft()
    print(node)
    answer+=1
    for next in graph[node]:
        if visited[next]:
            continue
        visited[next] = True
        q.append(next)
print(answer-1)

#DFS
# answer = 0
# recursion(1)
# print(answer-1)
# def recursion(i):
#     global answer
#     visited[i] = True
#     answer += 1
#     print(i)
#     for j in graph[i]:
#         if not visited[j]:
#             recursion(j)