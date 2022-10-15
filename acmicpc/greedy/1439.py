# 0 연속 갯수, 1 연속 갯수 비교해서 작은거
n = input()

last = n[0]
zero = 1 if last == '0' else 0
one = 1 if last == '1' else 0
for i in range(len(n)):
    if n[i] != last:
        if n[i] == '0':
            zero += 1
        else:
            one += 1
        last = n[i]

print(min(zero, one))
