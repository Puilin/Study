inp = int(input())

def fun1(n):
    array = []
    for a in range(n+1):
        for b in range(n+1):
            if 5*a + 3*b == n:
                array.append(a+b)
    if array != []:
        return min(array)
    else:
        return -1

print(fun1(inp))
