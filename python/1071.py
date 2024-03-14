# 1071 	Soma de Impares Consecutivos I
# -*- coding: utf-8 -*-
x = int(input())
y = int(input())

if y > x:
    numbers = [i for i in range(x, y) if i != x if i != y if i % 2 != 0]
else:
    numbers = [i for i in range(y, x) if i != x if i != y if i % 2 != 0]
print(sum(numbers))