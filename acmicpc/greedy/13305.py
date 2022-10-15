# 그리디
'''
4
2 3 1
5 2 4 1

18
================
4
3 3 4
1 1 1 1

10
'''
# 첫 번째 도시에서는 주유 필수, 마지막 도시에서는 주유 불가능
# 현재 도시의 금액과 앞으로 남은 도시들의 금액을 비교해서 최저가 지점 찾고(cheapest_points)
# 최저가 지점의 가격 * 최저가 지점 끼리의 거리 합

n = input()
distance = input().split()
distance = [int(x) for x in distance]
price = input().split()
price = [int(x) for x in price]

tot = 0
cheapest_points = [0]

for i in range(len(price)-1):
    if price[cheapest_points[-1]] > price[i]:
        cheapest_points.append(i)

cheapest_points.append(len(price)-1)

for j in range(len(cheapest_points)-1):
    tot += price[cheapest_points[j]] * sum(distance[cheapest_points[j]:cheapest_points[j+1]])

print(tot)