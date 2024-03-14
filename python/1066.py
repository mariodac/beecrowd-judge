# 1066 Pares, Ímpares, Positivos e Negativos 
# -*- coding: utf-8 -*-
even = []
odd = []
positives = []
negatives = []
for _ in range(5):
    n = float(input())
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
    if n > 0:
        positives.append(n)
    elif n < 0:
        negatives.append(n)
print(f'{len(even)} valor(es) par(es)')
print(f'{len(odd)} valor(es) impar(es)')
print(f'{len(positives)} valor(es) positivo(s)')
print(f'{len(negatives)} valor(es) negativo(s)')
