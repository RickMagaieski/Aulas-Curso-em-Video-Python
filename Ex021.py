import pygame

pygame.init()
pygame.mixer.music.load("Ex021.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

