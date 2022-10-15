i = 1
while True:
    n = input()
    if n == '0 0 0':
        break
    else:
        l, p, v = n.split(' ')
        a, b = divmod(int(v), int(p))
        print(f'Case {i}: {a*int(l) + min(b, int(l))}')
        i+=1