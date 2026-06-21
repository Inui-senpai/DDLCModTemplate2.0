# В этом файле прописан код Python для обработки особых исключений мод-шаблона
# и проверки версии Ren'Py во время запуска.

## Этот импорт не используется во время запуска игры, но нужен для того, чтобы IDE
## не выдавали кучу предупреждений.
import renpy  # type: ignore

"""renpy
python early:
"""


class NotRenPyEight(Exception):
    def __str__(self):
        return "Данная версия мод-шаблона предназначена для Ren'Py 8.\nСкачайте последнюю версию SDK с официального сайта, или, если оная у вас уже есть, соберите свою модификацию на ней."


class DDLCRPAsMissing(Exception):
    def __init__(self, archive: str):
        self.archive = archive

    def __str__(self):
        return f"Файл «{self.archive}.rpa» не был найден в папке игры.\nПроверьте правильность установки модификации на оригинальную DDLC и повторите попытку."


class IllegalModLocation(Exception):
    def __str__(self):
        return "Модификации для DDLC и проекты оных не могут быть запущены из этой папки, т.к. это папка OneDrive или иного облачного хранилища.\nПереместите папку модификации/проекта в другую директорию и повторите попытку."


if renpy.version_tuple < (8, 0, 0, 22062402):
    raise NotRenPyEight
