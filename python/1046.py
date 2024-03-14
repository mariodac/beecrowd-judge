# 1046 	Tempo de Jogo
# -*- coding: utf-8 -*-

init_hour, finish_hour = map(int, input().strip().split(' '))

total_hour = finish_hour - init_hour
if (finish_hour - init_hour <= 0):
    total_hour = 24 + (finish_hour - init_hour)
print(f'O JOGO DUROU {total_hour} HORA(S)')