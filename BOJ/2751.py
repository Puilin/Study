import sys

n = int(input())

arr = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    arr.append(num)

arr.sort()

for i in arr:
    sys.stdout.write(str(i) + '\n')