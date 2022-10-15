# n개의 로프가 각각 k/n만큼 하중을 버터야 하므로 오름차순 정렬 후 P1*n, P2*(n-1), ... 중에 최대값
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

maximum = 0
for i in range(n):
    if lst[i] * (n-i) > maximum:
        maximum = lst[i] * (n-i)

print(maximum)