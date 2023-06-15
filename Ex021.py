from pygame import mixer

mixer.init()
mixer.music.load("bh021.mp3")
mixer.music.set_volume(0.6)
mixer.music.play()
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    acao = input("")

    if acao == 'p':
        mixer.music.pause()
    elif acao == 'r':
        mixer.music.unpause()
    elif acao == 'e':
        mixer.music.stop()
        break
