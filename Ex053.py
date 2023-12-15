print()

frase = str(input("Digite uma frase qualquer: ")).upper()

sep = frase.split()
junt = ''.join(sep)
inver = ''

for p in range(len(junt) - 1, - 1, - 1):
    inver += junt[p]

if junt == inver:
    print("Essa frase e um pilindromo!")
else:
    print("Essa frase nao e um palindromo...")
