n, x = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if arr[end] > target:
        return end
    else:
        return start

idx = binary_search(arr, x-1)
idx2 = binary_search(arr, x+1)
count = 0
for i in range(idx, idx2):
    if arr[i] == x:
        count += 1
print(count if count > 0 else -1)