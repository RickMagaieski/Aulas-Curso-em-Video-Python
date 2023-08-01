while True:
    print("\033[1mDIGITE 999 PARA ENCERRAR\033[m")
    soma = cont = 0
    while True:
        perg = int(input("Digite um número: "))
        if perg != 999:
            soma += perg
            cont += 1
        if perg == 999:
            print("\033[1mO programa foi encerrado. Dados inseridos:\033[m")
            print(f"{cont} números foram inseridos e a soma entre eles deu {soma}")
            break
    break
