lista = []
for p in range(1, 6):
    pergunta = float(input(f"Digite o peso da {p}ª pessoa: "))
    lista += [pergunta]
print(f"O maior peso inserido foi {max(lista)}\nE o menor peso inserido foi {min(lista)}")
