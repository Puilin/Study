n = input()

len(n) // 2
left = 0
for i in range(0, len(n)//2):
    left += int(n[i])
right = 0
for j in range(len(n)//2, len(n)):
    right += int(n[j])

if left == right:
    print("LUCKY")
else:
    print("READY")