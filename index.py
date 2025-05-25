import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)
    
    print("Please say something:")
    
    audio = mic.listen(source)
    
    try: 
        frase = mic.recognize_google(audio, language="pt-BR")
        print("You said: " + frase)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")