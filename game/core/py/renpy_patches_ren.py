# В этом файле прописан код Python, который необходим для корректной работы DDLC на Ren'Py 8.

## Эти импорты не используются во время запуска игры, но нужны для того, чтобы IDE
## не выдавали кучу предупреждений.
import os
import renpy  # type: ignore

"""renpy
python early:
"""

# Изменяет старые команды для ОС Windows из DDLC, чтобы использовался интерпретатор PowerShell; нужно для совместимости с Windows 11.
if renpy.windows:
    os.environ["wmic process get Description"] = "powershell (Get-Process).ProcessName"
    os.environ["wmic os get version"] = (
        "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"
    )

## Отображаемые элементы, использующие ATL, запускают свою анимацию
## при первом появлении, а не в том случае, когда появился сам экран.
## Мы же откатим это поведение ради блага трансформаций DDLC.
if renpy.version_tuple >= (7, 4, 7, 1862):
    renpy.config.atl_start_on_show = False

## Удаляет папку «saves» из списка известных местоположений сохранений в настольных версиях игры.
## P.S. Это ломает автоматическое создание «navigation.json», но это необходимая жертва.
## И потом, его всегда можно создать вручную, а обновляться он уже будет сам. :upside_down:
import threading

def savelocation_init_override():
    renpy.savelocation.quit()
    renpy.savelocation.quit_scan_thread = False

    location = renpy.savelocation.MultiLocation()
    location.add(renpy.savelocation.FileLocation(renpy.config.savedir))

    for i in renpy.config.extra_savedirs:
        location.add(renpy.savelocation.FileLocation(i))

    location.scan()

    renpy.loadsave.location = location

    renpy.savelocation.scan_thread = threading.Thread(target=renpy.savelocation.run_scan_thread)
    renpy.savelocation.scan_thread.start()

renpy.savelocation.init = savelocation_init_override
