import sys

n, c = map(int, input().split())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    arr.append(x)

arr.sort()

def is_possible(arr, mid, c):
    count = 1
    current_house = arr[0]
    for house in arr:
        if house - current_house >= mid:
            count += 1
            current_house = house
    return count >= c

def binary_search(arr, c):
    start = 1  # 가능한 최소 거리
    end = arr[-1] - arr[0]  # 가능한 최대 거리
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if is_possible(arr, mid, c):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

result = binary_search(arr, c)
print(result)
