# 몰라 문제가 좆병신같아 무슨 말인지 이해도 안되게 써놨음

n = int(input())
s = 0
a = 0
for i in range(1, n+1):
    s += i
    a += 1
    if n == 2:
        print(1)
        break
    elif s == n:
        print(a)
        break
    elif s > n:
        print(a-1)
        break
