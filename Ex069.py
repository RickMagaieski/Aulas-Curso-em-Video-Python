from time import sleep

mulheres20 = homens = idademais18 = 0
void = ''

print("\033[1m=" * 20)
print(" " * 5, "CADASTRO")
print("=\033[m" * 20)

print(void)

while True:

    print("\033[1m-=\033[m" * 14)

    idade = int(input("\033[1mQual é a idade desta pessoa? \033[m"))
    sexo = str(input("\033[1mQual é o sexo desta pessoa? \033[m")).upper().strip()[0]

    print("\033[1m-=\033[m" * 14)

    print(void)

    perg = str(input("\033[1m#\033[m Quer cotinuar [S/N]? ")).upper().strip()

    print(void)

    if idade >= 18:
        idademais18 += 1
    if idade < 20 and sexo == 'F':
        mulheres20 += 1
    if sexo == 'M':
        homens += 1
    if perg == 'N':
        print(void)
        print("\033[4mDas pessoas cadastradas foram recolhidos os seguintes dados:\033[m")
        print(void)
        print(f"Existe(m) {idademais18} pessoa(s) com idade superior a 18 anos")
        print(f"Foi(ram) cadastrado(s) {homens} homem(ns) no total")
        print(f"Existe(m) {mulheres20} mulher(es) com a idade inferior a 20 anos")
        break
