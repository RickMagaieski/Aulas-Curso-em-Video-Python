from time import sleep

while True:
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper()
    if sexo != "F" and sexo != "M":
        print("Sexo Inválido!")
        sleep(0.5)
        print("Por favor, tente Novamente.")
        sleep(1)
    else:
        print("Dados Cadastrados com Sucesso!")
        break
