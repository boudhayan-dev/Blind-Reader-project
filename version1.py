import RPi.GPIO as GPIO
import time,os,pygame,datetime
from picamera import PiCamera
from google.cloud import vision
from google.cloud.vision import types
from gtts import gTTS


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'guru.json'
client = vision.ImageAnnotatorClient()
camera = PiCamera()
camera.resolution = (512,512)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
capture_button = GPIO.input(16)
pause_button = GPIO.input(18)
#pygame.init()    # -------->>> Uncomment this line in case there is problem with the sound playing part.
pygame.mixer.init()

print("Press Start button to read out the page")
flag=0


while True: 
    try:
        if capture_button == False:
            time.sleep(1)
            flag=0
           
            print('Button Pressed...')
            bookname="Book-"+datetime.datetime.now().strftime("%H-%M-%S")+".jpg"
            camera.start_preview()
            time.sleep(2)
            camera.capture(bookname)
            print("Image clicked . . .")

            with open(bookname, 'rb') as image_file:
                content = image_file.read()
            print("Sending Image to OCR . . ")
            
            image = types.Image(content=content)
            response = client.document_text_detection(image=image)
            labels = response.full_text_annotation
            s=""
            for i in labels.text.split():
            s+=i+" "
            t=""
            for i in s.split():
               temp=i[0].upper()
               temp2=i[1:].lower()
               t+=temp+temp2+" "
            print("\n"+t)
            
            print("Converting your text to sound . . .")
            tts = gTTS(text=t, lang='en')
            audioname="Book-"+datetime.datetime.now().strftime("%H-%M-%S")+".mp3"
            tts.save(audioname)
            print("Starting audio. . .")
            print("Press pause button to Pause/Resume")
            
            pygame.mixer.music.load(audioname)
            pygame.mixer.music.play()

        if (pause_button == False):
            time.sleep(1)
            if flag==0: 
                pygame.mixer.music.pause()
                flag=1
                print("Paused. . . ")
            elif flag==1:
                pygame.mixer.music.unpause()
                flag=0
                print("Resumed. . . ")

    except Exception as e:
        print(e)
        GPIO.cleanup()
        break