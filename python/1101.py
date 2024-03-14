# 1101 - Sequência de Números e Soma
# -*- coding: utf-8 -*-

while True:
    x, y = map(int, input().strip().split())
    if x <= 0 or y <= 0:
        break
    
    if y > x:
        numbers = [i for i in range(x, y+1)]
    else:
        numbers = [i for i in range(y, x+1)]
    str_number = list(map(str, numbers))
    print(f"{' '.join(str_number)} Sum={sum(numbers)}")