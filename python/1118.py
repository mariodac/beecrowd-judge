# 118 - Várias Notas Com Validação

# -*- coding: utf-8 -*
notas = []
while True:
    n = float(input())
    if n >= 0 and n <= 10:
        notas.append(n)
        if len(notas) == 2:
            print(f'media = {(sum(notas)/2):.2f}')
            notas = []
            x = '4'
            while x != '2':
                print('novo calculo (1-sim 2-nao)')
                x = input()
                if x == '1':
                    break
            if x == '2':
                break
    else:
        print('nota invalida')
    