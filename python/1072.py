# 1072 	Intervalo 2
# -*- coding: utf-8 -*-
n = int(input())
in_range = 0
out_range = 0
for _ in range(n):
    x = int(input())
    if x in range(10, 21):
        in_range += 1
    else:
        out_range += 1
        
print(f'{in_range} in\n{out_range} out')
    