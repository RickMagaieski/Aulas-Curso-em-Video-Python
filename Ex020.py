from random import shuffle
no1 = str(input("Primeiro Aluno: "))
no2 = str(input("Segundo Aluno: "))
no3 = str(input("Terceiro Aluno: "))
no4 = str(input("Quarto Aluno: "))
lis = [no1, no2, no3, no4]
shuffle(lis)
print("A ordem de apresentação será a seguinte:\n{}".format(lis))
