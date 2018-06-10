import RPi.GPIO as GPIO
import os,pygame
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("Press Start button to read out the page")
flag=0
pause_flag=0
resume_flag=0
while True:
     button_state = GPIO.input(16)
     pause_button_state = GPIO.input(18)
     if button_state == False:
        flag=0
        pygame.mixer.init()
        pygame.mixer.music.load("Book-03-40-40.mp3")
        pygame.mixer.music.play()
         
     if (pause_button_state == False):
        if flag==0: 
           os.system("clear")
           print("Paused..")
           pygame.mixer.music.pause()
           flag=1
        elif flag==1:
           os.system("clear")
           print("Resumed..")
           pygame.mixer.music.unpause()
           flag=0
         

