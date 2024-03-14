# 1060 	Números Positivos
# -*- coding: utf-8 -*-
positives = 0
for _ in range(6):
    n = float(input())
    if n > 0:
        positives += 1
        
print(f'{positives} valores positivos')