from datetime import date
ano = int(input("Qual ano você deseja analisar? Digite 0 para saber se o ano atual é bissexto:"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é um ano BISSEXTO.")
else:
    print(f"O ano {ano} não é um ano BISSEXTO.")
