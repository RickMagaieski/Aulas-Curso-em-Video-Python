# Solução proposta inicialmente:

frase = str(input("Digite algo: ")).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, - 1, - 1):
    inverso += junto[letra]
print(f"O inverso de {frase} é {inverso}")
if inverso == junto:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo.")


# solução mais simples:


"""def palindromo(frase):
    frase = frase.replace(' ', '')
    inverso = frase[::-1]
    if frase == inverso:
        print(f"O contrário da sua frase é {inverso}, ou seja: ")
        return True
    else:
        print(f"O contrário da sua frase é {inverso}, ou seja: ")
        return False


usuario = input("Digite algo: ").upper()
if palindromo(usuario):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo...")"""
