times = ('Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Grêmio',
                 'Internacional', 'Cruzeiro', 'Atlético-MG', 'Botafogo', 'Fluminense',
                 'Santos', 'Vasco da Gama', 'Bahia', 'Sport', 'Fortaleza', 'Ceará',
                 'Chapecoense', 'Avaí', 'Goiás', 'Atlético-PR')

print()
print(f"Os cinco primeiros times sao: {times[:5]}")
print()
print(f"Os ultimos 4 colocados sao: {times[-4:]}")
print()
print(f"Os times em ordem alfabetica sao: {sorted(times)}")
print()
print(f"O Chapecoense esta na {times.index('Chapecoense') + 1}a posicao")
