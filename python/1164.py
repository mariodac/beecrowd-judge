n = int(input())
divisores = []
for _ in range(n):
    x = int(input())
    for i in range(1,x):
        if x % i == 0:
            divisores.append(i)
    if sum(divisores) == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
    divisores = []