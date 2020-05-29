#import gtts module for text to speech conversion
import gtts
#import os to start the audio file
import os

#Taking input from user to convert it into speech
myText = input("Enter text to convert into Speech")

#language we want to use--In this case en--stands for english
language ='en'

output = gtts.gTTS(text=myText, lang=language, slow=False)

#This is used to save the audio file
output.save("Speech.mp3")

#Play the converted file
os.system("start Speech.mp3")
