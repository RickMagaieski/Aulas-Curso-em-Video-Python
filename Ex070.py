from time import sleep

void = ''

print("-=" * 20)
print(" " * 10, "MAGAIESKI'S SHOP")
print("-=" * 20)
print(void)

produtos = []
produto2 = ''
menorv = []
cont1000 = 0
soma = 0.0
cont = 0


while True:
    produto = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o preço do produto: R$"))
    print(void)
    perg = str(input("Quer continuar a digitar [S/N]? ")).upper().strip()[0]
    print(void)

    soma += valor
    menorv.append(valor)
    produtos.append(produto)
    minimo = min(menorv)
    cont += 1

    if produto and valor == minimo:
        produto2 = produto
    if valor > 1000:
        cont1000 += 1
    if perg == "N":
        print(void)
        print("-=" * 10, "FIM DO PROGRAMA", "-=" * 10,"-")
        print(f"Foram comprados {cont} itens ao todo, os quais serão listados abaixo:")
        for item in produtos:
            print(f".{item}")
            sleep(1)
        print(f"O total da compra foi R${soma:.2f}")
        print(f"Temos {cont1000} produto(s) custando mais de R$1000.00")
        print(f"O produto mais barato foi o(a) {produto2} que custa R${minimo:.2f}")

        break
