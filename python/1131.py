# 1131 - Grenais

grenais = 0
vitoria_gremio = 0
vitoria_inter = 0
empate = 0
while True:
    gols_inter, gols_gremio = map(int, input().strip().split(' '))
    grenais += 1
    if gols_inter == gols_gremio:
        empate += 1
    elif gols_inter > gols_gremio:
        vitoria_inter += 1
    else:
        vitoria_gremio += 1
    print('Novo grenal (1-sim 2-nao)')
    novo_grenal = int(input())
    if novo_grenal == 2:
        print(f'{grenais} grenais')
        print(f'Inter:{vitoria_inter}')
        print(f'Gremio:{vitoria_gremio}')
        print(f'Empates:{empate}')
        if vitoria_inter == vitoria_gremio:
            print('Nao houve vencedor')
        elif vitoria_inter > vitoria_gremio:
            print('Inter venceu mais')
        else:
            print('Gremio venceu mais')
        break
    