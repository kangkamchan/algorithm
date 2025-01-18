k = int(input())

jewels = []

div = 2
while k > 1:
    while k % div == 0:
        jewels.append(div)
        k //= div
    div += 1
    if div * div > k:
        if k>1:
            jewels.append(k)
        break

print(len(jewels))
print(*jewels)