from datetime import date

print()

n = int(input("Digite um ano para descobrir se ele é BISSEXTO\nOu digite 0 para saber sobre o ano atual: "))

print()
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f"O ano de {n} é um ano BISSEXTO!")
else:
    print(f"O ano de {n} não é um ano BISSEXTO...")
