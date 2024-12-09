n = input()

is_eugine = False
for i in range(1, len(n)):
    left = list(map(int, list(n[:i])))
    right = list(map(int,list(n[i:])))

    left_base = 1
    for l in left:
        left_base *= l
    
    right_base = 1
    for r in right:
        right_base *= r
    
    if left_base == right_base:
        is_eugine = True
        break

if is_eugine:
    print("YES")
else:
    print("NO")