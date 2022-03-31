n = 6
mas = [5, 4, 6, 7, 8, 3]
count = 0
for j in range(n-1):
    for i in range(n-1-j):
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]
print(*mas)

