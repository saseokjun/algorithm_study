import sys
n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())
    arr = []
    for j in range(m):
        lst = sys.stdin.readline().split(' ')
        arr.append(lst)
    arr.sort(key= lambda x:int(x[0]))
    min_rank = len(arr)
    cnt = 0
    for k in arr:
        if int(k[1]) <= min_rank:
            cnt += 1
            min_rank = int(k[1])
    print(cnt)
