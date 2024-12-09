n = int(input())

for i in range(n, 3, -1):
    num = list(str(i))
    
    flag = True
    for part in num:
        if part != "7" and part != "4":
            flag = False
    
    if flag:
        print(i)
        break