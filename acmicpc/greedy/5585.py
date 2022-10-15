# 그냥 기본적인 그리디 알고리즘. 1000-n에서 제일 큰 동전(500엔)부터 빼서 채워나감
n = int(input())

n = 1000 - n
cnt = 0

while True:
    if n == 0:
        break
    
    if n >= 500:
        d, n = divmod(n, 500)
        cnt += d
    elif n >= 100:
        d, n = divmod(n, 100)
        cnt += d
    elif n >= 50:
        d, n = divmod(n, 50)
        cnt += d
    elif n >= 10:
        d, n = divmod(n, 10)
        cnt += d
    elif n >= 5:
        d, n = divmod(n, 5)
        cnt += d
    elif n >= 1:
        d, n = divmod(n, 1)
        cnt += d

print(cnt)
    