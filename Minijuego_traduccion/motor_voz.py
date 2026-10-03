import pyttsx3

rate = 130
volume = 1.0

def hablar(texto):
    engine = pyttsx3.init()

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(texto)
    engine.runAndWait()
    engine.stop()