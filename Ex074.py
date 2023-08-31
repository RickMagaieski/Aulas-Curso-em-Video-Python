from random import randint

numsort = []

for sort in range(1, 6):
    sr = randint(1, 10)
    numsort.append(sr)
tupla = tuple(numsort)

print(f"Os números sorteados foram: {tupla}")
print(f"O menor número foi: {min(tupla)}")
print(f"O maior número foi: {max(tupla)}")
