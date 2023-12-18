from time import sleep

while True:
    print()

    p = int(input("Primeiro valor: "))
    s = int(input("Segundo valor: "))

    print()
    o = 0

    print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do Programa")

    while True:
        print()

        op = int(input(">>> Sua Opcao: "))

        print()

        if op == 1:
            print(f"A soma entre {p} e {s} vai dar {p + s}")
        elif op == 2:
            print(f"A multiplicacao entre {p} e {s} vai dar {p * s}")
        elif op == 3:
            print(f"O maior numero dentre os dois e o numero {max(p, s)}")
        elif op == 4:
            break
        else:
            o = 2
            print("Finalizando Programa", end='')
            for p in range(1, 4):
                sleep(0.7)
                print(".", end='')
                sleep(0.7)
            break
    if o == 2:
        print('\n')
        print("Programa Finalizado")
        break
