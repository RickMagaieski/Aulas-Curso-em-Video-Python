tabela = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Fortaleza',
          'Atlético-MG', 'Cuibá', 'São Paulo', 'Cruzeiro', 'Corinthias', 'Internacional', 'Goias', 'Bahia', 'Santos',
          'Vasco', 'Coritiba', 'América-MG')

void = ''

tabelaordenada = sorted(tabela)

print(void)
print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print(f"Os ultimos 4 colocados são: {tabela[-4:]}")
print(void)
print("Time em ordem alfabética:")
for times in tabelaordenada:
    print(times)
print(void)
for loc, time in enumerate(tabela):
    if 'Chapecoense' in time:
        print(f"A chapecoense está na {loc}ª posição.")
        break
else:
    print('O time não foi encontrado.')

