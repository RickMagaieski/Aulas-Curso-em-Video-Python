from random import randint
from time import sleep

while True:
    print("\033[1;37m=\033[m"*22, "\033[1mSeja muito bem vindo(a) a essa delicia de jogo!\033[m", "\033[1;37m=\033[m"*22)
    sleep(1.5)
    print("\033[1mAqui meu querido, eu vou escolher um número e você vai ter que adivinhar\033[m")
    sleep(2.5)
    for d in range(1, 4):
        print("\033[1m|\033[m")
    print("\033[1mV\033[m")
    sleep(1)
    print("\033[1mTu vai errar dms hahahaha\033[m")
    sleep(2)
    al = randint(1, 10)
    adv = int(input("\033[1mTente a sorte: \033[m"))
    cont = 1
    print("\033[1mVamos ver...\033[m")
    sleep(1.3)
    if adv == al:
        sleep(1.3)
        print("\033[1;32mFilho de uma mula descabelada!\033[m")
        sleep(1.3)
        print("\033[1;32mDe primeira! Parabéns fio(a)!!\033[m")
    while adv != al:
        if adv < al:
            print("\033[1;31mErrouuu! Vai de novo, só que agora tenta um número maior!\033[m")
            adv = int(input("\033[1mAcerta agora em: \033[m"))
            cont += 1
        else:
            print("\033[1;31mErrouuu! Vai de novo, só que agora tenta um número menor!\033[m")
            adv = int(input("\033[1mAcerta agora em: \033[m"))
            cont += 1
        if adv == al:
            print(f"\033[1;32mFinalmente... conseguiu depois de {cont} tentativas, parabéns kkkkk\033[m")
    if cont > 5:
        perg = str(input("\033[1mEai fio(a), quer tentar a sorte de novo depois disso kkkk? [S/N] \033[m")).upper()
        if perg == 'N':
            break
    else:
        perg = str(input("\033[1mFio(a), quer tentar a sorte de novo? [S/N] \033[m")).upper()
        if perg == 'N':
            break
