import speech_recognition as sr
import asyncio

microfone = sr.Recognizer()
microfone.pause_threshold=0.8
microfone.dynamic_energy_threshold=True

assistente = "assistente"

def escuta2():
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source=source, duration=1)

        print("Diga: \n")
        audio = microfone.listen(source=source, phrase_time_limit=5)
        try:
            frase2 = microfone.recognize_google(audio, language="pt-BR")
            return frase2
        
        except sr.UnknownValueError:
            print("Desculpa")

def escuta():
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source=source, duration=0.5)

        print("\nEsperando")
        audio = microfone.listen(source=source, phrase_time_limit=5)
        try:
            frase1 = microfone.recognize_google(audio, language="pt-BR")
            if frase1.lower() == assistente:
                return escuta2()
        
        except sr.UnknownValueError:
            print("Desculpa")