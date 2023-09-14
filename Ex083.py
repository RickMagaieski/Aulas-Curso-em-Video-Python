conto = 0
contc = 0

quest = str(input("Digite uma expressão: "))

for run in quest:
    if run == '(':
        conto += 1
    elif run == ')':
        contc += 1

if conto == contc:
    print("Parabéns! Sua expressão é válida :)")
else:
    print("Sinto muito... Sua expressão não é válida :(")
