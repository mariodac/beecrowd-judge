# 1133 - Resto da Divisão

x = int(input())
y = int(input())
if x < y:
    numbers = [i for i in range(x+1, y)]
else:
    numbers = [i for i in range(y+1, x)]
for i in numbers:
    if (i % 5 == 2) or (i % 5 == 3):
        print(i)