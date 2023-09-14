listy = []
ques2 = ''
void = ''

while True:
    ques = int(input("Digite um número: "))
    if ques not in listy:
        listy.append(ques)
    else:
        print("Valor já digitado anteriormente.")
    ques2 = str(input("Você quer continuar? [S/N] ")).upper()
    if ques2 == 'N':
        break
    if ques2 != 'S':
        print("Comando Inválido")
        break
print(void)
if ques2 == 'N':
    print(f"Você adicionou esses valores: {sorted(listy)}")
if ques2 != 'N' or 'Y':
    print("Programa Finalizado")
