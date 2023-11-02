from random import randint
from time import sleep

void = ''
random = randint(0, 5)

print(void)

print("\033[1m=\033[m" * 62)
print("\033[1m\033[34mEscolherei um número, tente advinhar em qual número eu pensei!\033[m")
print("\033[1m=\033[m" * 62)

print(void)

esc = int(input("\033[1mTente a sorte!\033[m "))

print(void)

print("\33[1mPROCESSANDO...\33[m")
sleep(1)

print(void)

if esc == random:
    print("\033[32mVocê acertou!!!\033[m")
else:
    print("\033[31mVocê errou!\033[m")
