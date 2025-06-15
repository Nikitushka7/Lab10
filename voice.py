import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('voice', 'ru')

def speak(text):
    engine.save_to_file(text, 'out.wav')
    engine.say(text)
    engine.runAndWait()