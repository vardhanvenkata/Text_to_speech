import pyttsx3 #Importing the pyttsx3 module

engine = pyttsx3.init()

say="Hello World i am vardhan"

engine.say(say)

engine.runAndWait()