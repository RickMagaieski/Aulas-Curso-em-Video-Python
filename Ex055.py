maior_peso = 0
menor_peso = 0
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f"O maior peso foi o de {maior_peso}Kg.")
print(f"E o menor peso foi o de {menor_peso}Kg.")

#solução alternativa

"""list = []
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    list.append(peso)
print(f"O maior peso digitado foi {max(list)}Kg\nE o menor foi {min(list)}Kg")"""
