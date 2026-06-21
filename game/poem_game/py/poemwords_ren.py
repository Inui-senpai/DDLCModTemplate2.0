# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл содержит код Python для привязки слов к персонажам в мини-игре про сочинение стихотворений.

# Данный файл заменяет оригинальный файл `poemwords.txt` и определяет слова, используемые в мини-игре,
# эксплуатируя структуру классов Python вместе с подходом `_ren.py` в Ren'Py 8 для кода на Python.

"""renpy
init python:
"""


class PoemWord:
    """
    Класс, представляющий слово в мини-игре.
    """

    def __init__(
        self,
        word: str,
        sayori_points: int,
        natsuki_points: int,
        yuri_points: int,
        glitch_word: bool = False,
    ):
        """
        Инициализирует экземпляр класса PoemWord.

        :param word: Само слово.
        :param sayori_points: Сколько очков это слово даст Сайори.
        :param yuri_points: Сколько очков это слово даст Юри.
        :param natsuki_points: Сколько очков это слово даст Нацуки.
        :param glitch_word: Является ли это слово искажением.

        :type word: str
        :type sayori_points: int
        :type yuri_points: int
        :type natsuki_points: int
        :type glitch_word: bool

        :raises ValueError: Если какая-то из прибавок отрицательная.
        """
        self.word = word

        if sayori_points < 0 or yuri_points < 0 or natsuki_points < 0:
            if sayori_points < 0:
                raise ValueError("Очки привязанности Сайори должны быть от 0 и выше.")
            elif yuri_points < 0:
                raise ValueError("Очки привязанности Юри должны быть от 0 и выше.")
            elif natsuki_points < 0:
                raise ValueError("Очки привязанности Нацуки должны быть от 0 и выше.")

        self.sPoint = sayori_points
        self.yPoint = yuri_points
        self.nPoint = natsuki_points
        self.glitch_word = glitch_word

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса PoemWord.

        :return str: Искомое слово.
        """
        return self.word


class PoemWordDB:
    """
    Класс, отвечающий за базу данных слов, используемых в мини-игре.
    """

    def __init__(self):
        """
        Инициализирует экземпляр класса PoemWordDB с пустым списком слов.
        """
        self.words: list[PoemWord] = []

    def add_word(
        self,
        word: str,
        sayori_points: int,
        natsuki_points: int,
        yuri_points: int,
        glitch_word: bool = False,
    ):
        """
        Добавляет новое слово в базу данных PoemWord.

        :param word: Слово, которое нужно добавить.
        :param sayori_points: Сколько очков это слово даст Сайори.
        :param yuri_points: Сколько очков это слово даст Юри.
        :param natsuki_points: Сколько очков это слово даст Нацуки.
        :param glitch_word: Является ли это слово искажением.

        :type word: str
        :type sayori_points: int
        :type yuri_points: int
        :type natsuki_points: int
        :type glitch_word: bool

        :raises ValueError: Если какая-то из прибавок отрицательная.
        """
        new_word = PoemWord(
            word, sayori_points, natsuki_points, yuri_points, glitch_word
        )
        self.words.append(new_word)

    def get_words(self):
        """
        Возвращает список слов в базе данных PoemWord.

        :return list[PoemWord]: Список экземпляров класса PoemWord.
        """
        return self.words.copy()

    def get_words_str(self) -> list[str]:
        """
        Возвращает список слов в базе данных PoemWord в виде строк.

        :return list[str]: Список слов в виде строк.
        """
        return [word.word for word in self.words]

    def get_word(self, word: str) -> PoemWord:
        """
        Выдаёт слово из базы данных PoemWord по его строковому представлению.

        :param word: Искомое слово.
        :type word: str
        :return: Экземпляр класса PoemWord, если такое слово есть.
        :rtype: PoemWord

        :raises ValueError: Если такого слова нет в базе данных.
        """
        for poem_word in self.words:
            if poem_word.word == word:
                return poem_word

        raise ValueError(f"Слово '{word}' не было найдено в базе данных слов для мини-игры.")


## Добавляет слова в базу данных.
poem_word_db = PoemWordDB()

## Искажённое слово
glitch_word = PoemWord("", 0, 0, 0, glitch_word=True)  # Строка намеренно оставлена пустой
## Слово «Моника»
monika_word = PoemWord("", 0, 0, 0)  # Строка намеренно оставлена пустой

## Слова Сайори
poem_word_db.add_word("счастье", 3, 2, 1)
poem_word_db.add_word("печаль", 3, 2, 1)
poem_word_db.add_word("смерть", 3, 1, 2)
poem_word_db.add_word("трагедия", 3, 1, 2)
poem_word_db.add_word("одиночество", 3, 1, 2)
poem_word_db.add_word("любовь", 3, 2, 1)
poem_word_db.add_word("приключение", 3, 2, 1)
poem_word_db.add_word("сладкий", 3, 2, 1)
poem_word_db.add_word("ажиотаж", 3, 2, 1)
poem_word_db.add_word("фейерверк", 3, 2, 1)
poem_word_db.add_word("романтика", 3, 2, 1)
poem_word_db.add_word("слёзы", 3, 1, 2)
poem_word_db.add_word("депрессия", 3, 1, 2)
poem_word_db.add_word("сердце", 3, 2, 1)
poem_word_db.add_word("свадьба", 3, 2, 1)
poem_word_db.add_word("страсть", 3, 2, 1)
poem_word_db.add_word("детство", 3, 2, 1)
poem_word_db.add_word("радость", 3, 2, 1)
poem_word_db.add_word("цвет", 3, 2, 1)
poem_word_db.add_word("надежда", 3, 1, 2)
poem_word_db.add_word("друзья", 3, 2, 1)
poem_word_db.add_word("семья", 3, 2, 1)
poem_word_db.add_word("вечеринка", 3, 2, 1)
poem_word_db.add_word("каникулы", 3, 2, 1)
poem_word_db.add_word("лень", 3, 2, 1)
poem_word_db.add_word("грёзы", 3, 1, 2)
poem_word_db.add_word("боль", 3, 1, 2)
poem_word_db.add_word("праздник", 3, 2, 1)
poem_word_db.add_word("кровать", 3, 2, 1)
poem_word_db.add_word("перо", 3, 2, 1)
poem_word_db.add_word("стыд", 3, 1, 2)
poem_word_db.add_word("страх", 3, 1, 2)
poem_word_db.add_word("теплота", 3, 2, 1)
poem_word_db.add_word("цветок", 3, 2, 1)
poem_word_db.add_word("уют", 3, 2, 1)
poem_word_db.add_word("танец", 3, 2, 1)
poem_word_db.add_word("пение", 3, 2, 1)
poem_word_db.add_word("крик", 3, 1, 2)
poem_word_db.add_word("смех", 3, 2, 1)
poem_word_db.add_word("тьма", 3, 1, 2)
poem_word_db.add_word("солнечный", 3, 2, 1)
poem_word_db.add_word("тучи", 3, 2, 1)
poem_word_db.add_word("покой", 3, 1, 2)
poem_word_db.add_word("глупый", 3, 2, 1)
poem_word_db.add_word("летающий", 3, 2, 1)
poem_word_db.add_word("чудесный", 3, 2, 1)
poem_word_db.add_word("безответный", 3, 1, 2)
poem_word_db.add_word("роза", 3, 1, 2)
poem_word_db.add_word("вместе", 3, 2, 1)
poem_word_db.add_word("обещание", 3, 2, 1)
poem_word_db.add_word("обаяние", 3, 2, 1)
poem_word_db.add_word("красота", 3, 2, 1)
poem_word_db.add_word("приободрение", 3, 2, 1)
poem_word_db.add_word("улыбка", 3, 2, 1)
poem_word_db.add_word("сломанный", 3, 1, 2)
poem_word_db.add_word("дорогой", 3, 2, 1)
poem_word_db.add_word("молитва", 3, 1, 2)
poem_word_db.add_word("неуклюжий", 3, 2, 1)
poem_word_db.add_word("прощение", 3, 1, 2)
poem_word_db.add_word("природа", 3, 2, 1)
poem_word_db.add_word("океан", 3, 2, 1)
poem_word_db.add_word("очаровывать", 3, 2, 1)
poem_word_db.add_word("особый", 3, 2, 1)
poem_word_db.add_word("музыка", 3, 2, 1)
poem_word_db.add_word("счастливый", 3, 2, 1)
poem_word_db.add_word("неудача", 3, 1, 2)
poem_word_db.add_word("громкий", 3, 2, 1)
poem_word_db.add_word("мирный", 3, 1, 2)
poem_word_db.add_word("веселье", 3, 1, 2)
poem_word_db.add_word("закат", 3, 2, 1)
poem_word_db.add_word("светлячки", 3, 2, 1)
poem_word_db.add_word("радуга", 3, 2, 1)
poem_word_db.add_word("обида", 3, 1, 2)
poem_word_db.add_word("играть", 3, 2, 1)
poem_word_db.add_word("блеск", 3, 2, 1)
poem_word_db.add_word("шрамы", 3, 1, 2)
poem_word_db.add_word("пустой", 3, 1, 2)
poem_word_db.add_word("удивительный", 3, 2, 1)
poem_word_db.add_word("горе", 3, 1, 2)
poem_word_db.add_word("объятия", 3, 1, 2)
poem_word_db.add_word("необычайный", 3, 2, 1)
poem_word_db.add_word("потрясающий", 3, 2, 1)
poem_word_db.add_word("поражение", 3, 1, 2)
poem_word_db.add_word("безнадёжный", 3, 1, 2)
poem_word_db.add_word("страдание", 3, 1, 2)
poem_word_db.add_word("сокровище", 3, 2, 1)
poem_word_db.add_word("блаженство", 3, 2, 1)
poem_word_db.add_word("воспоминания", 3, 2, 1)

## Слова Нацуки
poem_word_db.add_word("милый", 2, 3, 1)
poem_word_db.add_word("пушистый", 2, 3, 1)
poem_word_db.add_word("чистый", 1, 3, 2)
poem_word_db.add_word("конфеты", 2, 3, 1)
poem_word_db.add_word("покупки", 2, 3, 1)
poem_word_db.add_word("щенок", 2, 3, 1)
poem_word_db.add_word("котёнок", 2, 3, 1)
poem_word_db.add_word("облака", 2, 3, 1)
poem_word_db.add_word("помада", 1, 3, 2)
poem_word_db.add_word("парфе", 2, 3, 1)
poem_word_db.add_word("клубника", 2, 3, 1)
poem_word_db.add_word("розовый", 2, 3, 1)
poem_word_db.add_word("шоколад", 2, 3, 1)
poem_word_db.add_word("сердцебиение", 1, 3, 2)
poem_word_db.add_word("поцелуй", 1, 3, 2)
poem_word_db.add_word("мелодия", 2, 3, 1)
poem_word_db.add_word("бантик", 2, 3, 1)
poem_word_db.add_word("резвый", 2, 3, 1)
poem_word_db.add_word("тук-тук", 2, 3, 1)
poem_word_db.add_word("кавайный", 2, 3, 1)
poem_word_db.add_word("юбка", 2, 3, 1)
poem_word_db.add_word("щёки", 2, 3, 1)
poem_word_db.add_word("е-мейл", 2, 3, 1)
poem_word_db.add_word("липкий", 2, 3, 1)
poem_word_db.add_word("энергичный", 2, 3, 1)
poem_word_db.add_word("блестящий", 2, 3, 1)
poem_word_db.add_word("грызть", 2, 3, 1)
poem_word_db.add_word("фантазия", 1, 3, 2)
poem_word_db.add_word("сахар", 2, 3, 1)
poem_word_db.add_word("хихикать", 2, 3, 1)
poem_word_db.add_word("зефир", 2, 3, 1)
poem_word_db.add_word("скакать", 2, 3, 1)
poem_word_db.add_word("классики", 2, 3, 1)
poem_word_db.add_word("мир", 2, 3, 1)
poem_word_db.add_word("вращение", 2, 3, 1)
poem_word_db.add_word("вертеть", 2, 3, 1)
poem_word_db.add_word("леденец", 2, 3, 1)
poem_word_db.add_word("пуф", 2, 3, 1)
poem_word_db.add_word("пузырьки", 2, 3, 1)
poem_word_db.add_word("шёпот", 2, 3, 1)
poem_word_db.add_word("лето", 2, 3, 1)
poem_word_db.add_word("водопад", 1, 3, 2)
poem_word_db.add_word("купальник", 2, 3, 1)
poem_word_db.add_word("ваниль", 2, 3, 1)
poem_word_db.add_word("наушники", 2, 3, 1)
poem_word_db.add_word("игры", 2, 3, 1)
poem_word_db.add_word("носки", 2, 3, 1)
poem_word_db.add_word("волосы", 2, 3, 1)
poem_word_db.add_word("песочница", 2, 3, 1)
poem_word_db.add_word("пижама", 1, 3, 2)
poem_word_db.add_word("одеяло", 1, 3, 2)
poem_word_db.add_word("молоко", 2, 3, 1)
poem_word_db.add_word("губки", 2, 3, 1)
poem_word_db.add_word("злость", 2, 3, 1)
poem_word_db.add_word("папа", 2, 3, 1)
poem_word_db.add_word("валентинка", 2, 3, 1)
poem_word_db.add_word("мышь", 1, 3, 2)
poem_word_db.add_word("свист", 2, 3, 1)
poem_word_db.add_word("жмяк", 2, 3, 1)
poem_word_db.add_word("кролик", 2, 3, 1)
poem_word_db.add_word("аниме", 2, 3, 1)
poem_word_db.add_word("прыгать", 2, 3, 1)

## Слова Юри
poem_word_db.add_word("решимость", 1, 1, 3)
poem_word_db.add_word("самоубийство", 2, 1, 3)
poem_word_db.add_word("воображение", 2, 1, 3)
poem_word_db.add_word("скрытный", 2, 1, 3)
poem_word_db.add_word("жизненность", 1, 1, 3)
poem_word_db.add_word("существование", 2, 1, 3)
poem_word_db.add_word("сверкающий", 1, 1, 3)
poem_word_db.add_word("багровый", 1, 1, 3)
poem_word_db.add_word("вихрь", 1, 1, 3)
poem_word_db.add_word("послеобраз", 1, 1, 3)
poem_word_db.add_word("головокружение", 1, 1, 3)
poem_word_db.add_word("дезориентация", 1, 1, 3)
poem_word_db.add_word("сущность", 2, 1, 3)
poem_word_db.add_word("атмосфера", 2, 1, 3)
poem_word_db.add_word("небосвод", 2, 1, 3)
poem_word_db.add_word("смятение", 1, 1, 3)
poem_word_db.add_word("загрязнение", 1, 1, 3)
poem_word_db.add_word("интеллектуальный", 1, 1, 3)
poem_word_db.add_word("анализ", 1, 1, 3)
poem_word_db.add_word("энтропия", 1, 1, 3)
poem_word_db.add_word("оживлённый", 1, 1, 3)
poem_word_db.add_word("сверхъестественный", 2, 1, 3)
poem_word_db.add_word("несовместимый", 1, 1, 3)
poem_word_db.add_word("гнев", 2, 1, 3)
poem_word_db.add_word("ниспосланный", 2, 1, 3)
poem_word_db.add_word("бойня", 2, 1, 3)
poem_word_db.add_word("философия", 1, 1, 3)
poem_word_db.add_word("непостоянный", 1, 1, 3)
poem_word_db.add_word("настойчивый", 1, 1, 3)
poem_word_db.add_word("аура", 2, 1, 3)
poem_word_db.add_word("неустойчивый", 1, 1, 3)
poem_word_db.add_word("инферно", 2, 1, 3)
poem_word_db.add_word("неспособный", 2, 1, 3)
poem_word_db.add_word("судьба", 2, 1, 3)
poem_word_db.add_word("непогрешимый", 1, 1, 3)
poem_word_db.add_word("мучительный", 2, 1, 3)
poem_word_db.add_word("расхождение", 1, 1, 3)
poem_word_db.add_word("неконтролируемый", 2, 1, 3)
poem_word_db.add_word("экстремальный", 1, 1, 3)
poem_word_db.add_word("убегать", 2, 1, 3)
poem_word_db.add_word("мечта", 2, 2, 3)
poem_word_db.add_word("катастрофа", 2, 1, 3)
poem_word_db.add_word("живописный", 2, 1, 3)
poem_word_db.add_word("пышущий", 1, 2, 3)
poem_word_db.add_word("вопрос", 1, 2, 3)
poem_word_db.add_word("нагноение", 2, 1, 3)
poem_word_db.add_word("предосуждение", 1, 1, 3)
poem_word_db.add_word("клетка", 1, 2, 3)
poem_word_db.add_word("взрываться", 1, 2, 3)
poem_word_db.add_word("наслаждение", 1, 2, 3)
poem_word_db.add_word("похоть", 1, 2, 3)
poem_word_db.add_word("ощущение", 1, 2, 3)
poem_word_db.add_word("кульминация", 1, 2, 3)
poem_word_db.add_word("электричество", 1, 2, 3)
poem_word_db.add_word("отрекаться", 1, 1, 3)
poem_word_db.add_word("презирать", 2, 1, 3)
poem_word_db.add_word("бесконечный", 2, 1, 3)
poem_word_db.add_word("вечность", 2, 1, 3)
poem_word_db.add_word("время", 2, 1, 3)
poem_word_db.add_word("вселенная", 2, 1, 3)
poem_word_db.add_word("нескончаемый", 2, 1, 3)
poem_word_db.add_word("капли", 2, 1, 3)
poem_word_db.add_word("жаждать", 1, 1, 3)
poem_word_db.add_word("несдержанный", 1, 1, 3)
poem_word_db.add_word("пейзаж", 2, 1, 3)
poem_word_db.add_word("портрет", 2, 1, 3)
poem_word_db.add_word("путешествие", 2, 1, 3)
poem_word_db.add_word("скудный", 1, 1, 3)
poem_word_db.add_word("беспокойство", 2, 1, 3)
poem_word_db.add_word("пугающий", 2, 1, 3)
poem_word_db.add_word("ужас", 2, 1, 3)
poem_word_db.add_word("меланхолия", 2, 1, 3)
poem_word_db.add_word("проницательность", 2, 1, 3)
poem_word_db.add_word("искупление", 2, 1, 3)
poem_word_db.add_word("дышать", 1, 2, 3)
poem_word_db.add_word("пленник", 2, 1, 3)
poem_word_db.add_word("желание", 1, 2, 3)
poem_word_db.add_word("кладбище", 2, 1, 3)
