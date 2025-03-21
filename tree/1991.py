#입력값
#N = 노드의 개수
#node, left, right = 각노드, 왼쪽자식, 오른쪽자식 N개
#graph = [] graph[node] = [왼쪽, 오른쪽]
#첫째줄에 전위순회 둘째줄에 중위순회 셋째줄에 후위순회 한 결과를 출력
import sys
input = sys.stdin.readline
N = int(input().strip())
graph = [[] for _ in range(128)] #대문자를 아스키코드로 바꾸어 숫자로 표현하는 방식으로 대략 128개로 설정
for _ in range(N):
    node, left, right = map(lambda str:ord(str),input().strip().split())
    graph[node] = [left,right]
preorder = ""
inorder = "" 
postorder = ""
def dfs(node):
    global preorder, inorder, postorder
    if node == 46:
        return
    preorder += chr(node)
    dfs(graph[node][0])
    inorder += chr(node)
    dfs(graph[node][1])
    postorder += chr(node)
dfs(65)
print(preorder)
print(inorder)
print(postorder)