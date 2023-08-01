maior = 0
menor = 9999
cont = 0
soma = 0
media = 0
while True:
    perg = int(input("Digite um número: "))
    perg2 = input("Deseja continuar? [S/N] ").upper()
    if perg != 0:
        cont += 1
    soma += perg
    media = soma / cont
    if perg > maior:
        maior = perg
    if perg != 0:
        if perg < menor:
            menor = perg
    if perg2 == 'N':
        print(f"Você digitou {cont} numeros e a média deles foi {media}")
        print(f"O maior valor foi {maior} e o menor valor foi {menor}")
        break
