from random import randint
from time import sleep
print("=-="*16)
print("Pensarei em um número entre 0 e 5... Tente acertar!")
print('=-='*16)
ri = randint(0, 5)
pergunta = int(input("Digite seu chute: "))
print("PROCESSANDO...")
sleep(2)
if pergunta == ri:
    print("Parabéns você acertou o número que eu estava pensando!")
else:
    print(f"GANHEI! Eu pensei no número {ri} e não no {pergunta}!")
