import gtts
import os

myText = "Text To Speech Conversion Using Python"

language ='en'

output = gtts.gTTS(text=myText, lang=language, slow=False)

output.save("Speech.mp3")

os.system("start Speech.mp3")