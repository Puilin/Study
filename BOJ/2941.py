str = input()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
while len(str) > 0:
    found = False
    for j in croatian:
        if str.startswith(j):
            count += 1
            str = str[len(j):]
            found = True
            break

    if not found:
        count += 1
        str = str[1:]

print(count)