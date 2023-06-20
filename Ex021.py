from pygame import mixer

mixer.init()
mixer.music.load("Ex021.mp3")
mixer.music.set_volume(0.6)
mixer.music.play()
while True:

    print("Pressione 'p' para pausar, 'r' para resumir.")
    print("Pressione 's' para sair do programa.")
    acao = input("")

    if acao == 'p':
        mixer.music.pause()
    elif acao == 'r':
        mixer.music.unpause()
    elif acao == 's':
        mixer.music.stop()
        break
