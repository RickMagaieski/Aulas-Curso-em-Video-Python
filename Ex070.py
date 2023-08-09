from time import sleep

void = ''

print("-=" * 20)
print(" " * 10, "MAGAIESKI'S SHOP")
print("-=" * 20)
print(void)

produtos = ''
valorpq = 0
cont1000 = 0
soma = 0


while True:
    produto = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o preço do produto: R$"))
    print(void)
    perg = str(input("Quer continuar a digitar [S/N]? ")).upper().strip()[0]
    print(void)

    soma += valor
    valorpq.append(valor)

    if valorpq < 9999:
        produtos = produto
    if valor > 1000:
        cont1000 += 1
    if perg == "N":
        print(void)
        print("-=" * 10, "FIM DO PROGRAMA", "-=" * 10)
        print("O total da compra foi R${:.2f}".format(soma))
        print(f"Temos {cont1000} produto(s) custando mais de R$1000.00")
        print(f"O produto mais barato foi {produtos} que custa R${menor}")
        break
