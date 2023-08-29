from random import randint

numsort = []

for sort in range(1, 6):
    sr = randint(1, 10)
    numsort.append(sr)
tupla = tuple(numsort)

print(f"The sorted number was: {tupla}")
print(f"The lowest number was: {min(tupla)}")
print(f"The highest number was: {max(tupla)}")
