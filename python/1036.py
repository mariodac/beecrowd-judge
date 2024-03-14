# 1036 	Fórmula de Bhaskara
# -*- coding: utf-8 -*-
from math import sqrt

a, b, c = map(float, input().strip().split(' '))
delta = b ** 2 - (4 * a * c)
if (delta > 0) and (a != 0.0):
    x1 = (- b + sqrt(delta)) / (2 * a)
    x2 = (- b - sqrt(delta)) / (2 * a)
    print (f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
else:
    print('Impossivel calcular')