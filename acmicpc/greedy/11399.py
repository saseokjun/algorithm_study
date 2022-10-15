# 그리디
'''
5
3 1 4 3 2

32
'''
# 오름차순 정렬, P1*n + P2*(n-1) + P3*(n-2) + ...
n = input()
l = input().split()
l = [int(x) for x in l]
l.sort()

cnt = 0
for i in range(int(n)):
    cnt += l[i] * (int(n) - i)

print(cnt)
