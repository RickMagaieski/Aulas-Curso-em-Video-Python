numeros = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve'
           , 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')

void = ''

while True:
    di = int(input('Type a number between 0 and 20: '))
    print(void)
    if di < 0 or di > 21:
        print("Error, unknown command, try again!")
    else:
        print(f"You typed number \033[1m{numeros[di]}\033[m")
        break
