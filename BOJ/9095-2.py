inp = int(input())
test_case = [int(input()) for _ in range(inp)]

def fun1(n):
    my_list = [0, 1, 2, 4]
    if n > 3:
        for i in range(4, n+1):
            my_list.append(my_list[i-1] + my_list[i-2] + my_list[i-3])
    return my_list[n]

for i in test_case:
    print(fun1(i))