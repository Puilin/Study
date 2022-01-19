N = int(input())

count = 0
for _ in range(N):
    word = input()
    lst = list(word)
    history = []
    passed = True
    for i in range(len(lst)):
        if lst[i] in history:
            if lst[i-1] != lst[i]:
                passed = False
                break
        else:
            history.append(lst[i])
    if passed:
        count += 1

print(count)