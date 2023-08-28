from time import sleep

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


a = (2, 3, 5)
b = (9, 12, 4, 5)
c = a + b

print(c)  #Ele concatena
print(c.index(5))  #Ver a posição
print(c.count(21))  #Ver se tem o 21, no caso

del(b)  # apaga o b

