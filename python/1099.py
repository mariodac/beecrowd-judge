# 1099 - Soma de Ímpares Consecutivos II

# -*- coding: utf-8 -*-
n = int(input())

for _ in range(n):
    x, y = map(int, input().strip().split())
    if y > x:
        numbers = [i for i in range(x, y) if i != x if i != y if i % 2 != 0]
    else:
        numbers = [i for i in range(y, x) if i != x if i != y if i % 2 != 0]
    print(sum(numbers))