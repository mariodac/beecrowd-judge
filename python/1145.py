# 1145 - Sequência Lógica 2

x, y = map(int, input().strip().split(' '))
index = 1
for i in range(1,y+1):
    if index == x:
        index = 1
        print(f'{i}')
    else:
        print(f'{i}', end=' ')
        index += 1
