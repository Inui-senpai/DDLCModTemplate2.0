# Этот файл содержит код Ren'Py для консоли Моники в DDLC.

# Логика работы консоли была кардинально изменена по сравнению с оригинальной игрой, чтобы
# обеспечить лучшее управление вводом и выводом данных с консоли, а также отображением.
# Логика Python отделена от кода отображения и теперь находится в файле `py/console_ren.py`.

# Чтобы вывести консоль на экран, пропишите `$ console.show_screen()` или `show screen console_screen(console)`.

# Чтобы просмотреть код Python, откройте файл `console_ren.py` в каталоге `py`.

init -1:
    default console = Console(console_delay=0.5, console_cps=30, max_log_history=5)

screen console_screen(console, input_text=None, output_text=None, cps=None, delay=None):
    """
    Этот экран показывает внутриигровую консоль.
    """

    style_prefix "console_screen"

    default finish_actions = [SetScreenVariable("in_progress", False), Return()] # использовать Return() во время диалога опасно – прим. пер. 

    python:
        used_cps = cps if cps is not None and type(cps) == int else console.console_cps
        used_delay = delay if delay is not None and type(delay) == float else console.console_delay

    # Вводимая команда, которая будет выведена на экран.
    # Она помещается вне переменной «new_input», чтобы не повторяться
    # снова и снова.
    default new_input_code = "_"

    # Меняется на True, когда отправляется новая команда
    default in_progress = False

    # Если текст не в процессе вывода на экран
    if not in_progress:

        $ new_input_code = "_"

        if input_text:
            $ in_progress = True
            $ new_input_code = input_text

    # Новая команда выводится на экран
    if in_progress:

        timer ( (float(len(renpy.filter_text_tags(new_input_code, deny = []))) / float(used_cps)) + used_delay ) action finish_actions

    frame:

        vbox:
            hbox:
                text ">" xpos 5 ypos 10

                text new_input_code xpos 15 ypos 10:
                    slow_cps 30
                    xmaximum 460

            vbox:
                xpos 26 ypos 30 
                spacing 5

                for output in console.console_history.values():
                    text output

style console_screen_frame:
    background Frame(Transform(Solid("#333"), alpha=0.75))
    xsize 480
    ysize 180

# Этот стиль определяет оформление текста, отображаемого во внутриигровой консоли.
style console_screen_text:
    font "gui/font/consola.ttf"
    color "#fff"
    size 18
    outlines []
