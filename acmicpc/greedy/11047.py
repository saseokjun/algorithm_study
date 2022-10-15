# 그리디
'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

6
==========================
5 10
1
2
4
8
16

2
'''
# 가장 큰 단위부터 비교해서 몫은 동전 갯수, 나머지는 남은 금액


n, k = map(int, input().split())
cnt = 0
lst = [int(input()) for _ in range(n)]

lst.reverse()
for j in lst:
    if k == 0:
        break

    if j < k:
        d, k = divmod(k, j)
        cnt += d
    elif j == k:
        k = 0
        cnt += 1
    else:
        pass

print(cnt)