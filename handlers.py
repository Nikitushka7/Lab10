import requests
from commands import COMMANDS, text_data

def handle_command(command):
    command = command.lower()

    if "создать" in command:
        return create_text()

    elif "прочесть" in command:
        return read_text()

    elif "текст" in command:
        return print_text()

    else:
        return "Команда не распознана."

def create_text():
    try:
        response = requests.get("https://loripsum.net/api/10/short/headers")
        if response.status_code == 200:
            text_data["lorem"] = response.text
            return "Текст успешно создан."
        else:
            return "Ошибка при получении текста."
    except Exception:
        return "Ошибка запроса."

def read_text():
    if text_data["lorem"]:
        return text_data["lorem"][:400]
    else:
        return "Сначала создайте текст."

def print_text():
    if text_data["lorem"]:
        print(text_data["lorem"])
        return "Текст выведен в консоль."
    else:
        return "Текст не найден."