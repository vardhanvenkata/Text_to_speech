import pyttsx3 #Importing the pyttsx3 module

engine = pyttsx3.init()

#say=input("Enter Something to say")
say="HI everyone"
engine.say(say)
engine.say("Hi Harsha")
engine.runAndWait()
