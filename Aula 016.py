comidas = 'Hamburger', 'Suco', 'Sorvete', 'Batata Frita'

for cont in range(0, len(comidas)):
    print(f"Eu vouc comer {comidas[cont]}")

for p in comidas:
    print(f"Eu vou comer {p}")

for pos, comida in enumerate(comidas):
    print(f"Eu vou comer {comida} na posicao {pos}")
