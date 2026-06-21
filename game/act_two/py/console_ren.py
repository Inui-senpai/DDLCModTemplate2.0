# Этот файл содержит код Python для консоли Моники в DDLC.

# Логика работы консоли была кардинально изменена по сравнению с оригинальной игрой, чтобы
# обеспечить лучшее управление вводом и выводом данных с консоли, а также отображением.
# Также здесь используется подход Ren'Py, предполагающий использование нового файла `_ren.py` для кода Python.

# Чтобы просмотреть код отображения консоли, откройте файл `console.rpy` в каталоге `act_two`.

## Этот импорт не используется во время запуска игры, но нужен для того, чтобы IDE
## не выдавали кучу предупреждений.
import renpy  # type: ignore

"""renpy
init python:
"""


class Console(object):
    """
    Определяет логику работы «терминала» DDLC.
    """

    def __init__(
        self,
        console_delay: float,
        console_cps: int,
        max_log_history: int = 5,
        testing: bool = False,
    ) -> None:
        """
        Инициализирует консоль с заданными задержкой и скоростью вывода текста (cps).

        :param console_delay: Задержка перед появлением «выхлопа» команды.
        :param console_cps: Скорость вывода вводимой команды.
        :param max_log_history: Максимальное число записей в истории консоли.
        :param testing: Обход системы экранов Ren'Py в целях тестирования. Не используется в DDLC. Используется системой GitHub Actions для проверки логики кода.

        :type console_delay: float
        :type console_cps: int
        :type max_log_history: int
        :type testing: bool
        """

        self.console_delay = console_delay
        self.console_cps = console_cps
        self.max_log_history = max_log_history

        # Создаёт пустой словарь для истории консоли.
        self.console_history: dict[str, str] = {}

        self.testing = testing

    def __call__(self, input_text: str, output_text: str, cps: int | None = None, delay: float | None = None) -> None:
        """
        Обрабатывает вводимый и выводимый текст в консоли.
        Если хотите, чтобы во время ввода команды что-то происходило,
        обязательно добавьте это здесь.

        :param input_text: Текст отправляемой команды.
        :param output_text: «Выхлоп» команды, который должен появиться после команды.
        :param cps: Скорость вывода текста. Если None, используется значение консоли по умолчанию.
        :param delay: Задержка перед появлением «выхлопа». Если None, используется значение консоли по умолчанию.
        :type input_text: str
        :type output_text: str
        :type cps: int | None
        :type delay: float | None
        """

        # Если число записей в истории консоли достигло установленного порога, будет удалена самая старая запись.
        if len(self.console_history) + 1 > self.max_log_history:
            oldest_key = min(self.console_history.keys())
            del self.console_history[oldest_key]

        # Отобразить экран консоли с командой и «выхлопом».
        if not self.testing:
            if renpy.get_screen("console_screen"):
                renpy.hide_screen("console_screen")
            renpy.call_screen(
                "console_screen",
                console=self,
                input_text=input_text,
                output_text=output_text,
                cps=cps,
                delay=delay,
            )

        # Сохранить команду и её «выхлоп» в истории консоли.
        self.console_history[input_text] = output_text
        self.show_screen()

        renpy.restart_interaction()

    def clear_history(self) -> None:
        """
        Очистить историю консоли.
        """
        self.console_history.clear()

    def show_screen(self) -> None:
        """
        Отобразить экран консоли.
        """
        if not self.testing:
            renpy.show_screen("console_screen", console=self)
