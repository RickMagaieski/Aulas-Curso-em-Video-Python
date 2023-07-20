from time import sleep

while True:
    valor1 = int(input("\033[1mDigite um valor qualquer: "))
    valor2 = int(input("Digite outro: \033[m"))
    sleep(0.5)
    escolha2 = 0
    while True:
        print("=-=" * 17)
        sleep(0.4)
        print("\033[1mO que você deseja fazer com os valores inseridos?\033[m")
        print("\033[1;37m[ 1 ] Somar\n[ 2 ] Subtrair\n[ 3 ] Multiplicar\n[ 4 ] Dividir \n[ 5 ] Mostrar o maior"
              "\n[ 6 ] Novos números\n[ 7 ] Sair\033[m")
        escolha = int(input("\033[1mDigite a opção escolhida: \033[m"))
        escolha2 = escolha
        sleep(0.5)
        if escolha == 1:
            print(f"\033[1;37mA soma de {valor1} + {valor2} é igual a {valor1 + valor2}\033[m")
            sleep(1.5)
        if escolha == 2:
            print(f"\033[1;37mA subtração de {valor1} - {valor2} é igual a {valor1 - valor2}\033[m")
            sleep(1.5)
        if escolha == 3:
            print(f"\033[1;37mA multiplicação de {valor1} X {valor2} é igual a {valor1 * valor2}\033[m")
            sleep(1.5)
        if escolha == 4:
            print("\033[1;37mA divisão de {} / {} é igual a {:.2f}\033[m".format(valor1, valor2, valor1/valor2))
            sleep(1.5)
        if escolha == 5:
            print(f"\033[1;37mO maior número entre esses dois números é o {max(valor1, valor2)}\033[m")
            sleep(1.5)
        if escolha == 6:
            break
        if escolha == 7:
            break
        if escolha > 7 and escolha != int:
            print("\033[1;37mComando Desconhecido, tente de novo!\033[m")
            sleep(1.5)
    if escolha2 == 7:
        print("\033[1;37mFechando o programa...\033[m")
        sleep(2)
        print("=-=" * 10)
        print("\033[1;37mPrograma Finalizado. Volte sempre!\033[m")
        break
    else:
        print("\033[1;37mDigite novamente!\033[m")
