nome = str(input("Digite seu nome completo: ")).strip()
div = nome.split()
print(f"Seu nome em maiúsuculas é {nome.upper()}\nSeu nome em minúsculas é {nome.lower()}\nSeu nome tem "
      f"{len(nome)-nome.count(' ')} letras\nE o seu primeiro nome que é {div[0]} tem {nome.find(' ')} letras")
