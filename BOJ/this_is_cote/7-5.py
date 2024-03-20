n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for item in arr2:
    if binary_search(arr, item):
        print("yes")
    else:
        print("no")