# Importa a biblioteca para reconhecimento de voz
import speech_recognition as sr

# Importa a biblioteca de expressões regulares
import re

# Importa a biblioteca para síntese de voz (fala)
import pyttsx3

# Variável para armazenar o nome dito pelo usuário
nome = ""

# Inicia um loop infinito para escutar continuamente
while True:
    # Cria um reconhecedor de áudio
    mic = sr.Recognizer()

    # Usa o microfone como fonte de entrada
    with sr.Microphone() as source:
        # Inicializa o mecanismo de fala
        engine = pyttsx3.init()

        # Define a voz que será usada (neste caso, voz "Luciana" no macOS)
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")

        # Ajusta para ignorar ruídos do ambiente
        mic.adjust_for_ambient_noise(source)

        # Informa que o programa está pronto para ouvir
        print("Vamos começar, fale alguma coisa...")

        # Escuta o que foi falado no microfone
        audio = mic.listen(source)

        try:
            # Converte o áudio para texto usando o Google (idioma português)
            frase = mic.recognize_google(audio, language='pt-BR')

            # Verifica se a palavra "ajudar" foi dita
            if re.search(r'\bajudar\b', frase):
                engine.say("Ajuda")
                engine.runAndWait()
                print("Algo relacionado a ajuda.")

            # Verifica se a frase contém "meu nome é"
            elif re.search(r'\bmeu nome é\b', frase):
                # Captura o nome dito após "meu nome é"
                t = re.search(r'meu nome é (.*)', frase)
                nome = t.group(1)

                print("Seu nome é " + nome)

                # Fala o nome de volta para o usuário
                engine.say("Nome falado foi " + nome)
                engine.runAndWait()

            # Mostra o que o usuário falou
            print("Você falou: " + frase)

        # Caso o áudio não possa ser entendido, exibe uma mensagem de erro
        except sr.UnknownValueError:
            print("Ops, algo deu errado.")



