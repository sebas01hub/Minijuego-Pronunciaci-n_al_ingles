import speech_recognition as sr

recog = sr.Recognizer()
mic = sr.Microphone()

def speech():
    with mic as source:
        recog.adjust_for_ambient_noise(source)
        print("Di la palabra...")
        audio = recog.listen(source)

    try:
        texto = recog.recognize_google(audio, language="en-US")
        return texto.lower()
    except sr.UnknownValueError:
        print("No se pudo entender.")
        return ""
    except sr.RequestError:
        print("Error con el reconocimiento de voz.")
        return ""
