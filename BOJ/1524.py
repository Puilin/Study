T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())
    sejun = list(map(int, input().split()))
    sebi = list(map(int, input().split()))

    sejun.sort()
    sebi.sort()

    i, j = 0, 0
    while True:
        if i == len(sejun):
            print("B")
            break
        if j == len(sebi):
            print("S")
            break
            
        if sejun[i] >= sebi[j]:
            j += 1
        elif sejun[i] < sebi[j]:
            i += 1