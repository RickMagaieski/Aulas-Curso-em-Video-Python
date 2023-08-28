from random import randint

numsort = []
for sort in range(1, 5):
    sorteio = randint(1, 10)
    numsort.append(sorteio)
tupla = tuple(numsort)
print(f"O valores sorteados foram: {tupla}")
print(f'O menor valor foi {min(tupla)}')
print(f'O maior valor foi {max(tupla)}')
