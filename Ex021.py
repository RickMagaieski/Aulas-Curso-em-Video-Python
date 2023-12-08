import pygame

print()

print('=' * 20, "OPTIONS", '=' * 20)

print()

print("     [ 1 ] RESUME   [ 2 ] PAUSE   [ 3 ] EXIT")

print()

print('=' * 49)

pygame.init()
pygame.mixer.music.load("Ex021.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

print()

while pygame.mixer.music.get_busy():
    a = int(input("What you want to do? "))
    if a == 2:
        pygame.mixer.music.pause()
        p = int(input('Press 1 again to resume: '))
        if p == 1:
            pygame.mixer.music.unpause()
    elif a == 3:
        break
