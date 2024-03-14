# 1035 	Teste de Seleção 1
# -*- coding: utf-8 -*-

a, b, c, d = map(int, input().strip().split(' '))
soma_ab = a + b
soma_cd = c + d
if (b > c) and (d > a) and (soma_cd > soma_ab) and ((c > 0) and (d > 0)) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")