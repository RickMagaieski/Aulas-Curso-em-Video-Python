media = 0.0
cont = 0
void = ''
veio = 0
name = ''
for p in range(1, 5):
    print("―" * 5, f"{p}ª Pessoa", "―" * 5)
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M]/[F]: "))
    media += idade / 4

    if idade > veio and sexo == "M":
        veio = idade
        name = nome

    if sexo == "F" and idade < 20:
        cont += 1

print(void)
print(f"A média de idade do grupo é de {media} anos.")
print(f"O homem mais velho tem {veio} anos e se chama {name}")
print(f"Ao todo existe(em) {cont} mulher(es) com menos de 20 anos. ")
