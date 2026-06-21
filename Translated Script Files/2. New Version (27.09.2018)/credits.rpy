

init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size (640, 360)

image credits_logo:
    "gui/logo_ru.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/v_CCBellyLaugh.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/comic.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/Adventure.ttf"
    color "#fff"
    size 30
    text_align 0.5
    line_leading 1
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image credits_header2 = ParameterizedText(style="credits_header", ypos=-55)
image credits_text2 = ParameterizedText(style="credits_text", ypos=30)
image credits_header_3 = ParameterizedText(style="credits_header", ypos=-85)
image credits_text_3 = ParameterizedText(style="credits_text", ypos=30)
image credits_header_5 = ParameterizedText(style="credits_header", ypos=-140)
image credits_text_5 = ParameterizedText(style="credits_text", ypos=25)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -340
    "black"
    10.33
    Text("День за днём,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.5, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -30
    "black"
    11.75
    Text("строю мир в голове, где будем", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 307
    "black"
    13.76
    Text("лишь мы с тобой.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -340
    "black"
    19.45
    Text("На листе", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.5, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -60
    "black"
    20.9
    Text("пером выведу стих, в котором", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 285
    "black"
    23.27
    Text("ты здесь, со мной.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("Тёмной лужей чернила вдруг стали,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.5, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    "black"
    32.9
    Text("Просто пиши - дай им стать большой рекой.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.5, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("В мире, где миллионы решений,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 11.5, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -185
    "black"
    42.0
    Text("Куда же плыть", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 110
    "black"
    43.47
    Text("вместе с нею за мечтой?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("Какой же путь вместе нас сведёт с тобой?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

label credits:
    $ persistent.autoload = "credits"
    $ renpy.save_persistent()
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    scene black
    if persistent.trans_ending:
        play music "bgm/end-voice_ru.ogg" noloop
    else:
        play music "bgm/end-voice.ogg" noloop



    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat

    if not persistent.trans_ending:
        $ pause(4.00)
        call showsubs ("... ме... шишь?..")
        $ pause(2.50)
        call showsubs ("...ты ...ня сл...шь?")
        $ pause(2.00)
        call showsubs ("Эм, ты меня слышишь?")
        $ pause(2.00)
        call showsubs ("Кхм...")
        $ pause(1.00)
        call showsubs ("Привет! Это я.")
        $ pause(2.00)
        call showsubs ("М-м-м, помнишь, как я говорила, что учусь играть на пианино?")
        $ pause(6.00)
        call showsubs ("Я до сих пор не добилась особых успехов...")
        $ pause(3.00)
        call showsubs ("Но...")
        $ pause(1.00)
        call showsubs ("Я написала тебе песенку.")
        $ pause(3.00)
        call showsubs ("И я надеялась, что спою её тебе, ведь я очень-очень долго над ней работала.")
        $ pause(6.00)
        call showsubs ("Так что... Вот!")
        pause 4
    else:
        pause 39
    jump credits1

label credits1:
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...")
    pause 1.0
    call hideconsole
    if persistent.trans_ending:
        play music "<to 50.0>bgm/credits_ru.ogg" noloop
    else:
        play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    if persistent.trans_ending:
        play music "<from 50.0>bgm/credits_ru.ogg" noloop
    else:
        play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Концепция и дизайн игры" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.trans_ending:
        call showsubs ("Всем ли я подыскала сегодня то, чем себя занять?")
        $ pause(16.00 - (datetime.datetime.now() - starttime).total_seconds())
        call hidesubs
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
    if not persistent.trans_ending:
        call showsubs ("Всё равно, когда мы с тобой рядом, хочется лишь болтать.")
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Художник по персонажам" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.trans_ending:
        $ pause(25.00 - (datetime.datetime.now() - starttime).total_seconds())
        call hidesubs
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
    if not persistent.trans_ending:
        call showsubs ("Если мне не понять свои чувства,")

    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Художник по фонам" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.trans_ending:
        $ pause(32.50 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Улыбка скажет о них нам за меня.")

    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
    if not persistent.trans_ending:
        call showsubs ("И если мир не создаст мне концовку,")

    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Автор сценария" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.trans_ending:
        $ pause(42.00 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Не стоит ли мне самой украсть тебя?")

    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
    if not persistent.trans_ending:
        call hidesubs

    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Композитор" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(54.30 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    if not persistent.trans_ending:
        show credits_header "Исполнитель песни" as credits_header_2 at credits_text_scroll_right
        show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    else:
        show credits_header2 "Исполнители песни" as credits_header_2 at credits_text_scroll_right
        show credits_text2 "Jillian Ashcraft\nAka" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(63.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header_5 "Перевод" as credits_header_1 at credits_text_scroll_left
    show credits_text_5 "Erizo\nMamavl\nDOOMer\nFibYar\nAka" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.trans_ending:
        $ pause(64.30 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Почему к тем, кто дорог, я не могу горечь заглушить?")
    $ pause(71.30 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.trans_ending:
        call hidesubs
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header_3 "Особая благодарность" as credits_header_2 at credits_text_scroll_right
    show credits_text_3 "Masha Gutin\nKagefumi\nDavid Evelyn" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    if not persistent.trans_ending:
        $ pause(74.30 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Красть тебя - это признак любви, или стоит отпустить?")
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.trans_ending:
        call hidesubs
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header_3 "Особая благодарность" as credits_header_1 at credits_text_scroll_left
    if not persistent.trans_ending:
        call showsubs ("Тёмной лужей чернила вдруг стали,")
    show credits_text_3 "Corey Shin\nAlecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    if not persistent.trans_ending:
        $ pause(92.40 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Как мне сказать в твоём мире о любви?")
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Особая благодарность" as credits_header_2 at credits_text_scroll_right
    show credits_text "Моника\n[player]" as credits_text_2 at credits_text_scroll_right
    if not persistent.trans_ending:
        $ pause(97.00 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Сердца звук не могу твой услышать.")
        $ pause(102.00 - (datetime.datetime.now() - starttime).total_seconds())
        call showsubs ("Как ты зовёшь любовь в твоей реальности?")
    $ pause(103.50 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    if not persistent.trans_ending:
        call showsubs ("И в твоей реальности, если я не полюблю вновь...")

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
    if not persistent.trans_ending:
        call hidesubs
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
    if not persistent.trans_ending:
        call showsubs ("Меня прости.")
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    if not persistent.trans_ending:
        call hidesubs
    show credits_ts
    show credits_text "сделано с любовью":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ renpy.save_persistent()
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        $ allow_skipping = False
        scene black
        show poem_end
        $ pause()
        call screen dialog(message="Ошибка: некоторые файлы повреждены или отсутствуют.\nПереустановите игру.", ok_action=Quit(confirm=False))
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
