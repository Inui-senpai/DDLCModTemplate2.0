# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл содержит код, управляющий отдельными частями мини-игры про обмен стихотворениями.

## Не используется в игре. Нужно только для того, чтобы IDE не выдавали кучу предупреждений.
readpoem: dict[str, bool] = {
    "sayori": False,
    "natsuki": False,
    "yuri": False,
    "monika": False,
}

"""renpy
init python:
"""


def get_read_poem_status(character: str) -> bool:
    """
    Возвращает статус прочтения стихотворения указанным персонажем.

    :param character: Имя персонажа в виде строки.
    :type character: str
    :return: Статус прочтения в виде логического значения.
    :rtype: bool

    :raises ValueError: Если персонаж не был найден в данных прочитанных стихов.
    """
    character = character.lower()
    if character not in readpoem:
        raise ValueError(f"Не удалось найти статус прочтения персонажа '{character}'.")

    return readpoem[character]


def set_read_poem_status(character: str) -> None:
    """
    Устанавливает статус прочтения стихотворения персонажем как ИСТИНА.

    :param character: Имя персонажа в виде строки.
    :type character: str

    :raises ValueError: Если персонаж не был найден в данных прочитанных стихов.
    """
    character = character.lower()
    if character not in readpoem:
        raise ValueError(f"Не удалось найти статус прочтения персонажа '{character}'.")

    readpoem[character] = True


def reset_read_poem_status() -> None:
    """
    Сбрасывает статус прочтения у всех персонажей в ЛОЖЬ.
    """
    for character in readpoem.keys():
        readpoem[character] = False
