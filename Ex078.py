v = []

for p in range(0, 5):
    v.append(int(input(f"Digite um número para a posição {p}: ")))

print(f"Você digitou os seguintes valores: {v}")
print(f"O maior número foi o {max(v)} encontrado nas posições: {v.index(max(v))}...")
