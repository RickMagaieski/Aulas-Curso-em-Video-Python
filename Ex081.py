count = 0
listy = []
void = ''

while True:
    listy.append(int(input("Digite um valor: ")))
    count += 1
    ques2 = str(input("Você quer continuar? [S/N] ")).upper()
    if ques2 == 'N':
        break
    if ques2 != 'S' and 'N':
        print("Comando Inválido!")
        break

listy.sort(reverse=True)

print(void)
print(f"Você digitou {count} valores.")
print(f"A lista dos valores em ordem crescente é esta: {listy}")
if 5 in listy:
    print("O valor 5 faz parte desta lista!")
else:
    print("O valor 5 não faz parte desta lista...")
