# 1061 	Tempo de um Evento
# -*- coding: utf-8 -*-

_, init_day = input().split(' ')
init_day = int(init_day)
init_hours, init_minutes, init_seconds = map(int, input().strip().split(' : '))
_, finish_day = input().split(' ')
finish_day = int(finish_day)
finish_hours, finish_minutes, finish_seconds = map(int, input().strip().split(' : '))
total_init = (init_day * 86400) + (init_hours * 3600) + (init_minutes * 60) + init_seconds
total_finish = (finish_day * 86400) + (finish_hours * 3600) + (finish_minutes * 60) + finish_seconds
duration = total_finish - total_init
days = duration // 86400
rest = duration % 86400
hours = rest // 3600
rest %= 3600
minutes = rest // 60
rest %= 60
seconds = rest
print(f'{days} dia(s)\n{hours} hora(s)\n{minutes} minuto(s)\n{seconds} segundo(s)')