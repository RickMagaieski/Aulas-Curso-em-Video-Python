s = 0
co = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        co += 1
print(f"A soma de todos os {co} valores será de {s} ")
