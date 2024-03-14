# 1134 - Tipo de Combustível

alcool = 0
gasolina = 0
diesel = 0
while True:
    code = int(input())
    if code >= 1 and code <= 4:
        if code == 4:
            print('MUITO OBRIGADO')
            print(f'Alcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')
            break
        elif code == 1:
            alcool += 1
        elif code == 2:
            gasolina += 1
        elif code == 3:
            diesel += 1
        
