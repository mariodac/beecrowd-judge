t = int(input())
anos = 0
for _ in range(t):
    pa, pb, g1, g2 = map(float, input().strip().split())
    pa, pb = int(pa), int(pb)
    g1, g2 = round(g1, 1), round(g2,1)
    # novo_pa = pa + (pa * g1) / 100
    while pa < (pb+0.9) and anos < 101:
        pa += int((pa*g1)/100)
        pb += int((pb*g2)/100)
        anos += 1
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')
    anos = 0
        
