# candy = 1 <= 사탕의 수 <= 100 
# C >= B + 2
# A % 2 == 0
# A,B,C != 0 

candy = int(input())
answer = 0
for a in range(1,candy+1):
    for b in range(1,candy+1):
        for c in range(1,candy+1):
            if a+b+c == candy:
                if a!=0 and b!=0 and c!=0:
                    if a%2 == 0:
                        if c >= b + 2:
                            answer += 1
print(answer)