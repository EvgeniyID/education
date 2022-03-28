n = int(input())
mas = [[0]*n for i in range(n)]
i = 1
x = 0
y = -1
d_row = 0 # -1 0 1
d_column = 1 # -1 0 1
while i <= n**2:
    if 0 <= x+d_row < n and 0 <= y+d_column < n and mas[x + d_row][y+d_column] == 0:
        x += d_row
        y += d_column
        mas[x][y] = i
        i += 1
    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
            d_column = -1
            d_row = 0
        elif d_column == -1:
            d_column = 0
            d_row = -1
        elif d_row == -1:
            d_column = 1
            d_row = 0
