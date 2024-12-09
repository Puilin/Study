n = int(input())

caves = list(map(int, input().split()))
checked = [False] * n

start_num = 0
for i in range(len(caves)):
    if caves[i] > 0:
        start_num = i
        break

ans = 0
for j in range(len(caves)):
    cur = (j + start_num) % n
    if caves[cur] > 0:
        ans += caves[cur]
    else:
        if caves[(cur+n-1)%n] > 0:
            ans += 1
            checked[cur] = True
        else:
            if not checked[(cur+n-1)%n]:
                ans += 1
                checked[cur] = True

print(ans)