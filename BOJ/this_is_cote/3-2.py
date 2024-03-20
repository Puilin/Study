n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

largest = max(arr)

arr.remove(largest)
secondary = max(arr)

result = 0
count = 0
for i in range(m):
    if count < k:
        result += largest
        count += 1
    else:
        result += secondary
        count = 0

print(result)