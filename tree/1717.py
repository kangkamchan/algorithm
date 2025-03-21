#유니온파인드
#union : 두 트리를 합침
#find : 두 노드의 조상이 일치하는지 확인
#입력
#n, m = 최초노드의수, 연산의수
#m개의 연산
#0 a b = a와 b를 합침
#1 a b = a와 b의 루트가 같은지 확인해서 YES, NO 출력

def _union(A,B):
    parent[A] = B
def _find(A):
    if parent[A] == A:
        return A
    else:
        return _find(parent[A])

n, m = map(int,input().strip().split())
parent = [i for i in range(n+1)]
# for _ in range(m):
#     x, a, b = map(int,input().strip().split())
#     if x == 0:
#         _union(a,b)
#     else:
#         if _find(a) == _find(b):
#             print("YES")
#         else:
#             print("NO")

#find 최적화 => 경로 단축: 모든 자식들을 루트에 붙여버리기
def __find(A):
    if parent[A] == A:
        return A
    else:
        parent[A] = __find(parent[A])
        return parent[A]
#union 최적화 => union by rank: 랭크를 두고 합치기, 높이가 낮은 union을 높은 union 루트에 합친다
rank = [0 for _ in range(n+1)]
def __union(A,B):
    A = __find(A)
    B = __find(B)
    if rank[A] == rank[B]:
        parent[A] = B
        rank[B] += 1
    elif rank[A] > rank[B]:
        parent[B] = A
    else:
        parent[A] = B
for _ in range(m):
    x, a, b = map(int,input().strip().split())
    if x == 0:
        __union(a,b)
    else:
        if __find(a) == __find(b):
            print("YES")
        else:
            print("NO")
print(rank)
print(parent)