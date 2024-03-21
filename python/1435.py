# 1435 Matriz Quadrada I
n = 1
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

    for i in range(n):
        for j in range(n):
            print(f'  {matrix[i][j]} ', end='')
        print('')
    print('')