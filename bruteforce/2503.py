N = int(input())
hints = [list(map(int,input().split())) for _ in range(N)]
answer = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a==b or b==c or c==a:
                continue
            count = 0
            for hint in hints:
                num = hint[0]
                strike = hint[1]
                ball = hint[2]
                h,t,o = map(int,str(num))
                sc = 0
                bc = 0
                if a == h:
                    sc += 1
                if b == t:
                    sc += 1
                if c == o:
                    sc += 1
                if a == t or a == o:
                    bc += 1
                if b == h or b == o:
                    bc += 1
                if c == h or c == t:
                    bc += 1
                if strike==sc and ball==bc:
                    count += 1 
            if count == N:
                answer += 1

print(answer)