X = int(input())

def fun(X):
    step = 1
    count = X
    x = 1; y = 1
    while count-1 > 0:
        for i in range(step):
            if count == 1:
                break
            if i+1 == step:
                if step % 2 == 0:
                    x += 1
                else:
                    y += 1
                step += 1
                count -= 1
            else:
                if step % 2 == 0:
                    x += 1
                    y -= 1
                    count -= 1
                else:
                    x -= 1
                    y += 1
                    count -= 1
        
    print(str(x) + "/" + str(y))

fun(X)