n = int(input())

arr = list(map(int, input().split()))

def solve(n, arr):
    if n == 1:
        return 1
    else:
        b = []
        max_k = 0
        # 맨앞에 짝수를 먼저 고르는 케이스
        mode = 0 # 0은 짝수 1은 홀수
        for num in arr:
            if mode == 0:
                if num % 2 == 0:
                    b.append(num)
                    mode = 1
            else:
                if num % 2 == 1:
                    b.append(num)
                    mode = 0
        max_k = max(len(b), max_k)

        b = []

        # 맨앞에 홀수를 먼저 고르는 케이스
        mode = 1
        for num in arr:
            if mode == 0:
                if num % 2 == 0:
                    b.append(num)
                    mode = 1
            else:
                if num % 2 == 1:
                    b.append(num)
                    mode = 0
        
        max_k = max(len(b), max_k)

        return max_k        

print(solve(n, arr))