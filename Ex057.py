cont = 0
while cont == 0:
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper()
    if sexo != 'M' and sexo != 'F':
        print("Dados inválidos!")
    else:
        break
print("Dados cadastrados com sucesso!")