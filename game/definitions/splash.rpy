# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# В этом файле прописаны заставка, дисклеймер и оформление меню игры.

# Это текстовое изображение показывает сообщение в центре экрана.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Оформление главного меню
# Эти изображения с трансформациями выводят на экран логотип игры, спрайты персонажей,
# а также плашки главного меню и меню паузы.

# Это изображение выводит на экран логотип DDLC на привычном месте.
image menu_logo:
    "mod_assets/DDLCModTemplateLogo.png"
    # im.Composite((512, 512), (0, 0), recolorize("mod_assets/logo_bg.png"), (0, 0), "mod_assets/logo_fg.png")
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# Задний план главного меню, оформленный в горошек.
image menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_move

# Задний план меню паузы, оформленный в горошек.
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_loop

# Это изображение с трансформацией накладывает переход из белой заливки в главное меню.
image menu_fade:
    "white"
    menu_fadeout

# Эти изображения с трансформациями расставляют спрайты персонажей на нужных местах в главном меню с соответствующей им анимацией.
image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# Те же спрайты, что и выше, но оформленные для «призрачной» пасхалки, которая
# имеет низкий шанс срабатывания.
image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# Искажённый спрайт Сайори, который появляется после прохождения первого акта.
image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

# Плашка, отображаемая в главном меню/меню паузы.
image menu_nav:
    "gui/overlay/main_menu.png"
    #recolorize("gui/overlay/main_menu.png", "#ffbde1")
    menu_nav_move

## Спецэффекты главного меню
# В этом разделе прописаны трансформации и изображения с ними, которые отвечают за
# эффекты меню при запуске игры.

# Это изображение с трансформациями выводит на экран эффект взрыва частиц в главном
# меню, когда логотип «ударяется» о плашку.
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

# Эта трансформация отвечает за затухание частиц.
transform particle_fadeout:
    easeout 1.5 alpha 0

# Эта трансформация сначала «роняет» задний план меню, а потом перемещает в верхний левый угол.
transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

# Эта трансформация зацикливает перемещение заднего плана меню в угол.
transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

# Эта трансформация «роняет» логотип игры на определённое для него место.
transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

# Эта трансформация отвечает за «выскакивание» плашки меню.
transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

# Эта трансформация растворяет экран главного меню.
transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

# Эта трансформация принимает значения оси Z, оси X и масштаба и расставляет спрайты
# персонажей в заранее определённые места.
transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

## Логотипы в заставке
# Это изображение выводит на экран логотип разработчиков при запуске игры.
image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# Резерв для логотипа фан-группы.
# image my_intro:
#     truecenter
#     "white"
#     0.5
#     "путь/к/логотипу.png" with Dissolve(0.5, alpha=True)
#     2.5
#     "white" with Dissolve(0.5, alpha=True)
#     0.5

# Остатки кода из ранней версии DDLC, который выводит на экран сообщение
# при запуске игры.
image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

## Изображения, которые отображаются во время дисклеймера.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## Задаёт постоянной переменной значение False, чтобы предложить игроку выбор языка.
default persistent.has_chosen_language = False

## Задаёт переменной первого запуска значение False, чтобы отобразить дисклеймер.
default persistent.first_run = False

