transportes = ('CARRO', 'BICICLETA', 'NAVIO', 'TREM', 'MOTO', 'PATINETE', 'CART', 'QUADRICICLO ', 'LANCHA')

for c in transportes:
    print(f'\nPara a palavra \033[1m{c}\033[m temos: ', end='')
    for vogais in c:
        if vogais in 'AIEOU':
            print(f"\033[1m{vogais}\033[m", end=' ')
