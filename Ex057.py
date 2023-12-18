print()

while True:
    s = str(input("Digite o seu sexo: "))[0].upper()

    if s != "M" and s != "F":
        print("Digitacao incorreta, tente novamente...")
    else:
        print(f"Sexo {s} cadastrado com sucesso!")
        break
