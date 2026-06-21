# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл отвечает за блокировку игры в целях предотвращения запуска двух и более копий игры.
# По сути, это переработанная версия `singleton.py`, позволяющая включать/отключать поведение модуля «одиночки».

"""renpy
python early:
"""

import os
import tempfile
import sys

if sys.platform == "win32":
    import msvcrt  # для ОС семейства Windows
else:
    import fcntl  # для ОС семейства Unix/Linux

# Включает/отключает ограничение числа работающих экземпляров игры.
# Чтобы разрешить запуск нескольких экземпляров, измените True на False.
# Примечание: изменение этого поведения нежелательно для некоторых модификаций.
ENABLE_SINGLETON = True


class SingleInstance:
    """
    Класс, который отвечает за ограничение числа работающих экземпляров игры.
    """

    def __init__(self):
        lock_file = "ddlc.lock"
        temp_dir = os.path.join(tempfile.gettempdir(), lock_file)

        self.lock_file = temp_dir
        self.lock_fd = None

        if not self.acquire_lock():
            sys.exit(-1)

    def acquire_lock(self):
        """
        Блокирует файл блокировки, чтобы гарантировать запуск только одного экземпляра игры.

        :return bool: True, если блокировка удалась, в противном случае – False.
        """
        if not ENABLE_SINGLETON:
            return True

        try:
            self.lock_fd = open(self.lock_file, "w+")
            if sys.platform == "win32":
                msvcrt.locking(self.lock_fd.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except (IOError, OSError):
            if self.lock_fd:
                self.lock_fd.close()
                self.lock_fd = None
            return False

    def release_lock(self):
        """
        Снимает блокировку с файла блокировки.
        """
        if not ENABLE_SINGLETON:
            return

        if self.lock_fd:
            if sys.platform == "win32":
                msvcrt.locking(self.lock_fd.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
            self.lock_fd.close()
            try:
                os.remove(self.lock_file)
            except OSError:  # Кто-то удалил это...
                pass
        self.lock_fd = None

    def __del__(self):
        self.release_lock()


# Создаёт экземпляр «одиночки», чтобы обеспечить работу только одного процесса игры.
# Не удаляйте эту строку. Если вы хотите отключить вышеописанное поведение, измените
# значение переменной `ENABLE_SINGLETON` выше на False.
_singleton = SingleInstance()
