# 재조합 해서 30의 배수 체크 : 각 자릿수 합이 3의 배수 + 자릿수 중 0 포함여부 확인
n = input()
length = len(n)
s = 0
arr = []

for i in range(0, len(n)):
    s += int(n[i])
    arr.append(int(n[i]))

if s % 3 == 0 and 0 in arr:
    arr.sort(reverse=True)
    print(''.join(str(x) for x in arr))
else:
    print(-1)
