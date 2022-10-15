'''
9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1

528
==========================
5
1 1 1 6 0
2 7 8 3 1

18
==========================
3
1 1 3
10 30 20

80
==========================
'''
# arr은 오름차순, arr2는 내림차순 정렬해서 각 인덱스끼리 곱
n = input()
arr = input().split()
arr2 = input().split()
arr = [int(x) for x in arr]
arr2 = [int(x) for x in arr2]

arr.sort()
arr2.sort(reverse=True)
tot = 0

for i in range(len(arr)):
    tot += arr[i] * arr2[i]

print(tot)