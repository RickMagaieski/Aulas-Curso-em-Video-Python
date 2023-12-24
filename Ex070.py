print("-=" * 15)
print("      MAGAIESKI'S SHOP")
print("-=" * 15)

mai = 0
men = 0
nom = []
maimil = 0
som = 0

print()

while True:

    print("-" * 22)
    pre = float(input("Preco do Produto: $"))
    nome = str(input("Nome do Produto: "))
    print("-" * 22)

    print()

    som += pre
    perg = str(input("Deseja continuar? [S/N] ")).upper()

    print()

    if mai == 0 and men == 0:
        mai = pre
        men = pre
    else:
        if pre > mai:
            mai = pre
        if pre < men:
            nom = nome
            men = pre

    if pre >= 1000:
        maimil += 1
    if perg == "N":
        break
    elif perg != "N" and perg != "S":
        print("Comando Incorreto... Tente novamente!")

print("------------- FIM DO PROGRAMA ------------")

print()

print(f"O total da compra foi ${som: .2f}")
print(f"Temos {maimil} produto(s) custando mais de $1000.00")
print(f"O produto mais barato foi {nom} custando ${men: .2f}")
