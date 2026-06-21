## Это шаблон версии 5.0.0. Если у вас спросят версию использованного шаблона,
## назовите им этот номер версии.
### НЕ УДАЛЯЙТЕ И НЕ ИЗМЕНЯЙТЕ ВЫШЕПРИВЕДЁННЫЙ КОММЕНТАРИЙ. ###

## options.rpy
# Этот файл определяет, что представляет собой ваша модификация, а также как она запускается и собирается!

# Указывает название вашей модификации.
define config.name = _("Мод-шаблон DDLC – Издание для Python 3")

# Указывает, хотите ли вы, чтобы название вашей модификации отображалось в главном меню.
# Если название длинное, этот параметр лучше отключить.
define gui.show_name = True

# Указывает номер версии вашей модификации.
define config.version = "5.0.0"

# Добавляет информацию о вашей модификации на экран «Об игре».
# В DDLC нет такого экрана, так что можете оставить это поле пустым.
define gui.about = _("")

# Указывает название дистрибутива вашей модификации во время упаковки
# в лаунчере Ren'Py или DDMM (Doki Doki Mod Maker).
# Примечание:
#   Название сборки поддерживает только символы ASCII, никаких цифр, пробелов и точек с запятой быть не должно.
#   Пример: «Doki Doki Yuri Time» -> «DokiDokiYuriTime»
define build.name = "DDLCModTemplateTwo-Py3"

# Указывает, есть ли в вашей модификации звуковые эффекты.
define config.has_sound = True

# Указывает, есть ли в вашей модификации музыка.
define config.has_music = True

# Указывает, есть ли в вашей модификации озвучка.
define config.has_voice = False

# Указывает, какая музыка будет играть при запуске модификации
# и в главном меню.
define config.main_menu_music = audio.t1

# Эти переменные управляют эффектами переходов в DDLC, когда игрок входит в
# меню и выходит из него.
#   config.enter_transition указывает эффект, которым сопровождается вход в игровое меню.
#   config.exit_transition указывает эффект, которым сопровождается возврат в игру.
#   Dissolve(X) «растворяет» меню или последний экран в течение X секунд.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# Указывает эффект перехода в DDLC после загрузки сохранения.
define config.after_load_transition = None

# Указывает эффект перехода, когда сюжет вашей модификации подошёл к своему финалу.
define config.end_game_transition = Dissolve(.5)

# Определяет поведение диалогового окна, через которое общаются персонажи.
#   "auto" – диалоговое окно будет скрываться во время смены сцен и показываться, когда персонаж говорит;
#   "show" – диалоговое окно будет отображаться постоянно;
#   "hide" – диалоговое окно будет показываться только тогда, когда персонаж говорит.
define config.window = "auto"

# Указывает эффекты переходов диалогового окна.
#   config.window_show_transition указывает эффект, которым сопровождается появление диалогового окна.
#   config.window_hide_transition указывает эффект, которым сопровождается скрытие диалогового окна.
#   Dissolve(X) «растворяет» меню или последний экран в течение X секунд.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# Указывает скорость вывода текста в вашей модификации.
default preferences.text_cps = 50

# Указывает задержку при включённом режиме авточтения в вашей модификации.
default preferences.afm_time = 15

# Указывает уровни громкости микшеров по умолчанию в вашей модификации.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# Указывает название папки сохранённых данных вашей модификации.
# Сохранения можно найти здесь:
#   Windows: %AppData%/RenPy/ (включите показ скрытых файлов и папок в меню Проводника)
#   macOS: $HOME/Библиотека/RenPy/ (включите показ папки «Библиотека» в Настройках Finder)
#   Linux: $HOME/.renpy/ (включите показ скрытых файлов в Настройках вашего файлового менеджера)
define config.save_directory = "DDLCModTemplateTwo-Py3"

# Указывает значок окна вашей модификации.
define config.window_icon = "gui/window_icon.png"

# Указывает, разрешено ли игроку пропускать диалоги.
define config.allow_skipping = True

# Указывает, может ли модификация автоматически сохраняться.
define config.has_autosave = False

# Указывает, может ли модификация автоматически сохраняться после выхода из игры.
define config.autosave_on_quit = False

# Указывает количество слотов, которые автосохранение может использовать для сохранения игры.
define config.autosave_slots = 0

# Указывает, может ли игрок откатываться назад по сюжету игры.
define config.rollback_enabled = config.developer

# Эти переменные контролируют расположение слоёв экранов, изображений и прочего.
# Настоятельно рекомендуется не трогать их.
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    # Отключает поддержку геймпада
    renpy.game.preferences.pad_enabled = False

    # Заменяет "-" в диалогах на "–" (избавляет от необходимости копировать знак
    # из русификатора Энтузиастов)
    def replace_text(s):
        s = s.replace(" - ", " – ")
        return s

    config.say_menu_text_filters = [replace_text]

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    config.adjust_view_size = force_integer_multiplier

