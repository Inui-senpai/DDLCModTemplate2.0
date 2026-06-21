# Этот файл содержит код Python для интеграции с сервисом Discord.
# Данный код зависит от библиотеки «pypresence», она должна находиться в каталоге «python-packages» вашей модификации.

# Перед началом работы создайте новое приложение на Портале разработчиков Discord:
# https://discord.com/developers/applications
# Чтобы настроить интеграцию под себя, следуйте инструкциям в комментариях внутри функции `set_defaults`.

## Эти импорты не используются во время запуска игры, но нужны для того, чтобы IDE
## не выдавали кучу предупреждений.
import renpy # type: ignore
from renpy import NoRollback # type: ignore
from game.definitions.py.core_ren import persistent

last_reported_status_data = {
    "state": "",
    "details": "",
    "large_image": "",
    "large_text": "",
    "small_image": "",
    "small_text": "",
}

"""renpy
init -950 python:
"""

from pypresence import Presence, DiscordError, DiscordNotFound, InvalidPipe
from copy import deepcopy
import time

class DiscordRPC(NoRollback):
    def __init__(self, client_id: str) -> None:
        """
        Инициализирует DiscordRPC с переданным ИД клиента.

        :param client_id: ИД клиента приложения Discord.
        :type client_id: str
        """

        self.client_id = client_id
        self.rpc_connected = False
        self.rpc: Presence | None = None

        # Данные статуса Discord
        self.start: float = 0.0
        self.details: str = ""
        self.state: str = ""
        self.large_image: str = ""
        self.large_text: str = ""
        self.small_image: str = ""
        self.small_text: str = ""

        self.original_state: dict = {}

    def set_defaults(self) -> None:
        """
        Задаёт значения по умолчанию для статуса интеграции с Discord.
        Меняйте эти значения, чтобы кастомизировать статус по умолчанию.
        """

        # Подробности, описывающие то, чем игрок сейчас занимается.
        # Пример: В главном меню
        self.details = renpy.version()

        # Состояние, отражающее дополнительную информацию в подробностях.
        # Пример: Просматривает настройки
        self.state = "Броня... :o"

        # Крупное изображение для отображения в интеграции.
        self.large_image = "ddlcmodtemplatelogo"

        # Текст, который отобразится, если пользователь наведёт курсор на крупное изображение.
        self.large_text = renpy.config.name # здесь используется название модификации

        # Маленькое изображение для отображения в интеграции.
        self.small_image = "test"

        # Текст, который отобразится, если пользователь наведёт курсор на маленькое изображение.
        self.small_text = renpy.config.version # здесь используется номер версии модификации

        self.original_state = self.__dict__()

    def initialize_rpc(self) -> None:
        """
        Инициализирует соединение интеграции.
        """
        if not persistent.enable_discord:
            return

        try:
            self.rpc = Presence(self.client_id)
        except (DiscordError, DiscordNotFound):
            renpy.exports.write_log("Клиент Discord не найден.")
            return

    def connect(self, reset: bool = False) -> None:
        """
        Подключается к службе интеграции с Discord.

        :param reset: Нужно ли сбросить данные статуса перед соединением.
        :type reset: bool
        """

        if not persistent.enable_discord:
            return
        if self.rpc_connected:
            return # Интеграция уже подключена
        if self.rpc is None:
            self.initialize_rpc()
            if self.rpc is None:
                return

        if reset:
            self.reset()
            self.start = time.time()
        else:
            self.set(**self.__dict__())

        try:
            self.rpc.connect()
            self.rpc_connected = True
        except InvalidPipe:
            self.rpc = None

    def disconnect(self) -> None:
        """
        Отключается от службы интеграции с Discord.
        """

        if self.rpc is None:
            return
        self.rpc.close()
        self.rpc_connected = False

    def set(self, **kwargs) -> None:
        """
        Задаёт статус интеграции.

        :param kwargs: Пары «ключ-значение» для данных статуса.
        """
        if not persistent.enable_discord:
            return
        if self.rpc is None or not self.rpc_connected:
            return

        # Обновляет данные статуса, используя предоставленные ключевые аргументы.
        valid_keys = {
            "state", "details", "large_image", "large_text",
            "small_image", "small_text"
        }
        for key, value in kwargs.items():
            if key in valid_keys:
                setattr(self, key, value)

        updated_data = self.__dict__()
        self.rpc.update(**updated_data)
        self.record_to_rollback()

    def reset(self) -> None:
        """
        Сбрасывает статус интеграции.
        """
        self.set(**self.original_state)

    def record_to_rollback(self) -> None:
        """
        Записывает текущие данные статуса для отката.
        """
        global last_reported_status_data
        last_reported_status_data = deepcopy(self.__dict__())

    def rollback_check(self) -> None:
        """
        Проверяет, изменились ли данные, и обновляет статус при необходимости.
        """

        global last_reported_status_data
        if not persistent.enable_discord:
            return
        if self.rpc is None or not self.rpc_connected:
            return

        current_data = self.__dict__()
        if current_data != last_reported_status_data:
            self.set(**last_reported_status_data)

    def on_load(self) -> None:
        """
        Обновляет статус после загрузки сохранения.
        """

        global last_reported_status_data
        if not persistent.enable_discord:
            return
        if self.rpc is None or not self.rpc_connected:
            return

        self.set(**last_reported_status_data)

    def __dict__(self) -> dict:
        return {
            "state": self.state,
            "details": self.details,
            "large_image": self.large_image,
            "large_text": self.large_text,
            "small_image": self.small_image,
            "small_text": self.small_text,
            "start": self.start,
        }

# Вставьте свой токен внутри кавычек
RPC = DiscordRPC("979471077187125248")
RPC.initialize_rpc()
RPC.connect(True)

renpy.config.quit_callbacks.append(RPC.disconnect)
renpy.config.after_load_callbacks.append(RPC.on_load)
renpy.config.interact_callbacks.append(RPC.rollback_check)
renpy.config.start_callbacks.append(RPC.reset)