som = 0
mai = 0
men = 0
cont = 0

while True:

    print()

    n = int(input("Digite um numero: "))
    o = ''

    if mai == 0 and men == 0:
        mai = n
        men = n
    else:
        if n > mai:
            mai = n
        if n < men:
            men = n

    cont += 1
    som += n
    med = som / cont

    while True:
        perg = str(input("Quer continuar ? [S/N] "))[0].upper()

        if perg == "N":
            o = 'N'
            break
        elif perg != "S" and "N":
            print("Comando Desconhecido. Tente novamente!")
        elif perg == "S":
            break

    if o == 'N':
        break

print()

print(f"Voce digitou {cont} numeros cuja media foi de {med}")
print(f"O maior valor foi {mai} e menor valor foi {men}")
