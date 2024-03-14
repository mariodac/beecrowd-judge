# 1098 	Sequencia IJ 4
# -*- coding: utf-8 -*-

i = float(0)
while i <= 2:
    for j in range(1, 4):
        if i.is_integer():
            print(f'I={i:.0f} J={(j+i):.0f}')
        else:
            print(f'I={i:.1f} J={(j+i):.1f}')
    i += 0.2
    i = round(i, 1)
    
