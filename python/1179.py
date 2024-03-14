impar = []
par = []
for _ in range(15):
    n = int(input().strip())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    if len(par) == 5:
        for i, j in enumerate(par):
            print(f'par[{i}] = {j}')
        par = []
    if len(impar) == 5:
        for i, j in enumerate(impar):
            print(f'impar[{i}] = {j}')
        impar = []

if len(impar) > 0:
    for i, j in enumerate(impar):
        print(f'impar[{i}] = {j}')
if len(par) > 0:
    for i, j in enumerate(par):
        print(f'par[{i}] = {j}')
