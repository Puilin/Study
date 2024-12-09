k = int(input())

stack = []
for _ in range(k):
    num = int(input())
    if num == 0:
        del stack[-1]
    else:
        stack.append(num)

print(sum(stack))