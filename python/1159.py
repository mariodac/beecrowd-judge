x = 1
numeros = []
while x != 0:
    x = int(input().strip())
    if x != 0:
        numeros.append(x)
inicio = 0
pares = 0
soma = 0
for i in numeros:
    inicio = i
    while pares < 5:
        if inicio % 2 == 0:
            soma += inicio
            pares += 1
        inicio += 1
    print(soma)
    pares = 0
    soma = 0
        