num = (int(input("Digite um numero: ")),
       int(input("Digite outro numero: ")),
       int(input("Digite mais um numero: ")),
       int(input("Digite o ultimo numero: ")))

print()

print(f'Voce digitou os valores {num}')
print(f"O valor 9 aparaceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}a posicao")
else:
    print("O valor 3 nao foi digitado em nenhuma posicao")
print("Os valores pares digitados foram", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end='')
