import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = int(sys.stdin.readline())

    proper = True
    for i in range(2, 1000001):
        if s % i == 0:
            proper = False
            break
    
    if proper:
        print("YES")
    else:
        print("NO")