# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# В этом файле содержится основной код Python для DDLC, мод-шаблона и его необязательного функционала.
# Редактирование этого файла может сломать игру полностью или частично.

## Эти импорты не используются во время запуска игры, но нужны для того, чтобы IDE
## не выдавали кучу предупреждений.
import os
import subprocess
import sys
import platform
import renpy  # type: ignore

"""renpy
init -3 python:
"""
# Эти переменные нужны, чтобы IDE не выдавали ошибки, код Python и без того имеет доступ к хранилищу и постоянным данным Ren'Py.
persistent = renpy.store.persistent
store = renpy.store

# Стандартное сообщение во время заставки игры, которое игроки увидят, запустив вашу модификацию.
splash_message_default = (
    "Данная игра является фанатской модификацией,\nкоторая никак не связана с Team Salvato."
)

# Кастомные сообщения, которые тоже могут отобразиться во время заставки.
splash_messages = [
    ":o",
    "Броня... :o",
]


## Функции DDLC

def _get_android_data_directory() -> str | None:
    """
    Возвращает путь к каталогу данных на Android.

    :return: Путь к каталогу Android/data, либо None, если путь нельзя определить.
    :rtype: str | None
    """
    if not renpy.android:
        return None

    import jnius  # type: ignore
    activity = jnius.autoclass("org.renpy.android.PythonSDLActivity")
    current_activity = jnius.cast("android.app.Activity", activity.mActivity)

    data_directory = current_activity.getFilesDir().getAbsolutePath()
    return data_directory

def get_characters_folder():
    """
    Возвращает путь к папке файлов персонажей.

    :return: Путь к папке файлов персонажей, либо None, если путь нельзя определить.
    :rtype: str | None
    """
    characters_folder = None
    if renpy.android:
        android_public_directory = _get_android_data_directory()
        if android_public_directory:
            characters_folder = os.path.join(android_public_directory, "characters")
    else:
        characters_folder = os.path.join(renpy.config.basedir, "characters").replace("\\", "/")

    return characters_folder


def restore_character(characters: list[str]):
    """
    Восстанавливает конкретных персонажей в папке «characters»
    и удаляет тех, кого нет в списке.

    :param characters: Перечень персонажей, которых надо восстановить.
    :type characters: list[str]
    """
    characters_folder = get_characters_folder()
    if characters_folder is None:
        raise FileNotFoundError("Невозможно найти папку с файлами персонажей.")

    # Удаляет файлы персонажей, которых нет в переданном списке
    for existing_file in os.listdir(characters_folder):
        if existing_file.endswith(".chr"):
            character_name = os.path.splitext(existing_file)[0]
            if character_name not in characters:
                try:
                    os.remove(os.path.join(characters_folder, existing_file))
                except OSError:
                    pass  # если файла нет – пропуск

    # Восстанавливает файлы указанных персонажей
    for character in characters:
        character_file_path = os.path.join(characters_folder, f"{character}.chr")
        if not os.path.exists(character_file_path):
            src_path = os.path.join("chrs", f"{character}.chr").replace("\\", "/")

            src_file = renpy.open_file(src_path)
            data = src_file.read()
            with open(character_file_path, "wb") as char_file:
                char_file.write(data)


def restore_characters():
    """
    Восстанавливает конкретных персонажей (или всех) в зависимости от текущего акта игры.
    """
    if renpy.store.persistent.playthrough == 0:
        restore_character(["monika", "natsuki", "sayori", "yuri"])
    elif renpy.store.persistent.playthrough in (1, 2):
        restore_character(["monika", "natsuki", "yuri"])
    elif renpy.store.persistent.playthrough == 3:
        restore_character(["monika"])
    else:
        restore_character(["natsuki", "sayori", "yuri"])


def delete_character(name: str):
    """
    Удаляет файл персонажа из папки «characters».

    :param name: Персонаж, которого надо удалить.
    :type name: str
    """
    characters_folder = get_characters_folder()
    if characters_folder is None:
        raise FileNotFoundError("Невозможно найти папку с файлами персонажей.")

    try:
        os.remove(os.path.join(characters_folder, f"{name}.chr"))
    except OSError:
        pass  # если файла нет – пропуск


def initialize_characters_folder():
    """
    Создаёт папку для файлов персонажей, если её нет.

    :return: Путь к искомой папке.
    :rtype: str
    """
    characters_folder = get_characters_folder()
    if characters_folder is None:
        raise FileNotFoundError("Невозможно определить путь к папке.")

    if not os.path.exists(characters_folder):
        os.makedirs(characters_folder)

    restore_characters()


