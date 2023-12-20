#Usando minha logica:



"""cont = 0
a = 1
b = 2
c = 3

n = int(input("Quantos termos voce quer mostrar? "))

print("0 --> 1 --> ", end="")

while cont < n - 2:

    print(f"{a} --> ", end='')

    cont += 1

    a = b
    b = c
    c = a + b

print("FIM")"""



#Melhor logica:



n = int(input("Quantos termos voce quer mostrar? "))
t1 = 0
t2 = 1

print(f"{t1} --> {t2} --> ", end="")

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f"{t3} --> ", end="")

    cont += 1
    t1 = t2
    t2 = t3

print("FIM", end="")
