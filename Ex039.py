ano = int(input('Digite o ano de nascimento: '))

conta = 2023 - ano

print()

print(f'Quem nasceu em {ano} tem {conta} hoje.')

if conta == 18:
    print('Voce devera se alistar esse ano pois ja tem 18 anos!')

if conta < 18:
    print(f'Voce ainda tem {conta} anos de idade. Faltam {18 - conta} anos ate o seu alistamento.')
    print(f'O seu alistamento ocorrera em {2023 + 18 - conta}')

if conta > 18:
    print(f'Voce ja passou da idade para o alistamento.')