## Настройка дистрибуции #######################################################
##
## Этот раздел контролирует, как Ren'Py строит файлы дистрибутива из вашего проекта.

init python:
    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Внутри образца:
    ## * включает в себя все символы, исключая разделитель директорий.
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Примеры:
    ## "*.txt" охватывает все файлы формата «.txt» из директории проекта.
    ## "game/**.ogg" охватывает все файлы «.ogg» из директории «game» и 
    ## всех поддиректорий.
    ## "**.psd" охватывает все файлы «.psd» из любого места проекта.

    # Эти переменные объявляют названия пакетов для дистрибуции вашей модификации,
    # которые соответствуют условиям Руководства по использованию ИС Team Salvato.
    # Никоим образом не изменяйте эти переменные.
    build.package("Renpy8-DDLCMod", 'zip', 'windows linux mac renpy mod',
        description="DDLC-совместимый мод на Ren'Py 8")

    # Эти переменные объявляют архивы, которые будут сделаны для упаковки вашей
    # модификации.
    # Чтобы добавить ещё один архив, пропишите ещё один «build.archive», взяв в
    # качестве примера одну из уже имеющихся переменных:
    build.archive("scripts", 'mod')
    build.archive("mod_assets", 'mod')

    # Не трогайте эти строчки. Это нужно для того, чтобы Ren'Py добавил файл
    # формата «.py» вашей модификации и специальный лаунчер для Linux и macOS,
    # необходимый для запуска.
    build.renpy_patterns.remove(('renpy.py', ['all']))
    build.classify_renpy("renpy.py", "renpy all")

    build.early_base_patterns.remove(('*.sh', None))
    build.classify("LinuxLauncher.sh", "linux") ## Скрипт лаунчера для Linux
    build.classify("*.sh", None)

    #############################################################
    # Эти функции классифицируют пакеты для настольных (ПК, Linux, macOS) и мобильных (Android, iOS) платформ.
    # Обязательно допишите 'android ios' в своей классификации, если планируете
    # портировать свою модификацию на Android и/или iOS, как в примере ниже.
    #   Пример: build.classify("game/**.pdf", "scripts android ios")
    build.classify("game/mod_assets/**", "mod_assets android ios")
    build.classify("game/presplash.png", "scripts") # игнорируется – прим. пер.
    build.classify("game/**.rpyc", "scripts android ios")
    build.classify("game/**.txt", "scripts android ios")
    build.classify("game/**.chr", "scripts android ios")
    build.classify("game/advanced_scripts/**","scripts android ios") ## Обратная совместимость
    build.classify("game/tl/**.rpymc", "scripts android ios") ## Базовый перевод интерфейса
    build.classify("game/tl/**", "scripts android ios") ## Переводы на разные языки
    build.classify("game/mod_extras/**.rpyc", "scripts android ios") ## Необязательный функционал (обратная совместимость)

    # Классификации для «классических» архивов – удаляем всё сверху, вплоть до
    # `build.package`, и раскомментируем это, если хотим ИМЕННО 4 архива, как в DDLC
    # build.archive("audio", "renpy")
    # build.archive("fonts", "renpy")
    # build.archive("images", "renpy")
    # build.archive("scripts", "renpy")

    # build.classify("game/**.wav", "audio android ios")
    # build.classify("game/**.mp3", "audio android ios")
    # build.classify("game/**.ogg", "audio android ios")
    # build.classify("game/**.opus", "audio android ios")
    # build.classify("game/**.ttf", "fonts android ios")
    # build.classify("game/**.otf", "fonts android ios")
    # build.classify("game/**.jpg", "images android ios")
    # build.classify("game/**.png", "images android ios")
    # build.classify("game/**.webm", "images android ios")
    # build.classify("game/**.webp", "images android ios")
    # build.classify("game/**.ogv", "images android ios")
    # build.classify("game/**.rpyc", "scripts android ios")
    # build.classify("game/**.rpymc", "scripts android ios")
    # build.classify("game/**.txt", "scripts android ios")
    # build.classify("game/**.chr", "scripts android ios")

    # build.classify("game/python-packages/**", "scripts android ios")
    # ---

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpym', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify("**/.DS_Store", None)
    build.classify("**/.vscode/**", None)
    build.classify("game/**.md", None)

    build.classify('README.html','mod all')
    build.classify('README.linux', 'linux')

    # Указывает файл README.html в качестве файла документации
    build.documentation('README.html')

    build.include_old_themes = False
