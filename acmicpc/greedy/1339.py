n = int(input())
dct = {}

for _ in range(n):
    word = input()
    word_length = len(word)
    for i in range(word_length):
        if word[i] in dct:
            dct[word[i]] += 10**(word_length - i - 1)
        else:
            dct[word[i]] = 10**(word_length - i - 1)

arr = sorted(dct.items(), key = lambda item: item[1], reverse=True)
total = 0
for j in range(len(arr)):
    total += arr[j][1] * (9-j)

print(total)
