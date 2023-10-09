lista = [10, 12, 13, 43, 50, 21, 453, 102, 3]
print(f"O maior número da lista é o número {max(listan)}")
print(f"O menor número da lista é o número {min(listan)}")
listan.pop(3)
print(listan)


lista = list(range(4,11))
print(lista)



listan = [1, 5, 2, 10, 6, 3]
listan.sort(reverse=True)
print(listan)

numeros = [1, 5, 9, 10, 3]
numeros[3] = 4 # Vai adicionar um 4 na posição 3
numeros.append(21)
numeros.sort(reverse=True) #Vai girar a orientação ao contrário
numeros.insert(2, 0) #Vai inserir um 0 na posição 2
numeros.pop() #Elimina o ultima elemento. Ele vai eliminar algo especifico se você especificar a posição
numeros.remove(3) #Eliminará o numero em questão (não a posição, o numero ou palavra). Caso existam dois números iguais,
#ele irá remover o primeiro elemento que ele encontrar
print(numeros)
print(f"Essa lista de números tem {len(numeros)} elementos")

from random import randint

lista = [3, 3, 4, 3, 5]
for r in range(1, 7):
    lista.append(randint(1, 10))
    for re in lista:
        if 3 in lista:
            lista.remove(3) #Somente se tiver o 3 ele irá excluir
print(lista)

# Esse é um programa onde números aleatórios são gerados, nos quais qualquer número que aparecer 3 será eliminado



valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista")



valores = []
for v in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista")



a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f"Essa é a lista A: {a}")
print(f"Essa é a lista B: {b}")

# Quando você faz isso, você não está criando uma cópia, você está interligando ambas as listas!
# Já para criar uma cópia você precisa fazer isso: b = a[:]. Assim, todos os números de A estarão em B, ou uma cópia :)



num = [2, 5, 9, 1]
num[2] = 3   #Adiciona o numero 3 na posição 3
num.append(7)
num.sort(reverse=True)   #Inverte a lista
num.insert(2, 2)

#num.pop(2)   #Exclui o número na posição 2

if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4")

print(num)
print(f"Essa lista tem {len(num)} elementos")



valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print("Cheguei ao final da lista")"""
