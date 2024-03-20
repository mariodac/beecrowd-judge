# 1187 Área Superior
def do_operation(operation, matrix, rows, cols):
    total = 0
    result = 0
    index = 0
    x = 0
    for i in range(0, int((rows / 2) - 1)):
        for j in range(x+1, cols-(x+1)):
            total += matrix[i][j]
            # print(f'[{i}][{j}]={matrix[i][j]}')
            index += 1
        x += 1
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