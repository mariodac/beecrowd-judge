# 1021 Notas e Moedas
# -*- coding: utf-8 -*-

entrada = input()
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
moedas1_real = 0
moedas50_centavos = 0
moedas25_centavos = 0
moedas10_centavos = 0
moedas5_centavos = 0
moedas1_centavos = 0
try:
    reais, centavos = map(int, entrada.split('.'))
    centavos = centavos + reais*100
    
    notas100 = centavos // 10000
    resto = centavos % 10000
    
    notas50 = resto // 5000
    resto %= 5000
    
    notas20 = resto // 2000
    resto %= 2000
    
    notas10 = resto // 1000
    resto %= 1000
    
    notas5 = resto // 500
    resto = resto % 500
    
    notas2 = resto // 200
    resto %= 200
    
    moedas1_real = resto // 100
    resto %= 100
    
    moedas50_centavos = resto // 50
    resto %= 50
    
    moedas25_centavos = resto // 25
    resto %= 25
    
    moedas10_centavos = resto // 10
    resto %= 10
    
    moedas5_centavos = resto // 5
    resto %= 5
    
    moedas1_centavos = resto // 1
    print(f'NOTAS:\n{notas100:.0f} nota(s) de R$ 100.00\n{notas50:.0f} nota(s) de R$ 50.00')
    print(f'{notas20:.0f} nota(s) de R$ 20.00\n{notas10:.0f} nota(s) de R$ 10.00')
    print(f'{notas5:.0f} nota(s) de R$ 5.00\n{notas2:.0f} nota(s) de R$ 2.00')
    print(f'MOEDAS:\n{moedas1_real:.0f} moeda(s) de R$ 1.00\n{moedas50_centavos:.0f} moeda(s) de R$ 0.50')
    print(f'{moedas25_centavos:.0f} moeda(s) de R$ 0.25\n{moedas10_centavos:.0f} moeda(s) de R$ 0.10')
    print(f'{moedas5_centavos:.0f} moeda(s) de R$ 0.05\n{moedas1_centavos:.0f} moeda(s) de R$ 0.01')
except:
    ...