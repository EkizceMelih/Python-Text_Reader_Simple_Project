from gtts import gTTS 
import os

text=open("speaking_txt.txt","r").read()

speech=gTTS(text=text, lang='en',slow = False)




speech.save("speaking1.mp3")
os.system("speaking1.mp3")