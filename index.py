import speech_recognition as sr
import re
import pyttsx3

def iniciar_assistente():
    # Inicializa o motor de voz apenas uma vez
    engine = pyttsx3.init()
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")  # Altere se estiver em outro sistema

    # Variável global para armazenar o nome
    nome = ""

    # Inicia o loop de escuta
    while True:
        reconhecedor = sr.Recognizer()

        with sr.Microphone() as fonte:
            reconhecedor.adjust_for_ambient_noise(fonte)
            print("Vamos começar, fale alguma coisa...")

            # Captura o áudio do usuário
            audio = reconhecedor.listen(fonte)

            try:
                # Converte o áudio para texto (em português)
                frase = reconhecedor.recognize_google(audio, language='pt-BR')

                # Verifica se o usuário quer ajuda
                if re.search(r'\bajudar\b', frase, re.IGNORECASE):
                    engine.say("Ajuda")
                    engine.runAndWait()
                    print("Algo relacionado a ajuda.")

                # Verifica se o usuário disse seu nome
                elif re.search(r'\bmeu nome é\b', frase, re.IGNORECASE):
                    t = re.search(r'meu nome é (.*)', frase, re.IGNORECASE)
                    if t:
                        nome = t.group(1)
                        print("Seu nome é " + nome)
                        engine.say("Nome falado foi " + nome)
                        engine.runAndWait()

                # Comando para encerrar o programa
                elif re.search(r'\bsair\b', frase, re.IGNORECASE):
                    print("Encerrando o assistente...")
                    engine.say("Até logo!")
                    engine.runAndWait()
                    break

                # Mostra a frase dita
                print("Você falou: " + frase)

            except sr.UnknownValueError:
                print("Ops, não consegui entender o que você disse.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

# Executa a função principal
iniciar_assistente()




