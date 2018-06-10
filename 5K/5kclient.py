




from google.cloud import vision
from google.cloud.vision import types
import io,os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'VisionTest-561078e67aed.json'


# Instantiates a client
client = vision.ImageAnnotatorClient()


print("Reading the Image file. . .")
with io.open("foo.jpg", 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

print("Receiving response from Google API. . .")
response = client.document_text_detection(image=image)
labels = response.full_text_annotation

s=""
for i in labels.text.split():
    s+=i+" "
t=""
for i in s.split():
    #print(i)
    temp=i[0].upper()
    temp2=i[1:].lower()
    #print(temp)
    t+=temp+temp2+" "


from gtts import gTTS
  
print("Converting your text to sound . . .")
tts = gTTS(text=t, lang='en')
tts.save("voice.mp3")
print("Starting audio. . .")
os.system("omxplayer voice.mp3")
print("Thank You !!")


