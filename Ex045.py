from time import sleep
import random
print(f"\033[1m{' JOKENPÔ VIRTUAL ':=^40}\033[m")
escolha = input("\033[1mFaça a sua jogada:\033[m ")
jokenpo = ["pedra", "tesoura", "papel"]
random.shuffle(jokenpo)
mistura = random.choice(jokenpo)
print("\033[0;33mJO\033[m")
sleep(0.8)
print("\033[0;32mKEN\033[m")
sleep(1)
print("\033[0;33mPO!\033[m")
if escolha == mistura:
    print(f"\033[0;37mEmpate... Você jogou \033[1;31m{escolha}\033[m\033[0;37m, e eu joguei \033[1;31m{mistura}\033[m"
          f".\033[0;37m Vamos tentar de novo!\033[m")
elif escolha == "papel" and mistura == "tesoura":
    print(f"\033[1mVocê escolheu \033[1;31m{escolha}\033[m\033[1m, e eu joguei \033[1;31m{mistura}"
          f"\033[m. \033[0;32mGANHEI!\033[m")
elif escolha == "tesoura" and mistura == "papel":
    print(f"\033[1mVocê escolheu \033[1;31m{escolha}\033[m,\033[1m e eu joguei \033[1;31m{mistura}"
          f"\033[m\033[1m... perdi...\033[m")
elif escolha == "pedra" and mistura == "papel":
    print(f"\033[1mVocê escolheu \033[1;31m{escolha}\033[m,\033[1m e eu joguei \033[1;31m{mistura}\033[m\033[1m. GANHEI!\033[m")
elif escolha == "papel" and mistura == "pedra":
    print(f"\033[1mVocê escolheu \033[1;31m{escolha}\033[m\033[1m, e eu joguei \033[1;31m{mistura}"
          f"\033[m\033[1m... perdi...\033[m")
elif escolha == "tesoura" and mistura == "pedra":
    print(f"\033[1mVocê escolheu \033[1;31m{escolha}\033[m,\033[1m e eu joguei \033[1;31m{mistura}\033[m\033[1m."
          f" GANHEI!\033[m")
elif escolha == "pedra" and mistura == "tesoura":
    print(f"\033[1mVocê escolheu \033[1;31m{escolha}\033[m,\033[1m e eu joguei \033[1;31m{mistura}"
          f"\033[m\033[1m... perdi...\033[m")
else:
    print("\033[7mUai, nada a ver essa jogada!\033[m")
