no = input("Qual o seu nome? ")
a = "="*15
b = "="*15
print(f"{a} Seja Bem Vindo {no}! {b}")
n = int(input("Digite um número: "))
print("De acordo com os cálculos aritiméticos {} será:\nQuando for o dobro: {}"
      "\nQuando for o triplo: {}\nQuando for raiz quadrada: {:.2f}".format(n, (n*2), (n*3), (n**(1/2))))
