from random import shuffle, choice
pa = str(input("Primeiro Aluno: "))
sa = str(input("Segundo Aluno: "))
ta = str(input("Terceiro Aluno: "))
qa = str(input("Quarto Aluno: "))
lista = [pa, sa, ta, qa]
shuffle(lista)
print(f"O aluno escolhido foi: {choice(lista)}")
