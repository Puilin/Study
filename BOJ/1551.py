n, k = map(int, input().split())

arr = list(map(int, input().split(",")))
for _ in range(k):
    vary_arr = []
    for i in range(len(arr)-1):
        vary_arr.append(arr[i+1]-arr[i])
    arr = vary_arr

print(*arr, sep=',')