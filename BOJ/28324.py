n = int(input())

via = list(map(int, input().split()))

acc = 0
now = 0
for i in range(len(via)-1, -1, -1):
    if via[i] > now:
        now += 1
    else:
        now = via[i]
    acc += now
print(acc)