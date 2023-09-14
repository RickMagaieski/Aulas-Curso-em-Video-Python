listy = []
even = []
odd = []
void = ''

while True:
    ques = int(input("Digite um valor: "))
    ques2 = str(input("Você quer continuar? [S/N] ")).upper()
    listy.append(ques)
    if ques % 2 == 0:
        even.append(ques)
    if ques % 2 == 1:
        odd.append(ques)
    if ques2 == 'N':
        break
    if ques2 != 'S' and 'N':
        print("Comando Inválido!")
        break

print(void)
print(f"A lista original é essa: {listy}")
print(void)
print(f"A lista de números pares é esta: {even}")
print(f"E a lista de números ímpares é esta: {odd}")