## Дисклеймер (отказ от ответственности) при запуске игры
## Этот лейбл вызывает дисклеймер, который появляется при запуске игры.
label splashscreen:
    $ initialize_characters_folder()
    ## Если условия соблюдены, показывает предложение удалить существующие сохранения.
    if not persistent.first_run and len(renpy.list_saved_games(fast=True)) > 0:
        $ quick_menu = False
        scene black
        menu:
            "Обнаружены файлы сохранений. Хотите удалить их и начать игру заново?"
            "Да, удалить существующие сохранения.":
                "Файлы сохранений удаляются...{nw}"
                python:
                    delete_all_saves()
                    renpy.utter_restart()
            "Нет, продолжить с того момента, где я остановился.":
                python:
                    restore_characters()
                    persistent.first_run = True

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        # Показать выбор языка перед дисклеймером, если у модификации имеются
        # переводы и игрок ещё не выбирал язык.
        if not persistent.has_chosen_language and translations:
            if _preferences.language is None:
                call screen language_selector

        # Вы можете редактировать это сообщение, но вы ДОЛЖНЫ пояснить, что ваша модификация
        # никоим образом не связана с Team Salvato, требовать, чтобы игрок сначала
        # прошёл оригинальную игру, указать на наличие спойлеров и откуда можно
        # скачать игру (предпочтение стоит отдать сайту https://ddlc.moe).
        #
        # ...Да, это применимо даже в том случае, если в вашей модификации нет спойлеров к оригинальной игре.
        "«[config.name]» является фанатской модификацией к игре «Литературный клуб \"Тук-тук!\"», которая никак не связана с Team Salvato."
        "В неё рекомендуется играть только после прохождения оригинальной игры, также в модификации имеются спойлеры, связанные с последней."
        "Также для игры в эту модификацию необходимы файлы игры «Литературный клуб \"Тук-тук!\"», саму игру можно скачать на сайте: {a}https://ddlc.moe{/a} или в Магазине Steam."

        menu:
            "Играя в «[config.name]», вы соглашаетесь с тем, что прошли полностью игру «Литературный клуб \"Тук-тук!\"» и готовы к любым спойлерам."
            "Я согласен.":
                $ persistent.first_run = True

        scene tos2
        with Dissolve(1.5)
        pause 1.0

        # Проверяем, запущена ли программа для стриминга/записи, и если да – предупреждаем игрока.
        if is_user_streaming():
            call screen dialog("Обнаружено ПО для стриминга/записи. В целях защиты вашей конфиденциальности был включён режим летсплейщика.",
                [Hide("dialog"), Return()])
        scene white

    # Этот блок Python указывает, должен ли сработать триггер раннего убийства
    # Сайори. Сам блок был закомментирован в целях безопасности, но его можно
    # использовать, если в этом будет необходимость.

    # python:
    #     s_kill_early = None
    #     if persistent.playthrough == 0:
    #         try: open(f"{user_dir}/characters/sayori.chr")
    #         except IOError: s_kill_early = True
    #     if not s_kill_early:
    #         if persistent.playthrough <= 2 and persistent.playthrough != 0:
    #             try: open(f"{user_dir}/characters/monika.chr")
    #             except IOError: open(f"{user_dir}/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    #         if persistent.playthrough <= 1 or persistent.playthrough == 4:
    #             try: open(f"{user_dir}/characters/natsuki.chr")
    #             except IOError: open(f"{user_dir}/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    #             try: open(f"{user_dir}/characters/yuri.chr")
    #             except IOError: open(f"{user_dir}/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    #         if persistent.playthrough == 4:
    #             try: open(f"{user_dir}/characters/sayori.chr")
    #             except IOError: open(f"{user_dir}/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    # Выбирает случайным образом особые стихи, которые появятся во время прохождения второго акта игры.
    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]

            # Задаёт диапазон для выбора. В оригинальной игре имеется
            # 11 особых стихотворений.
            a = list(range(1,12))

            # Выбирает три уникальных стихотворения, которые игрок увидит во втором акте.
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    # Сохраняет путь к корневому каталогу игры. Используется в третьем акте.
    $ basedir = config.basedir.replace('\\', '/')

    # Загружает конкретный лейбл, если переменная автозагрузки не пуста.
    if persistent.autoload:
        jump autoload

    $ config.allow_skipping = False
    # Показывает «призрачное» меню, если игрок проходит второй акт и все условия соблюдены.
    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

    # Этот блок проверяет, был ли удалён файл «sayori.chr» после прохождения дисклеймера, и если да –
    # показывает сцену раннего убийства. Сам блок был закомментирован в целях безопасности, но его можно
    # использовать, если в этом будет необходимость.

    # if s_kill_early:
    #     show black
    #     play music "bgm/s_kill_early.ogg"
    #     $ pause(1.0)
    #     show end with dissolve_cg
    #     $ pause(3.0)
    #     scene white
    #     show expression "images/cg/s_kill_early.png":
    #         yalign -0.05
    #         xalign 0.25
    #         dizzy(1.0, 4.0, subpixel=False)
    #     show white as w2:
    #         choice:
    #             ease 0.25 alpha 0.1
    #         choice:
    #             ease 0.25 alpha 0.125
    #         choice:
    #             ease 0.25 alpha 0.15
    #         choice:
    #             ease 0.25 alpha 0.175
    #         choice:
    #             ease 0.25 alpha 0.2
    #         choice:
    #             ease 0.25 alpha 0.225
    #         choice:
    #             ease 0.25 alpha 0.25
    #         choice:
    #             ease 0.25 alpha 0.275
    #         choice:
    #             ease 0.25 alpha 0.3
    #         pass
    #         choice:
    #             pass
    #         choice:
    #             0.25
    #         choice:
    #             0.5
    #         choice:
    #             0.75
    #         repeat
    #     show noise:
    #         alpha 0.1
    #     with Dissolve(1.0)
    #     show expression Text("Теперь все будут счастливы.", style="sayori_text"):
    #         xalign 0.8
    #         yalign 0.5
    #         alpha 0.0
    #         600
    #         linear 60 alpha 0.5
    #     pause
    #     $ renpy.quit()

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    # Удалите паузу в 2,5 секунды и раскомментируйте нижеприведённые строки, если хотите вставить свой логотип
    $ pause(2.5)
    # $ pause(1.5)
    hide intro with Dissolve(0.5, alpha=True)
    # show my_intro with Dissolve(0.5, alpha=True)
    # $ pause(1.5)
    # hide my_intro with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    $ pause(1.5)
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ pause(0.5)
    $ config.allow_skipping = True
    return

