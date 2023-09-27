print(f"{'='*50}")
print(f"{'THE MAGAIESKI SHOP':>34}")
print(f"{'='*50}")

produtos = ('Papel', 20,
            'Caneta', 30,
            'Lápis', 40,
            'Borracha', 50,
            'Caderno', 60,
            'Mochila', 70)
for lis in produtos:
    if len(produtos) % 2 == 0:
        print(f"{lis}", end=' ')
    else:
        print(f"\n{lis}")
