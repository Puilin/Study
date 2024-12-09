x, y = map(int, input().split())

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
max_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count_days = 0
for i in range(1, x):
    count_days += max_days[i]

count_days += y

print(days[(count_days-1) % 7])