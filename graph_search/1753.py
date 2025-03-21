#입력값
#V, E = 정점, 간선의 개수
#K = 시작 정점
#graph = [] graph[i] = [j,v] i번째 정점에서 j번째 정점으로 가는 가중치
from collections import deque
import sys
input = sys.stdin.readline
V, E = map(int,input().strip().split())
K = int(input())
graph = {}
for _ in range(E):
    u, v, w = map(int,input().strip().split())
    if graph.get(u) == None:
        graph[u] = {}
    if graph.get(u).get(v) == None:
        graph.get(u)[v] = w
    else:
        tw = graph.get(u)[v]
        graph.get(u)[v] = min(tw,w)
answers = [float("inf") for _ in range(V+1)]
q = deque()
q.append([K,0])
answers[K] = 0
while q:
    v, w = q.popleft()
    if graph.get(v) == None:
        continue
    next_graph = graph[v]
    next_keys = next_graph.keys()
    for next in next_keys:
        nw = next_graph[next]+w
        q.append([next,nw])
        answers[next] = min(answers[next],nw)
for answer in answers[1:]:
    if answer == float("inf"):
        print("INF")
    else:
        print(answer)