from time import sleep
print("Bem vindo a sua conta do Itaú!")
codigo = "1234"
saldo = 2000
print("As opções disponíveis são essas:\nDeposito\nSaque\nSaldo Atual")
per = input("O que você deseja fazer? ")
if per == "deposito":
    cod = input("Certo. Para continuarmos, precisamos do seu código de ativação: ")
    if cod == codigo:
        print("Código correto!")
        print(f"Saldo atual: R${saldo}")
        per2 = input("Quanto gostaria de depositar? ")
        print("Certo!\nProcessando deposito, aguarde...")
        sleep(2)
        print("...")
        sleep(2)
        soma = saldo + float(per2)
        print("Deposito realizado com sucesso!")
        print("Agora o seu saldo atual é de R${:.2f}".format(soma))
    else:
        print("Código incorreto.")
elif per == "saque":
    cod2 = input("Certo. Para continuarmos, precisamos de seu código de ativação: ")
    if cod2 == codigo:
        print("Código correto!")
        print(f"Saldo atual: R${saldo}")
        saque = input("Quanto você gostaria de sacar? ")
        print("Aguarde... realizando operação.")
        conta = saldo - int(saque)
        if saldo < int(saque):
            print("Saldo insuficiente para realizar o saque.")
        else:
            sleep(4)
            print("Saque realizado com sucesso!\nSeu saldo agora é de R${:.2f}".format(conta))
    else:
        print("Código Incorreto.")
elif per == "saldo":
    cod3 = input("Certo. Para continuarmos, precisamos do seu código de ativação: ")
    if cod3 == codigo:
        print("Código correto!")
        print("Aguarde... acessando conta.")
        sleep(2)
        print(f"O saldo atual é de: R${saldo}")
    else:
        print("Código Incorreto.")
else:
    print("Operação Desconhecida.")
