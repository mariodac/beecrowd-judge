# 1189 Área Esquerda
def do_operation(operation, matrix, rows, cols):
    total = 0
    result = 0
    index = 0
    x = 0
    max = int((rows / 2) - 1)
    to_max = False
    for i in range(1, rows - 1):
        if x >= max:
            x -= 1
            to_max = True
        for j in range(x+1):
            total += matrix[i][j]
            # print(f'[{i}][{j}]={matrix[i][j]}')
            index += 1
        if x >= max:
            x -= 1
        elif not to_max:
            x += 1
        else:
            x -= 1
    if operation == 'M':
        if index == 0:
            index = 1
        result = float(total / index)
    else:
        result = float(total)
    return result
operation = input().strip()
operation = operation.upper()
matrix = []
cont = 1
rows = 12
cols = 12
for i in range(rows):
    x = []
    for j in range(cols):
        x.append(float(input().strip()))
    matrix.append(x)
print(f'{do_operation(operation, matrix, rows, cols):.1f}')