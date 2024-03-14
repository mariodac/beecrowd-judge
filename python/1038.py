# 1038 	Lanche
# -*- coding: utf-8 -*-

prices = [4, 4.50, 5, 2, 1.50]

index, qtd = map(int, input().strip().split(' '))
total = qtd * prices [index - 1]
print(f'Total: R$ {total:.2f}')