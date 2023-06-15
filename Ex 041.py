from datetime import date
from time import sleep
print("Seja bem vindo ao sistema de categorias da CNN\n(Confederação Nacional de Natação)")
nascimento = int(input("Digite o ano no qual você nasceu: "))
data = date.today().year
conta = data - nascimento
if conta <= 9:
    print("= Até 9 anos =")
    sleep(1)
    print("A sua categoria é a categoria MIRIM.")
elif 9 < conta <= 14:
    print("=== Até 14 anos ===")
    sleep(1)
    print("A sua categria é a categoria INFANTIL.")
elif 14 < conta <= 19:
    print("==== Até 19 anos ====")
    sleep(1)
    print("A sua categoria é a categoria JÚNIOR.")
elif 19 < conta <= 25:
    print("*== Até 25 anos ==*")
    sleep(1)
    print("A sua categoria é a categoria SÊNIOR.")
elif 25 < conta <= 80:
    print("**== A cima de 25 ==**")
    sleep(1)
    print("A sua categoria é a categoria MASTER.")
elif conta <= 500:
    print("Ta de brincadeira comigo?")
else:
    print("Comando Desconhecido.")