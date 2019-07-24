import speech_recognition as sr
speech=sr.Recognizer()
while True:
    
    with sr.Microphone() as source:
        print("say Something:")
        voice=speech.listen(source)
    
        try:
            
        
            text=speech.recognize_google(voice)
            print("you said :{}".format(text))
        except:
            print("sorry i couldnt here you"
