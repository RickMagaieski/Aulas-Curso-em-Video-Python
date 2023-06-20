import time
s = 0
c = 0
impar = []
for p in range(1, 7):
    numero = int(input(f"Digite o {p}° número: "))
    if numero % 2 == 0:
        s += numero
        c += 1
    if numero % 2 != 0:
        impar.append(numero)
time.sleep(1)
print(f"Esse foi o resultado da soma dos {c} numeros pares foi {s}")
time.sleep(1)
print(f"Esses foram os números retirados por serem ímpares: {impar}")
