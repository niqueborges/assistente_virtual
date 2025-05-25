# Importa a biblioteca de reconhecimento de voz
import speech_recognition as sr

# Importa a biblioteca de expressões regulares para buscar palavras específicas na fala
import re

# Cria um reconhecedor de voz
mic = sr.Recognizer()

# Usa o microfone como fonte de entrada de áudio
with sr.Microphone() as source:
    # Ajusta o reconhecimento para desconsiderar ruídos do ambiente
    mic.adjust_for_ambient_noise(source)

    # Solicita ao usuário que fale algo
    print("Por favor, diga algo:")

    # Escuta e grava o áudio falado pelo usuário
    audio = mic.listen(source)

    try:
        # Usa o serviço de reconhecimento de voz do Google para converter o áudio em texto
        frase = mic.recognize_google(audio, language="pt-BR")

        # Verifica se a frase contém alguma saudação
        if re.search(r'\b(oi|olá|e aí|fala)\b', frase, re.IGNORECASE):
            print("Olá! Como posso te ajudar hoje?")

        # Verifica se a frase contém alguma despedida
        elif re.search(r'\b(tchau|até logo|adeus)\b', frase, re.IGNORECASE):
            print("Tchau! Tenha um ótimo dia!")

        # Exibe a frase reconhecida
        print("Você disse: " + frase)

    # Caso o reconhecimento de voz falhe (áudio incompreensível), exibe uma mensagem
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")



