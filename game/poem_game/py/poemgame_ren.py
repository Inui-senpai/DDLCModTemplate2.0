# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл содержит код логики мини-игры на Python.

# Код логики был переписан с использованием подхода `_ren.py` для кода на Python.

# Чтобы просмотреть код Ren'Py, откройте файл `script-poemgame.rpy` в каталоге `poem_game`.

## Эти импорты не используются во время запуска игры, но нужны для того, чтобы IDE
## не выдавали кучу предупреждений.
from game.poem_game.py.poemgame_chibi_ren import chibis, chibi_s, chibi_n, chibi_y
from game.poem_game.py.poemwords_ren import poem_word_db, glitch_word, monika_word
from game.definitions.py.core_ren import persistent, store
import renpy  # type: ignore

poemwinner: dict[int, str] = {
    0: "sayori",
    1: "sayori",
    2: "sayori",
}

poemappeal: dict[str, dict[int, int]] = {
    "sayori": {0: 0, 1: 0, 2: 0},
    "natsuki": {0: 0, 1: 0, 2: 0},
    "yuri": {0: 0, 1: 0, 2: 0},
    "monika": {0: 0, 1: 0, 2: 0},
}

"""renpy
init python:
"""

POEM_CLICK_GLITCH_SOUND = store.audio.t4g
POEM_CLICK_SOUND = store.gui.activate_sound


