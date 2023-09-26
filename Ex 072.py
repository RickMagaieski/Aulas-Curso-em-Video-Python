numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove","Dez", "Onze", "Doze",
           "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    n = 0

    for n in range(0, len(numeros)):
        if num == n:
            print(f"Você digitou o número {numeros[n]}")
        elif num >= len(numeros) or num < 0:
            print("Tente novamente!")
            break
    if n > 0:
        break
