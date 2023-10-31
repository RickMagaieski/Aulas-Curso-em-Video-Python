import random
pa = str(input("Primeiro Aluno: "))
sa = str(input("Segundo Aluno: "))
ta = str(input("Terceiro Aluno: "))
qa = str(input("Quarto Aluno: "))
lista = [pa, sa, ta, qa]
print(f"O aluno escolhido foi: {random.choice(lista)}")
