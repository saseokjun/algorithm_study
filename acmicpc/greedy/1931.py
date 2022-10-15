# 그리디
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

4
======================
4
1 5
1 7
2 3
3 4

2
'''
# 시작 시간, 끝나는 시간으로 오름차순 정렬
# 다음 시작 시간이 현재 끝나는 시간보다 늦으면 추가 아니면 패스
n = input()
lst = [input().split() for _ in range(int(n))]
lst.sort(key= lambda x:int(x[0]))
lst.sort(key= lambda x:int(x[1]))

cnt = 1
s, e = lst[0]
for i in range(int(n)-1):
    s2, e2 = lst[i+1]
    if int(e) <= int(s2):
        e = e2
        cnt += 1

print(cnt)
