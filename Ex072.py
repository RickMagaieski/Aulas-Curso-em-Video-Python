numeros = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve'
           , 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')

void = ''

while True:
    di = int(input('Digite um número entre 0 e 20: '))
    print(void)
    if di < 0 or di > 21:
        print("Erro, comando desconhecido, tente novamente!")
    else:
        print(f"Você digitou o número \033[1m{numeros[di]}\033[m")
        break
