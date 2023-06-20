from datetime import date
from time import sleep

print("Seja bem vindo ao consulta de alistamento online")
nasci = int(input("Digite o ano em que você nasceu: "))
ano = date.today().year
idade = ano - nasci
anoalis = nasci + 18  # o ano em que ira se alistar
quantfal = anoalis - ano  # quanto tempo falta para se alistar
quantoatras = ano - anoalis  # quanto tempo de atraso
if idade < 18:
    sleep(2)
    print(f"Você ainda possui {idade} anos de idade. Você ainda não precisa se alistar!")
    print(f"Seu alistamento so se dará daqui a {quantfal} ano(s), e será em {anoalis}.")
elif idade == 18:
    sleep(1)
    print(f"Você possui {idade} anos e você já pode ser alistar.")
    sleep(1)
    print(f"Se aliste o quanto antes!")
elif idade > 18:
    sleep(2)
    print(f"Você já possui {idade}. Você já devia ter se alistado!")
    print(f"A data normal do seu alistamento se deu em {anoalis}, você esta atrasado em {quantoatras} ano(s).")
else:
    print("Comando Desconhecido")
