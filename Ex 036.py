from time import sleep
print("Bem Vindo ao Financiamentos Itaú!")
print("Financiamentos disponiveis:\n# Para Imóveis\n# Para Veiculos")
per1 = input("Qual tipo de empréstimo você gostaria de acessar? ")
if per1 == "imoveis":
    sleep(1)
    print("Certo. A opção de empréstimo de imóveis foi escolhida")
    imo = float(input("Qual é o valor da casa que você irá financiar? "))
    sal = float(input("Quanto você ganha? "))
    temp = int(input("Em quantos tempo você pretende financiar esse imóvel? "))
    prestacao = imo / (temp * 12)
    conta = sal * 30 / 100
    if conta <= prestacao:
        print("Para pagar por uma casa no valor R${} por {} anos, a prestação mensal será de R${:.2f}"
              .format(imo, temp, prestacao))
        sleep(1)
        print("Infelizmente o empréstimo foi NEGADO.")
    else:
        sleep(3)
        print("O seu financiamento foi APROVADO!")
        sleep(1)
        print("Você terá que pagar o valor mensal de R${:.2f} durante {} anos.".format(prestacao, temp))
elif per1 == "veiculos":
    sleep(1)
    print("Certo. A opção de empréstimo para veiculos foi escolhida")
    car = float(input("Qual será o valor do carro a ser financiado? "))
    sal = float(input("Quanto você ganha? "))
    temp = int(input("Em quanto tempo você pretende financiar esse carro? "))
    prestacao = car / (temp * 12)
    conta = sal * 25 / 100
    if conta <= prestacao:
        print("Para pagar um carro de R${} durante {} anos, as parcelas mensais seriam de R${:.2f}"
              .format(car, temp, prestacao))
        sleep(1)
        print("Por conta disso seu empréstimo foi NEGADO.")
    else:
        sleep(3)
        print("O seu empréstimo para o financiamento do carro foi APROVADO!")
        sleep(1)
        print("Você terá que pagar o valor mensal de R${:.2f} durante {} anos.".format(prestacao, temp))
else:
    print("Operação desconhecida.")
