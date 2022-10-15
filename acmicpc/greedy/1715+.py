'''
10
123
456
234
998
12
7
876
887
455
234

12108
===========================
3
10
20
40

100
'''
# 거 시발 진짜 뭔소린지 모르것다
import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

heapq.heapify(heap)

total = 0
if n == 1:
    print(total)
else:
    while len(heap) >= 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        total += a + b
        heapq.heappush(heap, a+b)
print(total)

# import sys

# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))

# total = 0
# arr.sort()
# if n == 1:
#     print(0)
# else:
#     while True:
#         if len(arr) == 1:
#             break
#         elif len(arr) == 2:
#             total += arr[0] + arr[1]
#             break
#         else:
#             s = 0
#             if arr[0] + arr[1] < arr[1] + arr[2]:
#                 s = arr[0] + arr[1]
#                 arr.pop(1)
#                 arr.pop(0)
#             else:
#                 s = arr[1] + arr[2]
#                 arr.pop(2)
#                 arr.pop(1)
#             total += s
#             arr.insert(0, s)
#     print(total)