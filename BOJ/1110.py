n = input()
origin = n

cnt = 0
while True:
    if len(n) < 2:
        n = '0' + n
    a, b = tuple(map(int, list(n))) 
    c = (a + b) % 10
    n = str(b * 10 + c)
    cnt += 1

    if n == origin:
        break

print(cnt)