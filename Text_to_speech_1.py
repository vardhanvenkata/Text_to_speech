import gtts 

tts = gtts.gTTS(text='Meeru', lang='en')
tts.save("hello.mp3")