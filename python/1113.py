# 1113 - Crescente e Decrescente

# -*- coding: utf-8 -*-

while True:
    x, y = map(int, input().strip().split())
    if x == y:
        break
    elif x > y:
        print('Decrescente')
    else:
        print('Crescente')