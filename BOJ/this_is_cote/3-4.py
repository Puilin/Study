n, m = map(int, input().split())
cards = []
for _ in range(n):
    row = list(map(int, input().split()))
    cards.append(row)

largest = 0
for row in cards:
    if largest < min(row):
        largest = min(row)

print(largest)