class PoemGame:
    """
    Этот класс отвечает за логику мини-игры про сочинение стихотворений.
    """

    def __init__(self, testing: bool = False):
        """
        Инициализирует мини-игру со значениями по умолчанию.

        :param testing: Обход системы экранов и функций Ren'Py в целях тестирования. Не используется в DDLC. Используется системой GitHub Actions для проверки логики кода.
        :type testing: bool
        """
        self.played_baa = False
        self.poemgame_glitch = False
        self.poem_progress = 1

        self.testing = testing

    def reset(self):
        """
        Сбрасывает состояние мини-игры.
        """
        self.played_baa = False
        self.poemgame_glitch = False
        self.poem_progress = 1

    def start(self):
        """
        Запускает мини-игру.
        Этот метод должен вызываться для инициализации логики мини-игры.
        """
        self.reset()

        # Сбрасывает очки у всех персонажей.
        chibis.reset()

        wordList = poem_word_db.get_words()
        if len(wordList) == 0:
            raise ValueError(
                "В базе данных слов для стихотворения отсутствуют слова. Проверьте файл 'poemwords_ren.py' на наличие объявленных слов."
            )

        while self.poem_progress <= 20:
            random_words: list[str] = []
            for _ in range(10):
                try:
                    word = renpy.random.choice(wordList)
                except IndexError:
                    raise IndexError(
                        "В базе данных слов недостаточно слов. Добавьте ещё пару слов в файл 'poemwords_ren.py'."
                    )
                random_words.append(word.__str__())
                wordList.remove(
                    word
                )  # Удаляет слово во избежание появления дубликатов в ходе одного сеанса.

            # Показывает экран мини-игры со случайными словами.
            if self.testing:
                if renpy.persistent.playthrough == 2:
                    act_two_words = random_words[:9]
                    act_two_words.append(glitch_word.word)
                    poemword_str = renpy.random.choice(act_two_words)
                elif renpy.persistent.playthrough == 3:
                    act_three_words = []
                    for _ in range(10):
                        act_three_words.append(monika_word.word)
                    poemword_str = renpy.random.choice(act_three_words)
                else:
                    poemword_str = renpy.random.choice(random_words)
            else:
                poemword_str = renpy.call_screen(
                    "poem_test",
                    words=random_words,
                    progress=self.poem_progress,
                    poemgame_glitch=self.poemgame_glitch,
                )

            # Проверяем, есть ли слово в базе.
            if poemword_str in poem_word_db.get_words_str():
                selected_poemword = poem_word_db.get_word(poemword_str)
            else:
                if renpy.persistent.playthrough == 2:
                    selected_poemword = glitch_word
                else:
                    selected_poemword = monika_word

            if not self.testing:
                if not self.poemgame_glitch:
                    if selected_poemword.glitch_word:
                        self.poemgame_glitch = True
                        renpy.music.play(POEM_CLICK_GLITCH_SOUND)
                        renpy.show("white")
                        # renpy.show("y_sticker_glitch", at_list=[sticker_glitch], zorder=10)
                    elif persistent.playthrough != 3:
                        renpy.play(POEM_CLICK_SOUND)

                        # Акт 1
                        if persistent.playthrough == 0:
                            if selected_poemword.sPoint >= 3:
                                renpy.show("s_sticker hop")
                            elif selected_poemword.nPoint >= 3:
                                renpy.show("n_sticker hop")
                            elif selected_poemword.yPoint >= 3:
                                renpy.show("y_sticker hop")
                        else:
                            # Акт 2
                            if (
                                persistent.playthrough == 2
                                and store.chapter == 2
                                and renpy.random.randint(0, 10) == 0
                            ):
                                renpy.show(
                                    "m_sticker hop"
                                )  # Шанс 1/10, что Моника выпрыгнет из нижней части экрана.
                            elif selected_poemword.nPoint > selected_poemword.yPoint:
                                renpy.show(
                                    "n_sticker hop"
                                )  # Во втором акте, если у Нацуки больше очков, чем у Юри, то прыгает первая.
                            elif (
                                persistent.playthrough == 2
                                and not persistent.seen_sticker
                                and renpy.random.randint(0, 100) == 0
                            ):
                                renpy.show(
                                    "y_sticker hopg"
                                )  # "y_sticker_2g.png". Шанс 1/100, чтобы увидеть его, если ещё не видели.
                                renpy.persistent.seen_sticker = True
                            elif persistent.playthrough == 2 and store.chapter == 2:
                                renpy.show(
                                    "y_sticker_cut hop"
                                )  # Стикер Юри с изрезанными руками.
                            else:
                                renpy.show("y_sticker hop")
                else:
                    r = renpy.random.randint(
                        0, 10
                    )  # Шанс 1/10, чтобы услышать звук «ба-а».
                    if r == 0 and not self.played_baa:
                        renpy.play("gui/sfx/baa.ogg")
                        self.played_baa = True
                    elif r <= 5:
                        renpy.play(store.gui.activate_sound_glitch)

            chibi_s.add_points(selected_poemword.sPoint)
            chibi_n.add_points(selected_poemword.nPoint)
            chibi_y.add_points(selected_poemword.yPoint)
            self.poem_progress += 1

    def finish(self):
        """
        Завершает мини-игру.
        Этот метод должен вызываться для завершения работы логики мини-игры.
        """
        chapter = store.chapter

        if persistent.playthrough == 0:
            # Добавляет 5 очков той девушке, на сторону которой мы встали в первой главе первого акта.
            if chapter == 1:
                chibi = chibis.get_chibi(store.ch1_choice)
                chibi.add_points(5)

        # Определяет «победителя» мини-игры.
        if persistent.playthrough == 0:
            # Подсчёты первого акта.
            poemwinner[chapter] = max(
                chibis.chibis, key=lambda c: c.charPointTotal
            ).name
        else:
            # Подсчёты второго акта.
            if chibi_n.charPointTotal > chibi_y.charPointTotal:
                poemwinner[chapter] = "natsuki"
            else:
                poemwinner[chapter] = "yuri"

        # Добавляет привязку к «победителю» мини-игры.
        poemwinner_chibi = chibis.get_chibi(poemwinner[chapter])

        # Установка степени привязанности.
        if persistent.playthrough == 0 and poemwinner_chibi.name != "sayori":
            poemappeal["sayori"][chapter] += chibi_s.calculate_appeal()
        if poemwinner_chibi.name != "natsuki":
            poemappeal["natsuki"][chapter] += chibi_n.calculate_appeal()
        if poemwinner_chibi.name != "yuri":
            poemappeal["yuri"][chapter] += chibi_y.calculate_appeal()

        # «Победитель» мини-игры всегда получает +1 к привязанности.
        poemappeal[poemwinner_chibi.name][chapter] += 1