def delete_all_saves():
    """
    Удаляет все сохранения игры.
    """
    for savegame in renpy.list_saved_games(fast=True):
        renpy.unlink_save(savegame)
    renpy.loadsave.location.unlink_persistent()
    renpy.persistent.should_save_persistent = False


def get_pos(channel: str = "music"):
    """
    Возвращает текущую позицию конкретного канала.

    :param channel: Имя нужного канала.
    :type channel: str

    :return: Текущая позиция канала, либо 0, если на канале ничего не играет.
    :rtype: int
    """
    pos = renpy.music.get_pos(channel)
    if pos is not None:
        return pos
    return 0


def pause(time=None):
    """
    Приостанавливает игру на какое-то время или пока игрок не нажмёт кнопку.

    :param time: Время (в секундах). Если None, пауза будет прервана только по нажатию кнопки.
    """
    global _windows_hidden

    if not time:
        _windows_hidden = True
        renpy.ui.saybehavior(afm=" ")
        renpy.ui.interact(mouse="pause", type="pause", roll_forward=None)
        _windows_hidden = False
        return
    if time <= 0:
        return
    _windows_hidden = True
    renpy.pause(time)
    _windows_hidden = False


## Функции ОС


def get_process_list():
    """
    Выдаёт перечень запущенных процессов в системе.

    :return: Перечень имён процессов.
    :rtype: set[str]
    """
    if renpy.android: 
        return set()  # Забор перечня процессов не поддерживается на Android

    process_list: set[str] = set()
    if renpy.windows:
        try:
            subprocess_list = subprocess.run(
                "powershell (Get-Process).ProcessName",
                shell=True,
                capture_output=True,
                text=True,
            ).stdout.splitlines()

            for _, process in enumerate(subprocess_list):
                process_list.add(f"{process.strip().lower()}.exe")
        except subprocess.CalledProcessError:
            pass
    else:
        try:
            subprocess_list = subprocess.run(
                "ps -eo comm=", shell=True, capture_output=True, text=True
            ).stdout.splitlines()

            for process in subprocess_list:
                process = process.strip().split()[
                    0
                ]  # Получаем первую часть команды
                if process:  # Убеждаемся, что она не пустая
                    process_list.add(process.lower())
        except subprocess.CalledProcessError:
            pass

    return process_list


def process_check(stream_list: list[str]):
    """
    Проверяем, запущено ли у игрока какое-то приложение из нашего перечня.

    :param stream_list: Перечень приложений для проверки.

    :type stream_list: list[str]

    :return bool: True, если что-то из перечня запущено, в противном случае – False.
    """
    if not renpy.windows:
        # Коррекция для не-Windows систем
        for index, process in enumerate(stream_list):
            stream_list[index] = process.replace(".exe", "")

    process_list = get_process_list()
    for process in stream_list:
        for running_process in process_list:
            # Проверяем, есть ли совпадения с искомым именем или с оным в качестве префикса запущенного процесса (имеет слэш в конце) [Linux/macOS]
            if running_process == process or running_process.startswith(f"{process}/"):
                return True
    return False


def is_user_streaming() -> bool:
    """
    Проверяем, запущено ли какое-то из популярных приложений для стриминга.

    :return: True, если такое приложение запущено, в противном случае – False.
    :rtype: bool
    """
    # Перечень распространённых имён приложений для стриминга
    streaming_apps = [
        "obs.exe",
        "obs64.exe",
        "streamlabsobs.exe",
        "xsplit.core.exe",
        "xsplit.broadcaster.exe",
        "twitchstudio.exe",
        "elgato.streamdeck.exe",
        "nvidia.share.exe",  # NVIDIA ShadowPlay
        "amd.raptr.exe",  # AMD ReLive
        "zoom.exe",  # Zoom (для видеоконференций)
        "teams.exe",  # Microsoft Teams (для видеоконференций)
    ]
    return process_check(streaming_apps)


def get_user_account_name():
    """
    Выдаёт имя учётной записи игрока.

    :return: Имя пользователя, либо None, если его нельзя получить.
    :rtype: str | None
    """
    if renpy.android:
        return None # На ОС Android нельзя узнать имя пользователя

    # Прерываем процесс, если игрок стримит, чтобы защитить его конфиденциальность
    if is_user_streaming():
        return None

    if renpy.windows:
        # `whoami` и разделение имени (ДОМЕН\Пользователь -> Пользователь)
        return (
            subprocess.run("whoami", shell=True, capture_output=True, text=True)
            .stdout.strip()
            .split("\\")[-1]
            or None
        )
    else:
        return (
            subprocess.run(
                "id -un", shell=True, capture_output=True, text=True
            ).stdout.strip()
            or None
        )


