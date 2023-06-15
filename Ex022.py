nome = str(input("Digite seu nom completo: ")).strip()
div = nome.split()
print("Seu nome em maiúsuculas é {}\nSeu nome em minúsculas é {}\nSeu nome tem {} letras\nE seu primeiro nome "
      "que é {} tem {} letras".format(nome.upper(), nome.lower(), len(nome)-nome.count(' '), div[0], nome.find(' ')))
