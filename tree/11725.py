#입력값
#N = 노드의 개수
#i, j = 연결된 두 정점 N-1개
#graph = [] graph[n] = [i,j,k]n번째 노드와 연결된 노드들
#1번 노드가 루트라고 할 때 2번노드부터 각 노드의 부모노드를 순서대로 출력
import sys
input = sys.stdin.readline
sys.setrecrusionlimit = 1000000
N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int,input().strip().split())
    graph[i].append(j)
    graph[j].append(i)
parents = [0 for _ in range(N+1)]

def dfs(node,prev):
    parents[node] = prev
    for next in graph[node]:
        if next == prev:
            continue
        dfs(next,node)

dfs(1,0)
for i in range(2,N+1):
    print(parents[i])