poem_game = PoemGame()


def get_appeal(chibi_name: str) -> int:
    """
    Возвращает степень привязанности указанного персонажа.

    :param chibi_name: Имя персонажа.
    :type chibi_name: str
    :return: Степень привязанности персонажа.
    :rtype: int
    """
    chibi = chibis.get_chibi(chibi_name)
    appeal = 0
    for a in poemappeal[chibi.name].values():
        appeal += a
    return appeal


def get_exclusive_scene(chapter: int) -> str:
    """
    Возвращает лейбл эксклюзивной сцены исходя из имени «победителя» и степени его привязанности.

    :param chapter: Номер текущей главы.
    :type chapter: int
    :return: Строка эксклюзивной сцены.
    :rtype: str
    """
    winner = chibis.get_chibi(poemwinner[chapter])
    name = winner.name

    # Во втором акте DDLC вместо Сайори подставлялась Юри,
    # так что и тут мы сделаем то же самое.
    if persistent.playthrough == 2 and winner.name == "sayori":
        name = "yuri"

    exclusive_scene = f"{name}_exclusive"
    if persistent.playthrough == 2:
        exclusive_scene += "2"
    exclusive_scene += f"_{get_appeal(name)}"
    return exclusive_scene


def get_monika_scene(chapter: int) -> str:
    """
    Возвращает лейбл сцены с Моникой исходя из номера главы.

    :param chapter: Номер текущей главы.
    :type chapter: int
    :return: Строка сцены с Моникой.
    :rtype: str
    """
    winner = chibis.get_chibi(poemwinner[chapter])
    monika_scene = "m"

    name = winner.name
    if persistent.playthrough == 2:
        monika_scene += "2"
        if winner.name == "sayori":
            name = "yuri"

    monika_scene += f"_{name}_{get_appeal(name)}"
    return monika_scene


def _character_poem_appeal_exists(character: str, chapter: int) -> bool:
    """
    Проверяет, существует ли значение привязанности у конкретного персонажа и главы.

    :param character: Имя персонажа в виде строки.
    :type character: str
    :param chapter: Номер главы в виде целого числа, отсчёт начинается с 1.
    :type chapter: int

    :return: True, если значение привязанности существует, в противном случае – False.
    :rtype: bool
    """

    if character not in poemappeal:
        return False

    if chapter not in poemappeal[character]:
        return False

    return True


def get_character_poem_appeal(character: str, chapter: int) -> int:
    """
    Возвращает значение привязанности конкретного персонажа и главы.

    :param character: Имя персонажа в виде строки.
    :type character: str
    :param chapter: Номер главы в виде целого числа, отсчёт начинается с 1.
    :type chapter: int

    :return: Значение привязанности в виде целого числа.
    :rtype: int

    :raises ValueError: Если персонаж и/или глава не были найдены в данных привязанности.
    """
    character = character.lower()
    chapter = chapter - 1  # Делает так, чтобы отсчёт глав начинался с нуля.
    if not _character_poem_appeal_exists(character, chapter):
        raise ValueError(
            f"Не удалось найти значение привязанности персонажа '{character}' и/или главы '{chapter}'."
        )

    return poemappeal[character][chapter]


def set_character_poem_appeal(character: str, chapter: int, value: int) -> None:
    """
    Задаёт значение привязанности конкретному персонажу в конкретной главе.

    :param character: Имя персонажа в виде строки.
    :type character: str
    :param chapter: Номер главы в виде целого числа, отсчёт начинается с 1.
    :type chapter: int
    :param value: Значение привязанности в виде целого числа.
    :type value: int

    :raises ValueError: Если персонаж и/или глава не были найдены в данных привязанности.
    """
    character = character.lower()
    chapter = chapter - 1  # Делает так, чтобы отсчёт глав начинался с нуля.

    if not _character_poem_appeal_exists(character, chapter):
        raise ValueError(
            f"Не удалось найти значение привязанности персонажа '{character}' и/или главы '{chapter}'."
        )

    poemappeal[character][chapter] = value
