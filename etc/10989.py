N = int(input())
dic = {n:0 for n in range(1,10001)}
for _ in range(N):
    n = int(input())
    dic[n] += 1
for key in dic.keys():
    for _ in range(dic[key]):
        print(key)
