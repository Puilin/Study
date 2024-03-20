n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() # n log n

def binary_split(arr):
    start = 0
    end = arr[-1]

    while (start <= end):
        mid = (start + end) // 2

        cum = 0
        for i in arr:
            if i < mid:
                continue
            cum += i - mid
        
        
        if cum > m:
            start = mid + 1
        else:
            end = mid - 1
    return mid

print(binary_split(arr))