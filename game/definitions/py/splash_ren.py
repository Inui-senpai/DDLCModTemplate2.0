# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# В этом файле прописана проверка наличия файлов «audio.rpa» и «images.rpa» в папке игры,
# и что папка проекта находится не в папке облачного хранилища (OneDrive).
# Примечание: Чтобы модификация собралась для ПК/Android, вы должны сохранить RPA-архивы из DDLC
# и распаковать их, чтобы собранный дистрибутив работал корректно.

import os
from game.core.py.template_checks_ren import DDLCRPAsMissing, IllegalModLocation
import renpy  # type: ignore

"""renpy
init -100 python:
"""

if not renpy.android:
    for archive in ["audio", "images"]:
        if archive not in renpy.config.archives:
            raise DDLCRPAsMissing(archive)

    if renpy.windows:
        onedrive_path = os.environ.get("OneDrive")
        if onedrive_path is not None:
            if onedrive_path in renpy.config.basedir:
                raise IllegalModLocation
