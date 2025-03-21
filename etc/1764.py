import sys
input = sys.stdin.readline
N, M = map(int,input().strip().split())
not_listen = set([input().strip() for _ in range(N)])
not_see = set([input().strip() for _ in range(M)])
both = sorted(list(not_listen.intersection(not_see)))
print(len(both))
for name in both:
    print(name)



    