# Этот сценарий запускается, если файл «monika.chr» был удалён до начала новой игры.
# Сценарий был закомментирован в целях безопасности, но его можно
# использовать, если в этом будет необходимость.

# label ch0_kill:
#     $ s_name = _("Сайори")
#     show sayori 1b zorder 2 at t11
#     s "..."
#     s "..."
#     s "Ч-что..."
#     s 1g "..."
#     s "Это..."
#     s "Что это?.."
#     s "О нет..."
#     s 1u "Нет..."
#     s "Этого не может быть."
#     s "Такого просто не может быть."
#     s 4w "Что это?"
#     s "Что я такое?"
#     s "Стойте!"
#     s "ПУСТЬ ЭТО ПРЕКРАТИТСЯ!"

#     $ delete_character("sayori")
#     $ delete_character("natsuki")
#     $ delete_character("yuri")
#     $ delete_character("monika")
#     $ renpy.quit()
#     return

## Этот лейбл отвечает за особую логику, которая должна выполняться после загрузки сохранения.
label after_load:
    $ restore_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    # Этот блок проверяет, находимся ли мы на сценке покончившей с собой Юри во втором акте, и если да – возвращает
    # на эту сценку. Блок был закомментирован в целях безопасности, но его можно
    # использовать, если в этом будет необходимость.

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     if persistent.yuri_kill >= 1380:
    #         $ persistent.yuri_kill = 1440
    #     elif persistent.yuri_kill >= 1180:
    #         $ persistent.yuri_kill = 1380
    #     elif persistent.yuri_kill >= 1120:
    #         $ persistent.yuri_kill = 1180
    #     elif persistent.yuri_kill >= 920:
    #         $ persistent.yuri_kill = 1120
    #     elif persistent.yuri_kill >= 720:
    #         $ persistent.yuri_kill = 920
    #     elif persistent.yuri_kill >= 660:
    #         $ persistent.yuri_kill = 720
    #     elif persistent.yuri_kill >= 460:
    #         $ persistent.yuri_kill = 660
    #     elif persistent.yuri_kill >= 260:
    #         $ persistent.yuri_kill = 460
    #     elif persistent.yuri_kill >= 200:
    #         $ persistent.yuri_kill = 260
    #     else:
    #         $ persistent.yuri_kill = 200
    #     jump expression persistent.autoload

    # [ВНИМАНИЕ: Если вы раскомментировали блок выше, обязательно измените `if` ниже на `elif`.]
    # Этот блок проверяет, совпадают ли локальная и постоянная переменные анти-чита,
    # и если нет – блокирует загрузку и выводит на экран особое послание.
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "Сохранение не может быть загружено."
        "Ты пытаешься смухлевать?"
        $ m_name = _("Моника")
        show monika 1 at t11
        if not persistent.playername:
            m "Ты такой смешной."
        else:
            m "Ты такой смешной, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        # Если игрок проходит игру впервые, появится подсказка о кнопке пропуска.
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog(_("Подсказка: используйте кнопку «Пропуск» для\nбыстрой прокрутки уже прочитанного текста."), ok_action=Return())
    return

## Этот лейбл загружает лейбл, записанный в переменную автозагрузки.
label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     $ persistent.yuri_kill += 200

    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

# Этот лейбл используется для принудительного возврата игрока на сценку
# с покончившей с собой Юри из главного меню. Лейбл был закомментирован в целях
# безопасности, но его можно использовать, если в этом будет необходимость.

# label autoload_yurikill:
#     if persistent.yuri_kill >= 1380:
#         $ persistent.yuri_kill = 1440
#     elif persistent.yuri_kill >= 1180:
#         $ persistent.yuri_kill = 1380
#     elif persistent.yuri_kill >= 1120:
#         $ persistent.yuri_kill = 1180
#     elif persistent.yuri_kill >= 920:
#         $ persistent.yuri_kill = 1120
#     elif persistent.yuri_kill >= 720:
#         $ persistent.yuri_kill = 920
#     elif persistent.yuri_kill >= 660:
#         $ persistent.yuri_kill = 720
#     elif persistent.yuri_kill >= 460:
#         $ persistent.yuri_kill = 660
#     elif persistent.yuri_kill >= 260:
#         $ persistent.yuri_kill = 460
#     elif persistent.yuri_kill >= 200:
#         $ persistent.yuri_kill = 260
#     else:
#         $ persistent.yuri_kill = 200
#     jump expression persistent.autoload

# Этот лейбл устанавливает заглавную тему в качестве темы главного меню,
# прежде чем появится само меню.
label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

# Этот лейбл отвечает за особую логику при завершении работы игры.
label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
