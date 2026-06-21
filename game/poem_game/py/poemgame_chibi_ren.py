# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл содержит код трансформаций для анимации чибиков в мини-игре про сочинение стихотворений.

# Код адаптирован под Ren'Py 8 и использует подход `_ren.py` для кода на Python.

## Эти импорты не используются во время запуска игры, но нужны для того, чтобы IDE
## не выдавали кучу предупреждений.
from typing import Literal
import renpy  # type: ignore

"""renpy
init python:
"""


class ChibiTransform(object):
    """
    Этот класс отвечает за трансформации чибиков в мини-игре.
    """

    def __init__(self) -> None:
        """
        Инициализирует анимацию чибиков.
        """
        self.charTime: float = renpy.random.random() * 4 + 4
        self.charPos: int = 0
        self.charOffset: float = 0
        self.charZoom: float = 1

    def produce_random(self) -> float:
        """
        Генерирует случайное время для анимации персонажа.
        """
        return renpy.random.random() * 4 + 4

    def reset_trans(self) -> None:
        """
        Сбрасывает анимацию персонажа.
        """
        self.charTime = self.produce_random()
        self.charPos = 0
        self.charOffset = 0
        self.charZoom = 1

    def randomPauseTime(self, trans, st, at) -> Literal[None, 0]:
        """
        Случайным образом приостанавливает анимацию на заданный промежуток времени.
        """
        if st > self.charTime:
            self.charTime = self.produce_random()
            return None
        return 0

    def randomMoveTime(self, trans, st, at) -> Literal[None, 0]:
        """
        Случайным образом перемещает персонажа в зависимости от указанного времени.
        """
        if st > 0.16:
            if self.charPos > 0:
                self.charPos = renpy.random.randint(-1, 0)
            elif self.charPos < 0:
                self.charPos = renpy.random.randint(0, 1)
            else:
                self.charPos = renpy.random.randint(-1, 1)
            if trans.xoffset * self.charPos > 5:
                self.charPos *= -1
            return None
        if self.charPos > 0:
            trans.xzoom = -1
        elif self.charPos < 0:
            trans.xzoom = 1
        trans.xoffset += 0.16 * 10 * self.charPos
        self.charOffset = trans.xoffset
        self.charZoom = trans.xzoom
        return 0


class Chibi(ChibiTransform):
    """
    Этот класс определяет персонажа в мини-игре.
    """

    def __init__(
        self, name: str, poem_dislike_threshold: int = 29, poem_like_threshold: int = 45
    ) -> None:
        """
        Инициализирует персонажа.

        :param name: Имя персонажа.
        :param poem_dislike_threshold: Порог негативного отношения к слову в стихотворении.
        :param poem_like_threshold: Порог положительного отношения к слову в стихотворении.

        :type name: str
        :type poem_dislike_threshold: int
        :type poem_like_threshold: int
        """
        super().__init__()
        self.name = name
        self.poem_dislike_threshold = poem_dislike_threshold
        self.poem_like_threshold = poem_like_threshold

        self.charPointTotal = 0

    def reset(self) -> None:
        """
        Сбрасывает очки персонажа и его анимацию.
        """
        self.charPointTotal = 0
        self.reset_trans()

    def add_points(self, points: int) -> None:
        """
        Добавляет очки к счёту персонажа.

        :param points: Число добавляемых очков.
        :type points: int
        """
        self.charPointTotal += points

    def calculate_appeal(self) -> Literal[-1, 0, 1]:
        """
        Вычисляет степень привязанности персонажа исходя из его счёта.

        Если счёт ниже порога негативного отношения, привязанность будет равна -1.
        Если счёт выше порога положительного отношения, привязанность будет равна 1 и персонаж становится «победителем».
        Если же счёт оказался между обоими порогами, то привязанность будет равна 0.

        :return appeal: Степень привязанности персонажа.
        :rtype: int
        """
        if self.charPointTotal < self.poem_dislike_threshold:
            return -1
        elif self.charPointTotal > self.poem_like_threshold:
            return 1
        return 0

    def __call__(self) -> str:
        """
        Возвращает имя персонажа.
        """
        return self.name


class ChibiDB(object):
    """
    Этот класс определяет базу данных персонажей, используемых в мини-игре.
    """

    def __init__(self) -> None:
        """
        Инициализирует экземпляр ChibiDB с пустым списком персонажей.
        """
        self.chibis: list[Chibi] = []

    def add_chibi(self, name: str) -> None:
        """
        Добавляет персонажа в базу.

        :param name: Имя персонажа, которого надо добавить.

        :type name: str
        """
        self.chibis.append(Chibi(name))

    def get_chibi(self, name: str) -> Chibi:
        """
        Выдаёт персонажа по его имени.

        :param name: Имя персонажа, которого надо выдать.
        :type name: str
        :return: Экземпляр персонажа, если он есть в базе, в противном случае – None.
        :rtype: Chibi

        :raises ValueError: Если персонажа с указанным именем нет в базе.
        """
        for chibi in self.chibis:
            if chibi.name == name:
                return chibi

        raise ValueError(f"Персонажа '{name}' нет в базе данных.")

    def reset(self) -> None:
        """
        Сбрасывает состояние всех персонажей в базе.
        """
        for chibi in self.chibis:
            chibi.reset()


# Инициализирует базу данных и персонажей в мини-игре.

chibis = ChibiDB()
chibis.add_chibi("sayori")
chibis.add_chibi("natsuki")
chibis.add_chibi("yuri")

chibi_s = chibis.get_chibi("sayori")
chibi_n = chibis.get_chibi("natsuki")
chibi_y = chibis.get_chibi("yuri")
chibi_m = (
    ChibiTransform()
)  # Моника не участвует в мини-игре. Она только передвигается по экрану.