def get_windows_version() -> tuple[int, int, int] | None:
    """
    Выдаёт установленную версию ОС Windows.

    :return: Версия Windows, либо None, если нельзя получить или если у игрока не Windows.
    :rtype: tuple[int, int, int] | None
    """
    if not renpy.windows:
        return None

    version = sys.getwindowsversion()
    return (version.major, version.minor, version.build)


def get_macos_version() -> tuple[int, int, int] | None:
    """
    Выдаёт установленную версию ОС macOS.

    :return: Кортеж вида `(мажорная.минорная.патч)`, либо None, если нельзя получить или если у игрока не macOS.
    :rtype: tuple[int, int, int] | None
    """
    if not renpy.macintosh:
        return None

    release, _, _ = platform.mac_ver()
    if release != "":
        version_parts = release.split(".")
        if len(version_parts) >= 2:
            major = int(version_parts[0])
            minor = int(version_parts[1])
            patch = int(version_parts[2]) if len(version_parts) > 2 else 0
            return (major, minor, patch)

    return None  # Неизвестно или неподдерживаемая версия


def ddlc_under_steam() -> bool:
    """
    Проверяем, запущена ли игра через Steam.

    :return: True, если запущена через Steam, в противном случае – False.
    :rtype: bool
    """
    return "steamapps" in renpy.config.basedir.lower()


currentuser = get_user_account_name()

## Функции мод-шаблона


## TODO: Попытаться адаптировать под Transform и MatrixColor
def recolorize(
    path: str, blackCol: str = "#ffbde1", whiteCol: str = "#ffe6f4", contr: float = 1.29
):
    """
    Перекрашивает конкретное изображение, используя указанные цвета и контрастность.

    :param path: Путь к искомому изображению.
    :param blackCol: Цвет для тёмных участков.
    :param whiteCol: Цвет для светлых участков.
    :param contr: Желаемый уровень контрастности.

    :type path: str
    :type blackCol: str
    :type whiteCol: str
    :type contr: float

    :return: Перекрашенное изображение.
    """
    return renpy.im.MatrixColor(
        renpy.im.MatrixColor(
            renpy.im.MatrixColor(
                path, renpy.im.matrix.desaturate() * renpy.im.matrix.contrast(contr)
            ),
            renpy.im.matrix.colorize("#00f", "#fff") * renpy.im.matrix.saturation(120),
        ),
        renpy.im.matrix.desaturate() * renpy.im.matrix.colorize(blackCol, whiteCol),
    )


### Динамическое суперпозиционирование
def dsp(original_position_value: int | float) -> int:
    """
    Динамически подгоняет положение элемента исходя из разрешения
    оригинальной игры (1280x720) относительно пользовательского.

    Предполагается, что исходное значение положения установлено для разрешения 1280x720.
    """
    valueIsInt = isinstance(original_position_value, int)
    scale_position_by = renpy.config.screen_width / 1280.0
    if valueIsInt:
        return int(original_position_value * scale_position_by)
    return original_position_value * scale_position_by


### Динамическое суперразрешение
def dsr(image_path: str):
    """
    Динамически подгоняет размер изображения исходя из разрешения
    оригинальной игры (1280x720) относительно пользовательского.

    (Настоятельно рекомендуется использовать изображения высокого разрешения и использовать DSP вместо DSR.)
    """
    image_bounds = renpy.image_size(image_path)
    return renpy.Transform(
        image_path, size=(dsp(image_bounds[0]), dsp(image_bounds[1]))
    )


## Инициализация основного кода

# Настройка горячих клавиш для игрового меню и скрытия окон.
renpy.config.keymap["game_menu"].remove("mouseup_3")
renpy.config.keymap["hide_windows"].append("mouseup_3")
renpy.config.keymap["self_voicing"] = []
renpy.config.keymap["clipboard_voicing"] = []
renpy.config.keymap["toggle_skip"] = []

# Регистрация музыкального канала для мини-игры про обмен стихами.
renpy.music.register_channel("music_poem", mixer="music", tight=True)

# Инициализация жестов для устройств на ОС Android.
if renpy.android:
    renpy.config.keymap["rollback"] = []
    renpy.config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]

renpy.pure(dsp)
