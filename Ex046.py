import pygame
from time import sleep
import sys

for i in range(10, -1, -1):
    pygame.mixer.init()
    pygame.mixer.music.load("Ex046 Bip.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()

    if i >= 7:
        sys.stdout.write(f"\033[1;32m\r {i}\033[m")
        sys.stdout.flush()
        sleep(1)
    elif i >= 4:
        sys.stdout.write(f"\033[1;33m\r {i}\033[m")
        sys.stdout.flush()
        sleep(1)
    else:
        sys.stdout.write(f"\033[1;31m\r {i}\033[m")
        sys.stdout.flush()
        sleep(1)
    while pygame.mixer.music.get_busy():
        pass

pygame.mixer.init()
pygame.mixer.music.load("Ex046 Boom.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()

print("\n\033[1;31mBOOOOOMMMMM!!!!\033[m")

while pygame.mixer.music.get_busy():
    pass
