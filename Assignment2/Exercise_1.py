n = 4

row = n
column = n

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if i + j <= n + 1:
            print ' '
        else:
            print '*'
