import pygame
from time import sleep

print()

n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))

media = (n1 + n2) / 2

print()

if media < 5.0:
    print(f"Tirando {n1} e {n2}, a media do aluno e de {media}")
    sleep(1.5)
    print("Portanto voce foi...")
    sleep(2)

    print()

    pygame.init()
    pygame.mixer.music.load("Ex040.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    sleep(0.4)
    print('\033[1;31mRE\033[m', end='')
    sleep(0.3)
    print('\033[1;31mPRO\033[m', end='')
    sleep(0.3)
    print("\033[1;31mVA\033[m", end='')
    sleep(0.3)
    print("\033[1;31mDO!\033[m")

    while pygame.mixer.music.get_busy():
        pass

elif media >= 5.0 <= 6.9:
    print(f"Tirando {n1} e {n2}, a media do aluno e de {media}")
    sleep(1)
    print("Portanto...")
    sleep(1)
    print("Ficou de recuperacao! Estude mais da proxima...")

elif media >= 7:
    print(f"Tirando {n1} e {n2}, a media do aluno e de {media}!")
    sleep(0.6)
    print("PARABENS! Voce passou de ano!!")
