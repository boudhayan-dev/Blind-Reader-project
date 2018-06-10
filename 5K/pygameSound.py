import pygame,os
pygame.mixer.init()
pygame.mixer.music.load("khalibali.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    if os.path.exists(os.getcwd()+"/hello.txt")==True:
        continue
    else:
        pygame.mixer.music.stop()
