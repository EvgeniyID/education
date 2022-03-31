import random

a = [random.randint(0,5) for i in range(10)]
print(a)
count = [0]*6
for i in a:
    count[i] += 1
for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ') * count[i], end='')


s = 'dnSDJnjkd sdlKJJLPjiJjdf jknl ndskjlnweu  im,. ./213!";№%!'
letters = [0]*26
for i in s.lower():
    if i >= 'a' and i <= 'z':
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97)*letters[i], end='')


b = [random.randint(-10,10) for i in range(10)]

count = [0]*21
for i in b:
    count[i+10] += 1
for i in range(21):
    if count[i] > 0:
        print(i-10, count[i])
