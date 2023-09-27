void = ''

print(f"{'='*50}")
print(f"{'THE MAGAIESKI SHOP':>34}")
print(f"{'='*50}")

print(void)

produtos = ('Bala', 0.50,
            'Chocolate', 12.09,
            'Caixa de Bombom', 15.34,
            'Tic Tac', 3.50,
            'Bolacha', 5.47,
            'Iogurte', 5.30,
            'Sorvete', 4.94,
            'Geladinho', 2.50,
            'Biscoito', 6.89,
            'Pirulito', 1.00)

for lis in range(0, len(produtos), 2):
    print(f"{produtos[lis]:.<42}{'R$'}", end=' ')
    print(f"{produtos[lis + 1]:>5.2f}")
print("=" * 50)
