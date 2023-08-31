numbers = []
void = ''
cont = 0
paircont = 0

for c in range(1, 5):
    quest = int(input("Digite um número: "))
    numbers.append(quest)
    if quest == 9:
        cont += 1
    if quest % 2 == 0:
        paircont += 1
tupla = tuple(numbers)
print(f"Você digitou esses números: {tupla}")
print(void)
print(f"O número 9 apareceu {cont} vezes")
if 3 in numbers:
    print(f"O primeiro 3 foi digitado na {numbers.index(3) + 1}ª posição")
else:
    print(f"Nenhum numero 3 foi digitado")
print(f"O número de números pares foi de {paircont}")
