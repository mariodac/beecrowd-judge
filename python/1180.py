# 1180 Menor e Posição
import re
n = int(input().strip())
numbers = input()
x = []
x = [int(item) for item in numbers.split(' ') if re.match(r'-?\d+', item)]
mininum = min(x)
print(f'Menor valor: {mininum}')
print(f'Posicao: {x.index(mininum)}')