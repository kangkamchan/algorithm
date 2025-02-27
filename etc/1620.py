N, M = map(int,input().split())
dic = {i+1:input() for i in range(N)}
reverse_dic = {v:k for k,v in dic.items()}
for _ in range(M):
    question = input()
    if question.isdigit():
        print(dic[int(question)])
    else:
        print(reverse_dic[question])
