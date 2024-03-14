# 1149 - Somando Inteiros Consecutivos 

inputs = [int(x)  for x in input().split(' ')]
inputs = [x for x in inputs if x > 0]
a, n = inputs[0], inputs[1]
    
soma = 0

for i in range(n):
    soma += a + i
    
print(soma)