numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze'
           , 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezeoito', 'Dezenove', 'Vinte')

void = ''

while True:
    di = int(input('Digite um número entre 0 e 20: '))
    print(void)
    if di < 0 or di > 21:
        print("Erro, comando desconhecido, tente de novo!")
    else:
        print(f"Você digitou o número \033[1m{numeros[di]}\033[m")
        break
