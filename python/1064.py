# 1064 	Positivos e Média
# -*- coding: utf-8 -*-
positives = []
for _ in range(6):
    n = float(input())
    if n > 0:
        positives.append(n)
media = sum(positives)/len(positives)
print(f'{len(positives)} valores positivos')
print(f'{media:.1f}')
