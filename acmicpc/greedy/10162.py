n = int(input())

arr = [0, 0, 0]

while True:
    if n == 0:
        break
    if n >= 300:
        d, n = divmod(n, 300)
        arr[0] += d
    elif n >= 60:
        d, n = divmod(n, 60)
        arr[1] += d
    elif n >= 10:
        d, n = divmod(n, 10)
        arr[2] += d
    else:
        n = 0
        arr = -1

if arr == -1:
    print(-1)
else:
    print(' '.join(str(x) for x in arr))