n = str(input("Digite seu nome e sobrenome meu querido! "))
div1 = n.split()
div2 = n.split()
print("O seu primeiro nome é {}\nE o segundo é {}.".format((div1[0]), (div2[1])))
p = str(input("Essas informações estão corretas? "))
if p == 'sim'or p == 'Sim':
    print("Que bom! Seja bem vindo {}.".format(n))
else:
    print("Que pena! Por favor, tente novamente.")
