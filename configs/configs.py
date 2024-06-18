API_ID: int = None
API_HASH: str = None

BOT_HYPERION_ID: int = 820567103
BOT_HYPERION_FIGHT_ID: int = 1102315510
BOT_CIRCLE_ID: int = 5672431343
CHAT_CIRCLE_ID: int = -1001423896138


class StartingTypeMoving():
    TYPE_NONE = "TYPE_NONE"
    "Отключённое авто-перемещение"
    "Можно не бояться банов."

    TYPE_TROLLEY = "TYPE_TROLLEY"
    "Перемещение, если у вас есть телега к кругу"
    "Считаю безопасным, но есть за что зацепиться, потому на свой страх и риск."

    TYPE_WALKING = "TYPE_WALKING"
    "Перемещение, если у вас нет телеги"
    "Крайне ленивая реализация, к использованию, если переживаете за аккаунт не советую."


text = """\n\n
Выберите одно из перечисленных, указав число:

0   TYPE_NONE = "TYPE_NONE"
    "Отключённое авто-перемещение"
    "Можно не бояться банов."

1   TYPE_TROLLEY = "TYPE_TROLLEY"
    "Перемещение, если у вас есть телега к кругу"
    "Считаю безопасным, но есть за что зацепиться, потому на свой страх и риск."

2   TYPE_WALKING = "TYPE_WALKING"
    "Перемещение, если у вас нет телеги"
    "Крайне ленивая реализация, к использованию, если переживаете за аккаунт не советую."

"""

TYPE_MOVING = None

while TYPE_MOVING not in ["0", "1", "2"]:
    TYPE_MOVING = input(text)
    
    if TYPE_MOVING == "0":
        TYPE_MOVING == StartingTypeMoving.TYPE_NONE
        print("Успешно.")
        break
    elif TYPE_MOVING == "1":
        TYPE_MOVING == StartingTypeMoving.TYPE_TROLLEY
        print("Успешно.")
        break        
    elif TYPE_MOVING == "2":
        TYPE_MOVING == StartingTypeMoving.TYPE_WALKING
        print("Успешно.")
        break
    else:
        print("\n\n-- Выберите из возможного! --\n\n")

