# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл содержит код Ren'Py для отображения стихотворений в DDLC.

# Чтобы просмотреть код Python, откройте файл `poems_ren.py` в каталоге `py`.

screen poem(poem):
    style_prefix "poem"

    fixed:

        frame:
            style "poem_paper"

            add poem.paper:
                subpixel True align (0.5, 0.5)

        frame:
            background None

            hbox:
                viewport id "poem_vp":
                    draggable True
                    mousewheel True

                    add poem

                vbar value YScrollValue("poem_vp")

    if not persistent.first_poem:
        add "gui/poem_dismiss.png" xpos 1050 ypos 590

    key ["repeat_K_UP", "K_UP"] action Scroll("poem_vp", "vertical decrease", 20)
    key ["repeat_K_DOWN", "K_DOWN"] action Scroll("poem_vp", "vertical increase", 20)

    on "show" action SetVariable("poem_last_author", poem.author)

style poem_vscrollbar:
    xsize 20
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style poem_paper:
    modal True
    align (0.5, 0.5)

style poem_fixed:
    align (0.5, 0.5)
    xsize 720

style poem_frame:
    padding (4, 35)

style poem_hbox:
    xfill True

style yuri_text:
    font "gui/font/Vivaldi.ttf"
    size 28
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/ShlapakScript.otf"
    size 20
    color "#000"
    outlines []
    kerning -2.2
    justify True

style natsuki_text:
    font "gui/font/ScriptC.otf"
    size 28
    color "#000"
    outlines []

style sayori_text:
    font "gui/font/StudioScriptC.otf"
    size 28
    color "#000"
    line_spacing 10
    outlines []

style monika_text:
    font "gui/font/Adventure.ttf"
    size 24
    color "#000"
    line_spacing 10
    outlines []

default poem_last_author = None

# Предупреждение об устаревшей функции
label showpoem(poem, **properties):
    python:
        text = "Эта функция устарела. Используйте теперь " + ("'$ poem_db.show_poem(\"%s\", %s)'" % (poem, ", ".join("%s=%s" % (k, v) for k, v in properties.items())) if properties else "'$ poem_db.show_poem(\"%s\")'" % poem) + ".\nПодробности см. в файле {u}poem_responses/py/poems_ren.py{/u}."
    $ renpy.notify(text)
    return
