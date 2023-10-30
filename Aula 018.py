"""teste = list()
teste.append("Gustavo")
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera)"""


"""
void = ''
ecossistema = list()

for n in range(1, 4):
    nome = str(input("Digite o nome de um animal: "))
    habitat = str(input("Digite onde mora esse animal: "))

    ecossistema.append([nome, habitat])

    print(void)

print(ecossistema)"""


"""
galera = list()
dados = list()
void = ''
totmen = totmai = 0

for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))

    print(void)

    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade. Idade: {p[1]}")
        totmai += 1
    else:
        print(f"{p[0]} não é maior de idade. Idade: {p[1]}")
        totmen += 1

print(void)

print(f"Temos no total {totmai} maiores de idade e {totmen} menores de idade.")"""
