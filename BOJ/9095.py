inp = int(input())

def partition1(n):
    count = 0
    count += 1
    return [1 for _ in range(n // 1)]

def partition2(n):
    global count
    if n % 2 == 0:
        count += 1
        return [2 for _ in range(n//2)]
    else:
        count += 1
        return [2 for _ in range(n//2)] + [1]

def partition3(n):
    global count
    if n % 3 == 0:
        count += 1
        return [3 for _ in range(n//3)]
    elif n % 3 == 1:
        count += 1
        return [3 for _ in range(n//3)] + [1]
    else:
        count += 1
        return [3 for _ in range(n//3)] + [2]

def first_step(lst):
    global count
    temp = []
    for i in lst:
        temp += partition2(i)
    return temp

def second_step(lst):
    global count
    temp = []
    for i in lst:
        temp += partition1(i)
    return temp

count = 0
_ = partition3(inp)
_ = first_step(partition3(inp))
_ = second_step(partition3(inp))
_ = second_step(first_step(partition3(inp)))
print(count)