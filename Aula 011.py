from random import randint
from time import sleep
print("\033[1;32m=\033[1;33m"*80)
print("\033[1;33mOlá, forasteiro! Eu sou a grande esfinge do Egito!!! Decifra-me ou eu te devoro!\033[m")
print("\033[1;32m=\033[1;33m"*80)
n = int(input("\033[1;33mTente a sorte. Escolha um número entre 0 e 5:\033[m "))
mix = randint(0, 5)
print("\033[1;32mEstou pensando...\033[m")
sleep(2)
if n == mix:
    print("\033[1;31mD\033[1;33mr\033[1;31mo\033[1;33mg\033[1;31ma\033[1;33m.\033[1;31m.\033[1;33m.\033[1;31m")
    sleep(1)
    print("\033[31mVocê acertou! Pode passar\033[m 😡!!")
else:
    print("\033[32mVOCÊ ERROU! Hahahahahah, agora eu irei te devorar!!!\033[m")
