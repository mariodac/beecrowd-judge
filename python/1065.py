# 1065 	Pares entre Cinco Números

# -*- coding: utf-8 -*-
even = []
for _ in range(5):
    n = float(input())
    if n % 2 == 0:
        even.append(n)
media = sum(even)/len(even)
print(f'{len(even)} valores pares')
