n = 1
matrixs = []
while n != 0:
    matrix = []
    n = int(input().strip())
    x = 0
    for i in range(1, n+1):
        collums = []
        for j in range(1, n+1):
            x = i
            if j < x:
                x = j
            if n - i + 1 < x:
                x = n - i + 1
            if n - j + 1 < x:
                x = n - j + 1
            collums.append(x)
        matrix.append(collums)
    matrixs.append(matrix)
for m in matrixs:
    for i in range(len(m)):
        for j in range(len(m)):
            if j == 0:
                print('%3hd'%m[i][j], end='')
            else:
                print(' %3hd'%m[i][j], end='')
            # if j == len(m) - 1:
            #     print('%3hd',m[i][j])
            # else:
            #     print('%3hd',m[i][j], end=' ')
        print('')
    print('')