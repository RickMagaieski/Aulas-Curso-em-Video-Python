#Tuplas são imutáveis

lanche = ("Hamburger", "Suco", "Pizza", "Pudim")

print("Eu vou comer:")

for c in lanche:
    print(f"{c}")


for pos, comida in enumerate(lanche):
    print(f"{comida} na posição {pos}")


for cont in range(0, len(lanche)):
    print(f"{lanche[cont]} na posição {cont}")


print(sorted(lanche))


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)  #Ele concatena(junta)
print(c.index(8))  #Ver a posição em que o número em questão está (primeira ocorrência)

print(c.index(5, 1)) #Para você ver se existe mais algum numero igual em uma posição diferente,
# você precisa colocar do lado uma posição a frente do que a primeira ocorrência está

print(c.count(5))  #Ver quantas vezes aparece o 5

del(b)  # apaga o bn