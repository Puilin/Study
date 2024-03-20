n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
largest = arr[n-1]
second = arr[n-2]

ans = (largest * k + second) * (m // (k+1)) + largest * (m % (k+1))
print(ans)