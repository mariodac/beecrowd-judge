# 1142 - PUM
n = int(input())

count = 0
for _ in range(n):
    for _ in range(3):
        count += 1
        print(f'{count}', end=' ')
    count += 1
    print('PUM')