n, l, d = map(int, input().split())

time = []
for _ in range(n-1):
    for _ in range(l):
        time.append(1)
    for _ in range(5):
        time.append(0)

time += [1 for _ in range(l)]

t = d
while True:
    try:
        if time[t] == 0:
            print(t)
            break
        else:
            t += d
    except IndexError:
        print(t)
        break