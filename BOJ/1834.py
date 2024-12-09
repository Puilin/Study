import sys

n = int(sys.stdin.readline())

sum = 0
for i in range(1, n):
    sum += i * (n+1)

print(sum)