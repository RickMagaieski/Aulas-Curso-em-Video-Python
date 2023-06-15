from random import choice
print("Aqui será sorteado quem apagará o quadro para o professor.")
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
l = [n1, n2, n3, n4]
print("O aluno(a) sorteado(a) foi {}".format(choice(l)))
