from recognition import recognize_speech
from handlers import handle_command
from voice import speak

speak("Голосовой ассистент запущен. ")

while True:
    text = recognize_speech()
    if text:
        print(f"Вы сказали: {text}")
        response = handle_command(text)
        speak(response)
