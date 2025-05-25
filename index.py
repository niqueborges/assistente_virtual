# Importa a biblioteca de reconhecimento de voz
import speech_recognition as sr

# Importa a biblioteca de expressões regulares
import re

while(True):

    # Cria um objeto reconhecedor, responsável por processar o áudio
    mic = sr.Recognizer()

    # Usa o microfone como fonte de entrada de áudio
    with sr.Microphone() as source:
        # Ajusta o reconhecimento para ignorar ruídos do ambiente
        mic.adjust_for_ambient_noise(source)
        
        print("Por favor, diga algo:")

        # Escuta o que foi falado no microfone
        audio = mic.listen(source)
        
        try:

            frase = mic.recognize_google(audio,language='pt-BR')



            if (re.search(r'\b' + "ajudar" + r'\b',format(frase))):

                print("Algo relacionado a ajuda.")



            elif (re.search(r'\b' + "meu nome é " + r'\b',format(frase))):

                t = re.search('meu nome é (.*)',format(frase))

                nome = t.group(1)

                print("Seu nome é "+nome)

        # Caso não consiga entender o áudio, exibe uma mensagem de erro
        except sr.UnknownValueError:
            print("Desculpe, não consegui entender o que você disse.")
