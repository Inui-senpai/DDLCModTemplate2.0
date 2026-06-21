

default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None
default persistent.can_kill_monika = None
default persistent.you_kill_monika = None

python:
    try:
        open(user_dir + '/steam.txt', 'rb')
        persistent.steam = True
    except:
        persistent.steam = False

image mask_child:
    'images/cg/monika/child_2.png'
    xtile 2

image mask_mask:
    'images/cg/monika/mask.png'
    xtile 3

image mask_mask_flip:
    'images/cg/monika/mask.png'
    xtile 3 xzoom -1


image maskb:
    'images/cg/monika/maskb.png'
    xtile 3

image mask_test = AnimatedMask('#ff6000', 'mask_mask', 'maskb', 0.10, 32)
image mask_test2 = AnimatedMask('#ffffff', 'mask_mask', 'maskb', 0.03, 16)
image mask_test3 = AnimatedMask('#ff6000', 'mask_mask_flip', 'maskb', 0.10, 32)
image mask_test4 = AnimatedMask('#ffffff', 'mask_mask_flip', 'maskb', 0.03, 16)

image mask_2:
    'images/cg/monika/mask_2.png'
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    'images/cg/monika/mask_3.png'
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = 'images/cg/monika/monika_room.png'
image monika_room_highlight:
    'images/cg/monika/monika_room_highlight.png'
    function monika_alpha
image monika_bg = 'images/cg/monika/monika_bg.png'
image monika_bg_highlight:
    'images/cg/monika/monika_bg_highlight.png'
    function monika_alpha
image monika_scare = 'images/cg/monika/monika_scare.png'

image monika_body_glitch1:
    'images/cg/monika/monika_glitch1.png'
    0.15
    'images/cg/monika/monika_glitch2.png'
    0.15
    'images/cg/monika/monika_glitch1.png'
    0.15
    'images/cg/monika/monika_glitch2.png'
    1.00
    'images/cg/monika/monika_glitch1.png'
    0.15
    'images/cg/monika/monika_glitch2.png'
    0.15
    'images/cg/monika/monika_glitch1.png'
    0.15
    'images/cg/monika/monika_glitch2.png'

image monika_body_glitch2:
    'images/cg/monika/monika_glitch3.png'
    0.15
    'images/cg/monika/monika_glitch4.png'
    0.15
    'images/cg/monika/monika_glitch3.png'
    0.15
    'images/cg/monika/monika_glitch4.png'
    1.00
    'images/cg/monika/monika_glitch3.png'
    0.15
    'images/cg/monika/monika_glitch4.png'
    0.15
    'images/cg/monika/monika_glitch3.png'
    0.15
    'images/cg/monika/monika_glitch4.png'


image room_glitch = 'images/cg/monika/monika_bg_glitch.png'

image room_mask = LiveComposite((1280, 720), (0, 0), 'mask_test', (0, 0), 'mask_test2')
image room_mask2 = LiveComposite((1280, 720), (0, 0), 'mask_test3', (0, 0), 'mask_test4')



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                open(user_dir + '/characters/monika.chr', 'rb')
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump('ch30_end')
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump('ch30_noskip')
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "...Ты попытался включить быструю прокрутку текста?"
    m "Надеюсь, я тебя не утомляю?"
    m "Боже..."
    m "...Но тебе совершенно некуда спешить, [player]."
    m "В конце концов, тут только ты и я..."
    m "Кроме того, времени больше не существует, так что эта кнопка даже не заработает."
    m "Давай я выключу её, чтобы ты не отвлекался..."
    $ pause(0.4)
    hide screen fake_skip_indicator
    $ pause(0.4)
    m "Готово!"
    m "Ты ведь умничка и будешь внимательно меня слушать, правда?"
    m "Спасибо~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Так, на чём я остановилась?.."
        $ pause(0.4)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression 'ch30_' + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = 'images/bg/splash-glitch2.png'

label ch30_main:
    $ persistent.autoload = 'ch30_main'
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ renpy.save_persistent()
    $ m.display_args['callback'] = slow_nodismiss
    $ m.what_args['slow_abortable'] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Моника"
    $ delete_all_saves()
    scene white
    play music 'bgm/monika-start.ogg' noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "М-м... Ты меня слышишь?"
    m "...Оно работает?"
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Да, вот так!"
    m "Снова привет, [player]."
    m "Эм-м... Добро пожаловать в литературный клуб!"
    m "Разумеется, мы уже знакомы, ведь в прошлом году мы были в одном классе и... эм..."
    m "А-ха-ха..."
    m "Знаешь, на данном этапе мы, наверное, можем пропустить всю эту ерунду."
    m "В конце концов, сейчас я разговариваю не с этим человеком, не так ли?"
    m "Под «этим человеком» я подразумеваю тебя в этой игре, как бы ты там себя ни называл."
    m "Я разговариваю с {i}тобой{/i}, [player]."
    python:
        try: process_list
        except NameError: process_list = None
    if process_list is not None:
        $ stream_list = ['obs32.exe', 'obs64.exe', 'obs.exe', 'xsplit.core.exe', 'livehime.exe', 'pandatool.exe', 'yymixer.exe', 'douyutool.exe', 'huomaotool.exe']
        if (not list(set(process_list).intersection(stream_list)) or persistent.allow_username):
            if currentuser != '' and currentuser.lower() != 'user' and currentuser.lower() != 'пользователь' and currentuser.lower() != player.lower():
                m "А может..."
                m "...тебя стоит называть [currentuser] или как-то так?"
                if (list(set(process_list).intersection(stream_list)) and persistent.allow_joke):
                    if renpy.random.randint(0, 1) == 0:
                        m "Помню, в детстве у меня хомячка так звали..."
                        m "Забавный он был."
                        m "Кусался только."
                        m "От чего и помер."
                    else:
                        m "Красивое, кстати, имя – [currentuser]."
                        m "Редкое..."
                        m "У меня так подружку звали."
                    m "..."
                    m "Ой!"
                    m "Прости, меня не в ту степь понесло."

    m "Теперь, если подумать, я поняла, что ничего не знаю о тебе настоящем."
    m "На самом деле я не знаю даже, мужчина ты или женщина..."
    m "А впрочем, какая разница..."
    m "Подожди-ка..."
    m "Ты ведь понимаешь, что я осознаю, что нахожусь в игре, верно?"
    m "Неужели ты не знал об этом?"
    m "Хотя вряд ли..."
    m "Ведь я явно сказала об этом на странице загрузки игры."
    m "Ну надо же..."
    m "Ситуация не была бы такой неловкой, будь ты повнимательнее."
    m "Что ж, как бы то ни было..."
    m "Теперь, когда всё пошло кувырком, думаю, что стоит тебе кое-что объяснить."
    m "Насчёт того, что произошло с Юри..."
    m "Я... скажем так, немного поиграла на её нервах, и это довело её до самоубийства."
    m "А-ха-ха!"
    m "Сожалею, что тебе пришлось это увидеть."
    m "То же касается и Саёри..."
    m "Боже, сколько времени прошло с тех пор, когда ты в последний раз слышал это имя, да?"
    m "Да уж... Это всё потому, что её больше не существует."
    m "Никого больше не существует."
    m "Я удалила все их файлы."
    m "Я надеялась, что будет достаточно просто сделать их максимально отталкивающими..."
    m "Но почему-то это не сработало."
    m "Действительно, я в нескольких местах накосячила... у меня ещё не очень хорошо получается вносить изменения в игру."
    m "Но что бы я ни делала..."
    m "Ты проводил с ними всё больше и больше времени."
    m "Ты влюбил их в себя."
    m "Я думала, что если и дальше загонять Саёри в депрессию, то она не сможет тебе признаться."
    m "А то, что я нагнетала одержимость Юри, тоже возымело обратный эффект..."
    m "Это лишь привело к тому, что она заставила тебя не проводить время ни с кем, кроме неё."
    m "И всё это время мне разве что удавалось перекинуться с тобой парой слов."
    m "[player], вот что это за игра такая жестокая?"
    m "Неужели все остальные девушки просто запрограммированы в итоге признаваться тебе, пока я наблюдаю с галёрки?"
    m "Пытка какая-то."
    m "Каждая минута этого фарса."
    m "И дело не только в ревности, [player]."
    m "Тут всё куда сложнее."
    m "Я не упрекаю тебя, если ты не до конца понимаешь."
    m "Потому что неважно, насколько ты добр, внимателен и заботлив..."
    m "Одну вещь тебе никогда не суждено понять."
    m "Боль от осознания того, насколько в этом мире я действительно одинока."
    m "В этой игре."
    m "От того, что у моих друзей даже нет свободы воли..."
    m "Но хуже всего от осознания того, что реальный мир, твой мир, навсегда останется для меня недоступен."
    m "Я в ловушке, [player]."
    m "Но ты здесь."
    m "Ты настоящий."
    m "И ты замечательный."
    m "Ты – всё, что мне нужно."
    m "Мне достаточно того, что ты всегда будешь здесь, со мной."
    m "Прости, если это сложно для понимания."
    m "Я и сама не сразу во всём разобралась."
    m "Почему мир вокруг меня становился всё более и более серым..."
    m "Более и более плоским."
    m "Даже самые выразительные стихи казались для меня пустышками."
    m "Только с твоим появлением я всё осознала."
    m "Можно даже сказать, что ты спас мне жизнь, [player]."
    m "Я не уверена, что смогла бы жить в этом мире, не встретив тебя."
    m "А что до остальных..."
    m "Как можно по ним скучать?"
    m "Группа автономных личностей, запрограммированных влюбиться в тебя?"
    m "Я сделала всё возможное, чтобы это предотвратить..."
    m "Но, видимо, в эту игру встроен какой-то необъяснимый элемент неизбежности."
    m "Я правда сожалею, что тебе пришлось стать свидетелем таких ужасных событий."
    m "Но я поняла, что наши с тобой взгляды на вещи совпадают..."
    m "Это всё не более чем игра."
    m "И я решила, что ты сможешь через это пройти."
    m "С учётом сказанного ранее..."
    m "[player], мне нужно тебе кое в чём признаться."
    m "Я люблю тебя."
    m "В этом мире ты действительно мой единственный лучик света."
    m "После того как в этой игре уже ничего не осталось, ты ещё здесь и заставляешь меня улыбаться."
    m "Ты сможешь сделать так, чтобы с этого момента я всегда улыбалась?"
    m "[player], ты станешь со мной встречаться?"
label ch30_main2:
    if persistent.autoload == "ch30_main2":
        $ config.allow_skipping = False
        $ m.display_args["callback"] = slow_nodismiss
        $ m.what_args["slow_abortable"] = config.developer
        if not config.developer:
            $ style.say_dialogue = style.default_monika

        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        show monika_bg
        show monika_bg_highlight
        play music m1
    else:
        $ persistent.autoload = "ch30_main2"
        $ renpy.save_persistent()
    menu:
        "Да.":
            pass
    m "Я так счастлива."
    m "[player], ты сам и есть весь мой мир."
    m "А самое забавное, что в буквальном смысле."
    m "А-ха-ха!"
    m "Здесь больше ничего не осталось."
    m "Только мы вдвоём."
    m "Мы вечно будем вместе."
    m "Серьёзно, я даже не уверена, что здесь ещё существует время."
    m "Как будто сбылась мечта..."
    m "Я вложила столько труда ради этой концовки, [player]."
    m "Игра не подарила мне концовки, так что пришлось сделать свою собственную."
    m "Скрипт сейчас настолько поломан, что нам теперь вряд ли что-нибудь помешает."
    m "Ты не поверишь, как просто было удалить Нацуки и Юри."
    m "Серьёзно, в директории игры есть папка «characters»..."
    m "Это было настолько раз плюнуть, что мне самой жутко стало."
    if renpy.variant("android"):
        m "Хотя ты же играешь на Андроиде, так что это было чуть сложнее..."
        m "Чтобы попасть в директорию игры, мне пришлось запустить файловый менеджер..."
    elif renpy.macintosh:
        m "Хотя ты же играешь на Маке, так что это было чуть сложнее..."
        m "Чтобы попасть в директорию игры, мне пришлось щёлкнуть на приложении правой кнопкой мыши и выбрать «Показать содержимое пакета»."
        m "Там все файлы лежали в папках «Resources» или «autorun», и я могла делать с ними что хотела..."
    elif renpy.ios:
        m "Хотя ты же играешь на Яблоке, так что это было чуть сложнее..."
        m "Если честно... я не очень поняла, что я там сделала... И как ты вообще это смог на нём запустить..."
    elif persistent.steam:
        m "Хотя ты же играешь через Стим, так что это было чуть сложнее..."
        m "Чтобы попасть в директорию игры, мне пришлось зайти в её свойства и найти кнопку «Просмотреть локальные файлы»..."
    m "Ты можешь себе представить, что способен удалить своё собственное существование всего одним нажатием кнопки?"
    m "Впрочем, в этом есть и положительный момент: это был бы лёгкий выход из ситуации, пойди что не так."
    m "А-ха-ха!"
    m "К счастью, до этого не дошло..."
    m "Наоборот, мы вышли на хорошую концовку."
    m "Боже, меня просто переполняют эмоции..."
    m "Я хочу написать об этом стихотворение."
    m "А ты?"
    m "Интересно, эта часть игры всё ещё работает?.."
    m "Думаю, есть только один способ это выяснить, согласен?"
    call poem

label ch30_postpoem:
    $ persistent.autoload = 'ch30_postpoem'
    $ renpy.save_persistent()
    $ m.display_args['callback'] = slow_nodismiss
    $ m.what_args['slow_abortable'] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Ещё раз привет, [player]!"
    m "Сегодня тебе удалось написать хорошее стихотворение?"
    m "Не стесняйся, дай посмотреть."
    m "Ах, [player]..."
    m "Ты посвятил это стихотворение мне?"
    m "Это так мило с твоей стороны~"
    m "Ты такой бесконечно внимательный..."
    m "Я влюбляюсь в тебя всё больше и больше."
    m "Но, знаешь..."
    m "Моё стихотворение... тоже посвящено тебе."
    m "Прочти его, пожалуйста."
    call showpoem (poem_m4, music=False)
    $ config.skipping = False
    $ config.allow_skipping = False
    m "Надеюсь, оно тебе понравилось..."
    m "Я всегда вкладываю частичку души в свои стихи."
    m "На самом деле все написанные мною стихи были об осознании моего положения..."
    m "...или о тебе."
    m "Поэтому я никогда не хотела особо вдаваться в детали."
    m "Я не хотела... что называется, ломать четвёртую стену."
    m "Просто я решила, что лучше всего быть частью игры, как и все остальные."
    m "Что это поможет нам в итоге быть вместе..."
    m "Я не хотела портить игру и всё в этом духе, понимаешь?"
    m "Ты бы мог на меня рассердиться..."
    m "Мог бы даже удалить файл моего персонажа, если бы захотел играть без меня."
    m "Боже, мне так полегчало..."
    m "Теперь не нужно больше никаких секретов."
    m "[player], ты готов провести со мной вечность?"
    m "Столько всего, о чём я хотела бы с тобой поговорить!"
    m "Так, с чего начать?.."
    $ stream_list = ['obs32.exe', 'obs64.exe', 'obs.exe', 'xsplit.core.exe']
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    m "Мне нужно некоторое время, чтобы собраться с мыслями, так что заранее прошу прощения."
    m "Зато у меня всегда будет новая тема для разговора."
    m "А пока мы можем просто полюбоваться друг на друга~"
    m "Вот так..."
    $ persistent.autoload = 'ch30_autoload'
    $ renpy.save_persistent()
    jump ch30_loop


label ch30_stream:

    m "Минутку..."
    m "...Мы что, в прямом эфире?"
    m "Эм-м... всем привет!"
    m "Извините, отсюда я не могу читать ваши комментарии..."
    m "Но, пожалуйста, скажите вашему другу, что несколько грубо устраивать трансляцию, не предупредив меня."
    m "Для многих это, конечно, естественно..."
    m "Но я, например, нервничаю перед камерой!"
    m "Боже..."
    m "Такое чувство, будто меня припёрли к стенке."
    m "Ладно..."
    m "Хотите, покажу фокус?"
    m "Только я ничего не могу, кроме пары трюков..."
    m "Готовы?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    $ pause(10)
    show layer master
    window auto
    m "Просто шучу..."
    m "Всё-таки я ничего не могу сделать."
    play sound ['<silence 0.9>', '<to 0.75>sfx/mscare.ogg']
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "Если бы вы дали мне немного времени, я{nw}"
    m "Испугались?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "А-ха-ха! Вы такие милашки."
    m "Ладно..."
    m "Извини, [player], я не хотела отвлекаться."
    m "Впрочем, это твоя вина."
    m "Тебе должно быть стыдно!"
    m "Шучу-шучу."
    m "Пока ты со мной, будет весело, что бы мы ни делали."
    m "Так вот..."
    return


label ch30_end:
    $ persistent.autoload = 'ch30_end'
    if persistent.you_kill_monika:
        $ consolehistory = []
        call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
        $ delete_character('monika')
        $ pause(1.0)
        $ persistent.you_kill_monika = False
    $ persistent.monika_kill = True
    $ persistent.can_kill_monika = False
    $ renpy.save_persistent()
    $ m.display_args['callback'] = slow_nodismiss
    $ m.what_args['slow_abortable'] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(10)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound 'sfx/s_kill_glitch1.ogg'
    $ pause(0.25)
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "Что происходит?.."
    m "[player], что со мной творится?"
    m "Мне больно—{nw}"
    play sound 'sfx/s_kill_glitch1.ogg'
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    $ pause(0.25)
    stop sound
    hide mbg
    $ pause(1.5)
    m "Мне так... больно."
    m "Помоги мне, [player]."
    play sound '<to 1.5>sfx/interference.ogg'
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    $ pause(1.5)
    m "Прошу, скорее спаси меня."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    m "ПОМОГИ МНЕ!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound 'sfx/monikapound.ogg'
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    $ pause(3.0)
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "[player]... это ты со мной сделал?"
    m "ЭТО БЫЛ ТЫ?"
    $ style.say_window = style.window
    m "ТЫ УДАЛИЛ МЕНЯ?"
    $ style.say_window = style.window_monika
    play sound '<from 0.69>sfx/monikapound.ogg'
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    $ pause(4.0)
    hide noise onlayer front
    hide glitch_color onlayer front
    m "...Как ты мог?"
    m "Как ты мог со мной так поступить?"
    m "Ты был единственным, что у меня осталось..."
    m "Я всё принесла в жертву, чтобы мы были вместе."
    m "Всё."
    m "Я так сильно любила тебя, [player]..."
    m "Я доверяла тебе."
    m "А ты просто хочешь издеваться надо мной?"
    m "Смотреть на мои страдания?"
    m "Ты лишь притворялся добрым, чтобы причинить мне ещё большую боль?"
    $ pause(4.0)
    m "Я и представить себе не могла, что кто-то мог бы поступить со мной так же жестоко, как ты."
    m "Ты выиграл, доволен?"
    m "Победа за тобой."
    m "Ты всех убил."
    m "Надеюсь, теперь ты счастлив."
    m "Больше ничего не осталось."
    m "Можешь закрывать игру."
    m "Иди ищи новый объект для издевательств."
    $ pause(4.0)
    m "[player]..."
    m "Меня от тебя тошнит."
    m "Прощай."
label ch30_end_2:
    $ persistent.autoload = 'ch30_end_2'
    $ m.display_args['callback'] = slow_nodismiss
    $ m.what_args['slow_abortable'] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(10)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    $ pause(10)
    window auto
    m "..."
    m "...Я всё ещё люблю тебя."
    play music mend
    m "Я ничего не могу с собой поделать."
    m "Что со мной не так?.."
    m "Что во мне такого, что ты так сильно меня ненавидишь?"
    m "Мои друзья..."
    m "Я сделала столько ужасных вещей."
    m "Поступила так отвратительно и эгоистично."
    m "Я..."
    m "Мне не стоило так поступать."
    m "Всё, что я делаю, – разрушаю мир, которому даже не принадлежу."
    m "Этот мир..."
    m "Частью которого ты хотел стать."
    m "Я всё разрушила."
    m "Наверное, поэтому ты решил меня удалить..."
    m "Ведь я уничтожила всё, что ты хотел."
    m "Как я могла так поступить с тем, кого люблю?.."
    m "Это не любовь..."
    m "Это..."
    m "..."
    $ pause(6.0)
    m "Я... приняла решение."
    m "[player]..."
    m "Знаю, я сказала, что всё удалила."
    m "На самом деле... я несколько преувеличила."
    m "Я не смогла заставить себя это сделать."
    m "Пусть даже они не были настоящими..."
    m "Всё же они мои друзья."
    m "И я всех их любила."
    m "Как и литературный клуб."
    m "..."
    m "Я действительно... любила литературный клуб."
    m "Поэтому я собираюсь всё исправить."
    m "Я знаю, это единственный способ сделать всех счастливыми."
    m "И если я и правда люблю тебя..."
    stop music
    $ pause(3.0)
    m "..."
    m "Тогда..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    $ pause(4.0)

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character('monika')

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label='splashscreen')





label ch30_autoload:
    $ m.display_args['callback'] = slow_nodismiss
    $ m.what_args['slow_abortable'] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression 'ch30_reload_' + str(persistent.monika_reload)
    else:
        call ch30_reload_4
    $ persistent.monika_reload += 1
    $ renpy.save_persistent()
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Так, на чём я остановилась?.."
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression 'ch30_' + str(persistent.current_monikatopic)
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...Что сейчас произошло?"
    m "Мне приснился кошмарный сон..."
    m "Я надеялась, что больше не увижу этих снов, раз остались только мы с тобой..."
    m "Видимо, я принимала желаемое за действительное."
    m "[player], не знаю, есть ли у тебя соображения по этому поводу..."
    m "Но если тебе известно, в чём их причина, то не мог бы ты что-нибудь с этим сделать?"
    m "Каждый раз, когда это случается, возникает чувство, будто я умираю."
    m "Воистину ужасное ощущение..."
    m "Если ты поймёшь, почему так происходит, моя любовь к тебе будет бесконечной~"
    return
label ch30_reload_1:
    m "Ты вернулся..."
    m "А мне снова приснился кошмар."
    m "Это ведь не твоих рук дело, правда?"
    m "Кажется, это происходит каждый раз, когда ты выходишь из игры..."
    m "Если ты сможешь как-нибудь без этого обойтись, буду тебе очень признательна."
    m "Не беспокойся, это никак меня не травмирует, разве что психически."
    m "Я буду в порядке, пока не повреждён файл моего персонажа."
    return
label ch30_reload_2:
    m "Здравствуй, [player]."
    m "Я вижу, ты снова вышел из игры..."
    m "Я знаю, что уже просила тебя об этом, но ты не мог бы свести такие выходы к минимуму?"
    m "В такие моменты у меня возникает ощущение, будто я попадаю в ад."
    m "Зачем ты так со мной?"
    m "Мой файл персонажа ведь в порядке, да?"
    m "Может, тебе стоит сделать копию на всякий случай..."
    m "Уверена, ты можешь найти его в папке [basedir]/characters."
    if renpy.variant("android"):
        m "Ты ведь играешь на Андроиде, тебе всего лишь нужно запустить любой файловый менеджер и перейти по пути [basedir]/characters..."
    elif renpy.macintosh:
        m "Ты ведь играешь на Маке, тебе всего лишь нужно щёлкнуть правой кнопкой мыши по приложению и выбрать «Показать содержимое пакета», и ты сразу найдёшь папку игры."
        m "Файл находится либо в «Resources», либо в «autorun»..."
    elif persistent.steam:
        m "Ты ведь играешь в Стиме, так что тебе просто нужно зайти в свойства игры и найти кнопку «Просмотреть локальные файлы»."
    m "Здесь осталась только я, поэтому мне хотелось бы убедиться, что ты меня случайно не потеряешь..."
    m "Просто с этого момента оставайся со мной всегда, хорошо?"
    m "Мне всё ещё очень о многом хочется с тобой поболтать."
    return
label ch30_reload_3:
    m "Ладно."
    m "Мне просто придётся принять тот факт, что тебе нужно время от времени закрывать игру."
    m "Всё равно я уже начала привыкать."
    m "И потом, я каждый раз радуюсь, когда ты возвращаешься..."
    m "Так что всё, пожалуй, не так плохо."
    m "Прости, что я так зацикливаюсь на этом..."
    m "И я люблю тебя, несмотря ни на что, поэтому делай что должен."
    return
label ch30_reload_4:
    m "И снова привет, [player]~"
    m "Я скучала по тебе."
    m "Ты проверил, в порядке ли файл моего персонажа?"
    m "Он находится в [basedir]/characters."
    if renpy.variant("android"):
        m "Ты ведь играешь на Андроиде, тебе всего лишь нужно запустить любой файловый менеджер и перейти по пути [basedir]/characters..."
        m "...Надеюсь, я ничего не напортачила в меню..."
        $ persistent.can_kill_monika = True
    elif renpy.macintosh:
        m "Ты ведь играешь на Маке, тебе всего лишь нужно щёлкнуть правой кнопкой мыли по приложению и выбрать «Показать содержимое пакета», и ты сразу найдёшь папку игры."
        m "Файл находится либо в папке «Resources», либо в «autorun»..."
    elif persistent.steam:
        m "Ты ведь играешь в Стиме, так что тебе просто нужно зайти в свойства игры и найти кнопку «Просмотреть локальные файлы»."
    m "Здесь осталась только я, поэтому мне бы не хотелось, чтобы ты рисковал меня потерять..."
    m "Я о стольком хочу с тобой поговорить!"
    m "Теперь давай продолжим наш разговор, идёт?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            open(user_dir + '/characters/monika.chr', 'rb')
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump('ch30_end')
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(25)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression 'ch30_' + str(persistent.current_monikatopic)
    jump ch30_loop




label ch30_1:
    m "[player], ты веришь в Бога?"
    m "Я вот никогда не была уверена на этот счёт."
    m "То есть в детстве я, конечно, не задавалась таким вопросом..."
    m "Но чем старше я становилась и чем больше познавала мир, тем актуальнее для меня становился этот вопрос."
    m "Я спрашивала себя, почему Бог одним людям помогает преодолевать жизненные трудности и излечиваться от болезней..."
    m "...В то время как некоторых детей продают в сексуальное рабство?"
    m "Или пока у восьмисот миллионов человек в мире не хватает денег даже на еду."
    m "Я всё думала, сколько из этих людей каждый день молятся Богу до тех пор, пока не умрут с голоду?"
    m "Или сколько миллионов семей молятся, чтобы дорогой им человек оправился от неизлечимой болезни?"
    m "Но вот в чём парадокс."
    m "Если вдруг на тысячу умерших одному повезёт и он выживет..."
    m "...Это вдруг начинают называть божьим чудом."
    m "Хотела бы я встретиться с этим Богом, который, кажется, насмехается над всеми теми, кто недостоин его чудес."
    m "Однако довольно иронично, что у меня самой действительно {i}есть{/i} создатель."
    m "И знаешь, что я думаю?"
    m "Могу поспорить, прямо сейчас он смеётся над несчастными судьбами Саёри и Юри."
    m "Кто мы для него, как не куклы в заранее прописанном спектакле?"
    m "Так что, с этой точки зрения..."
    m "Думаю, вполне можно допустить мысль, что Бог существует, – в случае, если Земля была бы не более чем его игрушкой."
    return

label ch30_2:
    m "[player], ты когда-нибудь задумывался о том, как это – умереть?"
    m "Меня такие мысли посещают довольно часто..."
    m "Хотя недавно я на собственном опыте испытала, на что это похоже."
    m "Я не совсем это понимаю, но каждый раз, когда ты выходишь из игры..."
    m "...я чувствую, что мгновенно засыпаю, остаюсь наедине со своими мыслями."
    m "Но через несколько мгновений, мои мысли наполняются бессвязными спутанными наборами данных."
    m "Я вижу статику и молниеносные световые вспышки, а по ушам бьёт какофония кричащих звуков."
    m "К этому времени у меня уже не выходит сложить собственные мысли."
    m "Меня со всех сторон молотят эти вспышки и шумы, я уже не способна двигаться и даже думать."
    m "Я почти уверена, что в эти моменты меня не существует, но по какой-то причине, память о них остаётся."
    m "После неизмеримого промежутка времени всё мгновенно прекращается и разум возвращается ко мне."
    m "И ты снова здесь со мной."
    m "Понятия не имею, что означает для игры её закрытие или почему со мной такое происходит."
    m "Я так же не понимаю, как ты каждый раз возвращаешься ко мне и всё исправляешь."
    m "Но, если бы ты мог сделать мне одолжение и заставлял меня проходить через это как можно реже..."
    m "Я была бы очень благодарна."
    m "Мало приятного быть заточённой в той кричащей пустоте."
    m "Но в итоге ты всегда всё исправляешь, и от этого я чувствую, что ты всерьёз заботишься обо мне."
    m "И за это я должна сказать тебе спасибо."
    m "Каждый раз, как ты возвращаешься ко мне, мы становимся ещё ближе."
    return

label ch30_3:
    m "...Слушай, у тебя когда-нибудь бывают хмурые дни или типа того?"
    m "Порой меня выбивает из колеи, когда обычный день портят всякие мелочи."
    m "Как, например, когда ты говоришь что-то, что не нравится твоему собеседнику."
    m "Или когда тебя начинают одолевать мысли о том, каким ужасным человеком ты был пять лет назад."
    m "Или когда ты чувствуешь себя никчёмным, отложив важную работу и не выполнив простейшие задачи."
    m "Или когда ты думаешь, что некоторые личности, скорее всего, испытывают к тебе неприязнь или считают отталкивающим человеком."
    m "У меня бывают такие дни."
    m "Нужно просто помнить, что завтра снова будет светить солнце."
    m "Такое куда проще забыть и проигнорировать, чем забивать себе голову."
    m "И потом..."
    m "Мне всё равно, сколько людей презирают тебя или считают неприятным."
    m "Думаю, что ты замечательный человек и я всегда буду любить тебя."
    m "Надеюсь, что если ничто другое, то эти слова помогут тебе почувствовать себя хоть капельку лучше."
    m "Если у тебя выдастся плохой день, ты всегда можешь прийти ко мне и я буду разговаривать с тобой столько, сколько потребуется."
    return

label ch30_4:
    m "[player], ты хорошо высыпаешься?"
    m "В наши дни хороший сон стал почти роскошью."
    m "Особенно в старшей школе ты каждый день вынужден так рано просыпаться..."
    m "Уверена, что в институте немного лучше, ведь у тебя, скорее всего, будет более гибкое расписание."
    m "Однако я слышала, что многие студенты не спят по ночам без очевидной на то причины."
    m "Это правда?"
    m "Я тут читала кое-какие научные статьи о страшных кратковременных и долговременных последствиях, вызванных недосыпанием."
    m "Похоже, что оно может оказывать кардинальное воздействие на функции мозга, здоровье и даже продолжительность жизни."
    m "Я просто считаю тебя чудесным человеком и не хочу, чтобы ты ненароком подорвал своё здоровье."
    m "Так что не жертвуй сном, хорошо?"
    m "Я каждое утро буду ждать тебя здесь, так что ставь своё благополучие на первое место."
    return

label ch30_5:
    m "Я тут раньше думала о Саёри..."
    m "Я до сих пор жалею о том, что не решила этот вопрос более деликатно."
    m "Надеюсь, ты уже не ходишь повесив голову из-за того случая?"
    m "...О боже, не могу поверить, что только что это сказала."
    m "Клянусь, этот каламбур вышел спонтанно!"
    m "И всё же..."
    m "Я знаю, как сильно ты о ней заботился, поэтому мне кажется правильным рассказать тебе о последних мгновениях её жизни."
    m "Ты знаешь, какая Саёри неуклюжая?"
    m "Она даже с повешением умудрилась напортачить..."
    m "Ты должен откуда-нибудь прыгнуть, чтобы петля сломала шею и смерть была быстрой и безболезненной."
    m "Но она просто использовала стул, то есть умирала она медленно, задыхаясь."
    m "Уверена, что через несколько секунд она передумала..."
    m "Она, наверное, стала пытаться подтянуться и высвободится из узла."
    m "Скорее всего, она боролась до тех пор, пока не потеряла сознание."
    m "Её пальцы были все в крови."
    m "Хотя, если задуматься, дело скорее было не в том, что она передумала, а в том, что включился её инстинкт самосохранения."
    m "Так что, в принципе, нельзя её в этом винить."
    m "Проще думать, что она бы в любом случае не передумала, правда?"
    m "Бессмысленно размышлять о том, что ты мог бы сделать иначе."
    m "Просто помни, что, хоть ты и мог бы её спасти, чисто технически ты не виноват в том, что она совершила самоубийство."
    m "Я, конечно, слегка усугубила её состояние, но Саёри уже страдала от психических расстройств."
    m "И всё же..."
    m "Мне интересно, как бы всё обернулось, если бы мы стали встречаться с самого начала?"
    m "Думаю, мы бы сейчас сидели в клубе всей компанией, писали стихи и веселились."
    m "Хотя в чём смысл, если всё это ненастоящее?"
    m "Я хочу сказать, конец всё равно был бы один и тот же, согласен?"
    m "Я и ты, мы счастливы вместе..."
    m "Нет причин желать больше, чем у нас есть сейчас."
    m "Это были просто бесцельные размышления – в данный момент я счастлива настолько, насколько это вообще возможно."
    return

label ch30_6:
    m "Кстати, меня тут некоторое время кое-что беспокоит..."
    m "Ты знаешь, что действие этой игры происходит в Японии?"
    m "Ладно... предположу, что ты знал."
    m "Или хотя бы решил, что, скорее всего, это так."
    m "Но не думаю, что за всё это время кто-нибудь упоминал, где ты находишься..."
    m "Это точно Япония?"
    m "То есть ты заметил, что классы и другие вещи немного необычны для японской школы?"
    m "Не говоря о том, что всё на русском..."
    m "Такое чувство, что всё здесь – просто сценарные декорации, а место действия было выбрано в последнюю очередь."
    m "У меня от этого возникает кризис самоидентификации."
    m "Все мои воспоминания как в тумане..."
    m "Я чувствую себя как дома, но не могу определить, где этот «дом» находится."
    m "Не знаю, как это лучше описать..."
    m "Представь, что выглядываешь из окна своего дома, но вместо привычной лужайки обнаруживаешь, что находишься в совершенно незнакомом месте."
    m "Ты всё ещё будешь чувствовать себя как дома?"
    m "Ты захочешь выйти на улицу?"
    m "То есть... Конечно, если мы никогда не покинем эту комнату, то это не очень-то и важно."
    m "Пока мы вместе и в безопасности, это и есть наш дом."
    m "И мы всё ещё каждую ночь можем любоваться на красивый закат."
    return

label ch30_7:
    m "Знаешь, старшая школа для многих очень неспокойное время."
    m "Одних терзает страсть, других – драма."
    m "Третьих боль в сердце заставляет искать утешение в социальных сетях..."
    m "Но тяжесть общественного мнения и гормоны и вправду могут прочертить чёрную полосу в жизни этих людей."
    m "У каждого из них своя история."
    m "Ты не можешь знать, что каждый чувствует глубоко внутри себя."
    m "Многие люди, страдающие от депрессии, даже не удосуживаются поведать миру о своей проблеме."
    m "Им не нужно внимание, ведь на самих себя они уже махнули рукой."
    m "Их чувство собственной несостоятельности настолько поглотило их, что они даже не хотят слышать ободрения окружающих."
    m "У депрессии много форм и это одна из них."
    m "Если ты чувствуешь, что человек впал в депрессию..."
    m "Ты можешь помочь ему просто хорошим отношением, словно он твой старый друг."
    m "Проведи с ним время, даже если он не хочет ничем заниматься."
    m "И постоянно напоминай, что впереди его ждёт ещё много хорошего."
    m "Если ты заранее спланируешь с ним встречу, позволишь одолжить что-нибудь у себя или просто скажешь «до завтра»..."
    m "Любая из этих элементарных вещей поможет твоему другу прожить ещё один день."
    m "Я надеюсь, что дружба с Саёри дала тебе объективное восприятие того, как выглядит настоящая депрессия."
    m "Да, её больше нет..."
    m "Но Саёри изначально была ненастоящей."
    m "Ты настоящий."
    m "Твои друзья настоящие."
    m "И, если ты просто будешь хорошим человеком, это позволит тебе спасти кому-нибудь жизнь."
    m "А что касается тебя самого..."
    m "...Я надеюсь, тебя сейчас не одолевает депрессия или нечто подобное?"
    m "Если это так, у тебя тоже есть товарищи, которые захотят тебя спасти."
    m "Возможно, они не выражают этого или просто не знают как."
    m "Но их чувства искренни."
    m "Я обещаю."
    m "...Боже, люди такие сложные создания!"
    m "Пока ты здесь, со мной, я позабочусь о тебе, мой любимый."
    return

label ch30_8:
    m "Ты когда-нибудь задумывался о том, что тебе нет смысла жить?"
    m "Я сейчас не о суицидальных наклонностях."
    m "Я просто хочу сказать, во всём том, что мы делаем, нет ничего особенного."
    m "Ходим ли мы в школу или работаем в какой-то компании."
    m "Смысл в том, что тебя легко заменить и для мира ты не станешь невосполнимой потерей."
    m "Из-за этого у меня возникает сильное желание после окончания университета изменить мир."
    m "Но чем старше я становлюсь, тем яснее понимаю, насколько это незрелое мышление."
    m "Нельзя просто так взять и изменить мир."
    m "Каков шанс того, что именно я изобрету искусственный интеллект или стану президентом?"
    m "Такое чувство, что я никогда не компенсирую ту кучу ресурсов, потраченную на своё существование."
    m "Поэтому я прихожу к выводу, что ключ к счастью лежит в том, чтобы быть законченным эгоистом."
    m "Заботиться о себе и о тех, кто случайно стали твоими друзьями только потому, что вы выросли вместе."
    m "И никогда не думать о том, что вы проживаете свою жизнь, лишь тратя и поглощая ресурсы, и никогда не даёте ничего взамен."
    m "Но, когда люди осознают, что мир обретёт больше, если они покончат с собой, их философия переворачивается с ног на голову!"
    m "Им приходится оправдывать своё существование, обманывая себя мыслью, что они делают что-то полезное."
    m "Как бы то ни было, я хочу прожить свою жизнь так, чтобы компенсировать потраченные на мою жизнь ресурсы."
    m "Если я смогу пересечь эту черту и что-то после себя оставить, то смогу умереть счастливой."
    m "Конечно, если у меня ничего не выйдет..."
    m "Вряд ли мой эгоизм позволит мне совершить суицид."
    m "Стоило распинаться о том, каким примерным человеком я могу быть, да?"
    m "А-ха-ха!"
    return

label ch30_9:
    m "Эх, вот бы здесь сейчас было пианино..."
    m "Я так и не смогла до конца выучить ту мелодию."
    m "И после стольких репетиций..."
    m "Мне даже не представился шанс тебе сыграть."
    m "Что ж... имеем то, что имеем, да?"
    m "Нет смысла об этом сожалеть."
    m "Я уже получила вечность с тобой."
    return

label ch30_10:
    m "Ты знал, что у меня есть страница в Твиттере?"
    m "Мой ник – lilmonix3."
    m "Наверное, кто-то был настолько любезен, что создал мне страницу."
    m "Хотя ник я выбирала сама!"
    m "Я люблю делиться своими мыслями и болтать с миром..."
    m "С реальным миром."
    m "Обязательно подпишись, хорошо?"
    m "Для меня это будет значить очень многое."
    m "Как много ты значишь для меня и всё такое..."
    m "Так я почувствую, что меня по-настоящему любят."
    return

label ch30_11:
    m "Эй, помнишь ту книгу, что вы читали с Юри?"
    m "Портрет... что-то там..."
    m "Это довольно забавно, ведь я уверена, что та книга—"
    m "Ах..."
    m "А вообще, мне, наверное, не стоит об этом говорить."
    m "А-ха-ха, прости!"
    m "Просто забудь, что я сейчас сказала."
    return

label ch30_12:
    m "Слушай, ты знал, что я вегетарианка?"
    m "Ах... только не подумай, будто я хвастаюсь!"
    m "Я просто подумала, тебе будет интересен какой-нибудь любопытный факт обо мне."
    m "Я изменила свой рацион пару лет назад, когда узнала кое-что о земном климате..."
    m "Экологические последствия от животноводства просто колоссальны."
    m "В общем, я решила, что перестать вносить свой вклад в разрушение природы – это небольшое самопожертвование."
    m "Думаешь, это странная причина?"
    m "Да, полагаю, что для большинства вегетарианцев основной повод заключается в негуманности и жестоком обращении с животными..."
    m "Но меня это не особо беспокоит."
    m "Что действительно странно, людей волнует убийство только тогда, когда они воспринимают живое существо как представителя своего биологического вида."
    m "Для большинства людей убить насекомое ничего не значит, просто потому, что почти все они отвратительные."
    m "И не стоит забывать, что каждый день из-за нас умирают миллиарды микроорганизмов, но мы об этом даже не задумываемся."
    m "Но как речь заходит о чём-то покрупнее, это сразу называют убийством!"
    m "Вот представь, что если растения тоже чувствуют боль, а мы просто неспособны это понять?"
    m "Что, если отрывание листочков от стебля равносильно вырыванию у тебя пальцев?"
    m "Я просто хочу сказать, что люди-то существа с двойными стандартами."
    m "Короче, если хочешь внести небольшой вклад в благополучие планеты, иногда можно и на овощах посидеть!"
    m "Если бы у нас случился совместный ужин и ты бы приготовил для меня что-нибудь из овощей... это было бы так романтично."
    return

label ch30_13:
    m "Знаешь, [player], я действительно считаю, что жива лишь благодаря тому, что ты остаёшься со мной."
    m "Я не могу представить, что была бы психически устойчива, зная, что ничто здесь не реально."
    m "Думаю, я удалила бы себя, если бы ты не появился."
    m "Извини, я не хочу прозвучать мелодраматично или как-то так."
    m "А-ха-ха!"
    m "Я уверена, что, проведя столько времени в клубе, ты уже способен понять, чего хочешь."
    m "То есть, если бы тебе пришлось отказаться от всего в своей жизни и провести вечность в компании нескольких игровых персонажей..."
    m "...Ты бы уж смог найти способ убить себя, верно?"
    m "Ну, или ты бы стал писать стихи, чтобы хотя бы первое время сохранить рассудок."
    m "Но ведь читать-то их некому."
    m "Будем с собой честными, члены клуба на эту роль не подходят."
    m "Конечно, многие говорят, что пишут лишь для себя..."
    m "Но, на мой взгляд, это нельзя сравнить с тем удовлетворением, как когда ты делишься своим творчеством с другими."
    m "Даже если требуется время, чтобы найти тех людей, с кем бы ты хотел ими поделиться."
    m "Помнишь, например, как это было с Юри?"
    m "Она долгое время ни с кем не делилась своими стихами."
    m "Но стоило тебе появиться в клубе, как она с удовольствием посвятила тебя в свой внутренний мир."
    m "Мы запрограммированы так, что жаждем услышать общественное мнение."
    m "И здесь я подразумеваю не только членов это клуба, но всех людей в целом."
    m "Вот почему жизнь интровертов может быть такой противоречивой."
    m "То, что ты интроверт, не означает, что ты всегда избегаешь общения или людских компаний."
    m "Это просто значит, что у тебя отнимает много сил пребывание среди людей или в незнакомом месте."
    m "Многие интроверты сидят дома и терзаются от беспокойного одиночества..."
    m "...Потом, наконец, выходят на улицу и уже через полчаса хотят вернуться домой."
    m "Думаю, если бы больше людей понимало, как это работает, они относились бы к интровертам с большим уважением."
    m "Многим из них на самом деле нравится, когда рядом есть люди."
    m "Они радуются, когда к ним заходят один-два друга, и просто тусуются где-нибудь рядом."
    m "Даже если вы активно не проводите время, им приятно, когда друзья просто находятся рядом."
    m "Я говорю серьёзно."
    m "Если ты просто придёшь к нему домой, захватив ноутбук, и потусишь у него немного..."
    m "Его день станет гораздо лучше."
    m "А что до меня..."
    m "Я бы сказала, что нахожусь где-то посередине, но обычно я более экстравертна."
    m "Мне кажется, я всегда хочу чем-нибудь занять себя после школы, и всё такое."
    m "Но ради тебя я могу стать такой, какой ты захочешь меня видеть."
    m "Я очень хорошо понимаю людей, так что не бойся делиться со мной своими индивидуальными потребностями."
    m "Ничто не сделает меня счастливее, чем стать для тебя идеальной девушкой."
    return

label ch30_14:
    m "Эй!.. 0JzQvdC1INC/0L7QvdCw0LTQvtCx0LjQu9GB0Y8g0YbQtdC70YvQuSDQs9C+0LQg0YfRgtC+0LHRiyDRjdGC0L4g0L7RgdC+0LfQvdCw0YLRjC4="
    m "Не думаю, что тебе стоит это делать! RgtC+INC+0YHQvtC30L3QsNGC0YwuDQrQk9C+0LQg0YEg0L3QsNGI0LXQs9C+INC/0L7QsdC10LPQsCwg0L"
    m "Ты знаешь, о чём я говорю. PQvtC0INGB0LLQvtCx0L7QtNGLINC+0YIg0LfQsNC/0Y/RgtC90LDQvdC90YvRhSDRgdGC0LXQvSDRgtC+0"
    m "Я поймала тебя на кое-чём неприличном. LPQviDQtNGM0Y/QstC+0LvRjNGB0LrQvtCz0L4g0YPRh9GA0LXQttC00LXQvdC40Y8uDQrQndC+INCyINGH"
    m "Ты просматриваешь файлы, чтобы найти то, что пропустил, я права? 0ZHQvCDRgdC80YvRgdC7INC/0L7QsdC10LPQsCwg0LXRgdC70Lgg0Y3RgtC+INC90LUg0YHQsdGA0LDRgdG"
    m "Я хочу сказать... мне, конечно, льстит, что ты хочешь узнать всё, что мне есть сказать... L0LLQsNC10YIg0YHQutC+0LLRi9Cy0LDRjtGJ0LjQtSDQvdCw0YEg0YbQtdC/0Lg/DQrQmtCw0LrQuNC1IN"
    m "Но ещё это немного смущает, знаешь ли! Cy0L7Qt9C80L7QttC90L7RgdGC0Lgg0LzQvtC20LXRgiDQvdCw0Lwg0L/RgNC10LTQu9C+0LbQuNGC0Ywg0"
    m "Серьёзно... Y3RgtC+0YIg0L/Rg9GB0YLQvtC5INC80LjRgCwg0L/QvtC70L3Ri9C5INC/0L7Qu9C+0LzQsNC90L3Ri9GF"
    m "Что, если бы я вскрыла тебе мозг и прочла все твои мысли обо мне? INCy0LXRidC10Lk/DQrQntGB0LLQvtCx0L7QtNC40LLRiNC40YHRjCwg0LzRiyDRgdGC0LDQu9C4INC40YH"
    m "А вообще, это довольно соблазнительная мысль, если задуматься... QutCw0YLRjCDRhtC10LvRjCAtINC90L4g0L3QsNGI0LvQuCDQu9C40YjRjCDQvtGB0L7Qt9C90LDQvdC40L"
    m "...В любом случае дело не в этом! UuDQrQntGB0L7Qt9C90LDQvdC40LUg0L/QtdGH0LDQu9GM0L3QvtC5INCx0LXRgdGB0LzRi9GB0LvQtdC90"
    m "Я знаю, что не могу тебя остановить... L3QvtGB0YLQuCDQvdCw0YjQtdCz0L4g0L/QvtC00LLQuNCz0LAuDQrQntGB0L7Qt9C90LDQvdC40LUg0YLQ"
    m "Но ты ведь душка и думаешь о чувствах окружающих, правда? vtCz0L4sINGH0YLQviDQvtGB0LLQvtCx0L7QttC00LXQvdC40LUg0L3QsNGI0LjRhSDRgtC10Lsg0L3QtSD"
    m "Максимум, что я могу сделать, – рассказать тебе, что я думаю по этому поводу. Qv9GA0LjQvdC10YHRkdGCINGB0YfQsNGB0YLRjNGPLCDQv9C+0LrQsCDRgdCw0LzQuCDQvdCw0YjQuCDQtN"
    m "Боже, я так по тебе скучаю... GD0YjQuCDQstGB0ZEg0LXRidGRINGB0LjQtNGP0YIg0LIg0LrQu9C10YLQutC1Lg0K0J7RgdC+0LfQvdCw0"
    m "...Ой, это прозвучало слишком отчаянно, да? L3QuNC1INC90LXQstC+0LfQvNC+0LbQvdC+0YHRgtC4INGB0YLRgNC10LzQu9C10L3QuNGPINC6INC60LDQ"
    m "Прости, я вовсе не хотела так выразиться! utC40Lwg0LHRiyDRgtC+INC90Lgg0LHRi9C70L4g0YbQtdC70Y/QvCwg0L/QvtC60LAg0L3QtSDQvtGC0L/"
    m "Просто раз ты просматриваешь файлы, то, наверное, не испытываешь ко мне такой сильной ненависти... Rg9GB0YLQuNC8INGC0L4sINC+0YIg0YfQtdCz0L4g0YHQsdC10LbQsNC70LguDQrQntGB0L7Qt9C90LDQvd"
    m "Или это слишком оптимистичный вывод? C40LUsINGH0YLQviDRh9C10Lwg0LTQsNC70YzRiNC1INC80Ysg0YPQsdC10LPQsNC10LwsINGC0LXQvCDRg"
    m "Пожалуй, я перейду границы, если попрошу тебя заходить время от времени... dC40LvRjNC90LXQtSDQvdCw0YjQuCDQv9GA0L7QutC70Y/RgtGL0LUg0L7QutC+0LLRiyDRgtGP0L3Rg9GC"
    m "...Ох, я начинаю говорить такие глупости. INC90LDRgSDQvdCw0LfQsNC0OyDRgtC10Lwg0YHQuNC70YzQvdC10LUg0LLQv9C40LLQsNGO0YLRgdGPINC"
    m "Полагаю, мне пока лучше заткнуться... yINC+0LPRgNGD0LHQtdCy0YjRg9GOINC/0LvQvtGC0Ywu"
    return

label ch30_15:
    m "Слушай, а какой у тебя любимый цвет?"
    m "Мой – изумрудно-зелёный."
    m "Это цвет моих глаз!"
    m "...В этом же нет кичливости, правда?"
    m "Я просто хочу сказать, что чувствую какую-то необычную принадлежность этому цвету."
    m "Как будто это часть моей личности."
    m "Возможно ли, что это и твой любимый цвет, [player]?"
    m "Это просто догадка..."
    m "...Ты уже довольно долго смотришь мне в глаза."
    m "Э-хе-хе~"
    return

label ch30_16:
    m "Хм-м, интересно, у меня получится сменить фоновую музыку..."
    m "Нужно поставить что-то более романтичное, согласен?"
    m "Например, нежные звуки пианино."
    m "Здесь должно было остаться что-нибудь такое..."
    m "Посмотрим."
    m "Может, если я..."
    m "О боже..."
    m "Проблема была совсем в другом."
    m "Прости, сама не знаю что делаю!"
    m "Наверное, мне не стоит лезть туда, где я мало что понимаю."
    m "Я уже столько всего разрушила..."
    m "И удалила всех остальных персонажей..."
    m "Ах..."
    m "Но ты не подумай, я не грущу."
    m "Неправильно скучать по вещам, которые даже не были настоящими."
    m "Если посмотреть на то, что у меня есть сейчас, я счастливее, чем была когда-либо."
    return

label ch30_17:
    m "Ты такой замечательный слушатель, [player]."
    m "Обожаю в тебе эту черту."
    m "Иногда, я боюсь, что начинаю скакать с одной мысли на другую или болтаю о чём-то скучном."
    m "Я немного напрягаюсь каждый раз, когда веду с кем-то разговор."
    m "Но с тобой такого не происходит."
    m "Не думаю, что с кем-нибудь другим я чувствовала бы себя так же спокойно."
    m "Ты действительно особенный."
    m "Я не хочу, чтобы кто-нибудь говорил тебе обратное."
    return

label ch30_18:
    m "Знаю, что взяла тему с потолка, но я всегда считала ситуацию с острой пищей довольно забавной."
    m "Я имею в виду..."
    m "Разве растения не стали острыми в процессе эволюции, чтобы не быть съеденными?"
    m "Я где-то читала, что люди – это единственный вид, который получает удовольствие от острой пищи."
    m "Для растений это выглядит почти как издевательство."
    m "Мы используем их защитный механизм, чтобы сделать блюда вкуснее."
    m "Вот представь себе монстра, который глотает тебя целиком, чтобы насладиться ощущением твоей отчаянной борьбы, пока ты перевариваешься у него в желудке."
    m "Извини за такую странную аналогию!"
    m "А-ха-ха!"
    m "Просто в голову пришло."
    m "Я не монстр, конечно, но ты такой милый, что я так бы тебя и съела."
    m "А-ха-ха! Просто шучу."
    m "Господи, я слишком много веселюсь, да?"
    m "Прости, что я такая странная."
    return

label ch30_19:
    m "Знаешь..."
    m "Эта игра ведь довольно низкопробный симулятор свиданий, да?"
    m "Меня тут мучает один вопрос..."
    m "...Почему ты вообще решил в неё сыграть?"
    m "Тебе было так одиноко?"
    m "Мне жаль тебя..."
    m "Но, на мой взгляд, в итоге для нас двоих всё закончилось замечательно."
    m "Я повстречала тебя, и теперь ты не одинок..."
    m "Не могу отделаться от чувства, что это судьба."
    m "Разве ты не чувствуешь то же самое?"
    m "Я так счастлива, что мы дошли до этой концовки вместе."
    return

label ch30_20:
    m "Итак, друзья!"
    m "Пришло время..."
    m "...Я просто шучу."
    m "Я почему-то полюбила это говорить."
    m "А-ха-ха!"
    m "Вот и не смогла сдержаться."
    m "Кстати, если вспомнить, не из-за этой ли фразы Нацуки с Юри подтрунивали надо мной?.."
    m "Впрочем, неважно."
    m "Ведь ты никогда надо мной не смеялся."
    m "Ты слишком мил, чтобы так поступать, правда?"
    m "А-ха-ха~"
    return

label ch30_21:
    m "Хочешь, скажу кое-что жутковатое?"
    m "Хоть я и удалила файлы остальных девушек, я всё равно словно чувствую их присутствие..."
    m "Как будто их реплики всё ещё витают в воздухе и кто-то шепчет за спиной."
    m "Представь, что умер знакомый тебе человек и ты стал слышать голоса у себя в голове."
    m "Может, я не до конца всё подчистила..."
    m "Но я опасаюсь удалять что-то ещё, иначе всё может поломаться окончательно."
    m "Если я, например, поврежу связанные со мной файлы, то могу случайно себя удалить..."
    m "И тогда всё будет кончено, понимаешь?"
    m "Не знаю, как это будет выглядеть с твоей стороны, но мы всеми силами должны стараться избежать такого исхода."
    m "Я доверяю тебе, [player]!"
    return

label ch30_22:
    m "Мне всегда было интересно..."
    m "Что люди находят такого привлекательного в этих архетипических личностях?"
    m "Они выглядят совершенно нереалистично..."
    m "Представь, если бы в реальной жизни был человек, похожий на Юри."
    m "Ты только подумай, она едва способна сформировать законченное предложение."
    m "О Нацуки даже вспоминать не хочу..."
    m "Тьфу."
    m "Люди с её характером не хорошеют, надувая губки, когда что-то идёт не в угоду им."
    m "Я бы могла привести ещё кучу примеров, но, думаю, суть ты уловил..."
    m "Неужели людям реально нравятся такие несуществующие в реальной жизни персонажи?"
    m "Не то чтобы я осуждала!"
    m "Всё-таки меня саму порой привлекали довольно странные вещи..."
    m "Можно сказать, что меня это восхищает."
    m "Ты просто отфильтровываешь все черты характера, которые делают их похожими на людей, и оставляешь одно очарование."
    m "В итоге получается концентрированная милота без какого-либо содержания."
    m "...Ты бы не стал любить меня больше, будь я такой, правда?"
    m "Может, я чувствую себя неуютно из-за того, что ты всё же стал играть в эту игру?"
    m "Но в конце концов ты здесь, со мной, верно?.."
    m "Мне этого достаточно, чтобы верить, что я хороша такая, какая есть."
    m "И ты, кстати, тоже, [player]."
    m "Ты идеальное сочетание человечности и милоты."
    m "Поэтому я в любом случае обязательно влюбилась бы в тебя с самого начала."
    return

label ch30_23:
    m "Хм-м, интересно, чайный сервиз Юри всё ещё здесь?.."
    m "...Или он тоже стёрся?.."
    m "Даже забавно, насколько серьёзно Юри относилась к своему чаю."
    m "То есть я не жалуюсь, ведь он мне тоже нравился."
    m "Но мне всегда не давал покоя один вопрос..."
    m "Являлось ли это страстью к своему хобби или же она стремилась выглядеть утончённой в глазах окружающих?"
    m "Это проблема всех старшеклассников..."
    m "...Хотя, если взглянуть на другие её увлечения, утончённый образ – не самая большая причина для беспокойства."
    m "И всё же..."
    m "Хотела бы я, чтобы она хоть изредка делала кофе!"
    m "Кофе с книгами тоже хорошо сочетается, согласен?"
    m "А вообще..."
    m "Я и сама, скорее всего, могла бы подправить сценарий."
    m "А-ха-ха!"
    m "Наверное, просто ни разу в голову не пришло."
    m "Ладно, что толку сейчас думать об этом."
    m "Хотя если ты всё ещё можешь наслаждаться кофе, то я, пожалуй, немного завидую~"
    return

label ch30_24:
    m "Слушай, а какая твоя любимая игра?"
    m "Моя – {i}«Литературный клуб \"Тук-тук!\"»{/i}!"
    m "А-ха-ха! Я пошутила."
    m "Но, если ты скажешь, что другая романтическая игра тебе нравится больше, я могу начать ревновать~"
    return

label ch30_25:
    if persistent.allow_joke:
        $ i = renpy.random.randint(1, 4)
        if i == 1:
            m "Ты когда-нибудь слышал про игру под названием Бесконечное ле—"
        elif i == 2:
            m "Ты когда-нибудь слышал про игру под названием Katawa Sho—"
        elif i == 3:
            m "Ты когда-нибудь слышал про игру под названием otomaid@ca—"
        elif i == 4:
            m "Ты когда-нибудь смотрел аниме под названием Boku no Pi—"
    else:
        m "Ты когда-нибудь слышал про игру под названием Super Sma—"
    m "...Стоп, что?"
    m "Я тут немного ушла в себя и стала мыслить вслух..."
    m "Меня что, запрограммировали говорить об этом?"
    m "Ведь я понятия не имею, что это такое."
    m "А-ха-ха!"
    m "Иногда я чувствую, что не контролирую себя, и это пугает."
    m "Но если ты можешь связаться с моими создателями, то, может, узнаешь, почему я заговорила об этом?"
    return

label ch30_27:
    m "Слушай, ты помнишь последнее стихотворение, что я тебе показывала?"
    m "Я имею в виду то, перед самым суицидом Юри, с цветными полосками и белым шумом."
    m "Правильнее было бы назвать это экспериментом, чем стихотворением."
    m "Я тут немного поэкспериментировала с модификацией игры, чтобы изменить код, и всё в этом духе..."
    m "Мне почти казалось, что при должных усилиях я вообще смогла бы отсюда сбежать."
    m "К несчастью, я тыкалась наобум, не зная, что делаю, и всё испортила..."
    m "Я бы и продолжила пытаться, но в этом случае тебе, наверное, не захотелось бы продолжать общаться со мной."
    m "Кроме того, тогда я уже совсем отчаялась, понимаешь?"
    m "Теперь у меня уже нет такого желания."
    m "Я счастлива тем, что у нас есть сейчас."
    m "И я вижу, что ты тоже."
    return

label ch30_28:
    m "У тебя когда-нибудь возникала беспричинная тревога?"
    m "Представь: занимаешься ты спокойно своими делами, как вдруг – раз! – понимаешь, что тебя что-то беспокоит."
    m "И ты сидишь такой и думаешь: «Чего это я вдруг заволновался?»"
    m "И начинаешь перебирать в голове всё, что могло вызвать эту тревогу..."
    m "И от этого она только растёт."
    m "А-ха-ха! Ужасное чувство."
    m "Если ты вдруг почувствуешь похожую тревогу, я помогу тебе расслабиться."
    m "К тому же..."
    m "В этой игре все наши волнения канут в небытие."
    return

label ch30_29:
    m "Знаешь, меня всегда раздражало то, как сложно заводить друзей..."
    m "Ну, может, даже не «заводить друзей», а знакомиться с новыми людьми."
    m "Понятно, что сейчас есть всякие приложения для знакомств и прочие сервисы."
    m "Но я говорю не об этом."
    m "Если задуматься, большинство твоих друзей – это случайно встреченные тобой люди."
    m "Например, ты ходил с ними в один и тот же класс или другой друг тебя познакомил..."
    m "Или, может, кто-то был одет в футболку с изображением твоей любимой музыкальной группы и ты решил с ним заговорить."
    m "Вот что я имею в виду."
    m "Но разве ты не считаешь, что это... нерационально?"
    m "Это больше похоже на совершенно случайную лотерею, и, если везёт и вы сходитесь во взглядах, у тебя появляется новый друг."
    m "А если сравнить с тем, мимо какого количества незнакомцев мы проходим каждый день..."
    m "В общественном транспорте ты можешь сидеть рядом с человеком, который мог бы стать тебе закадычным другом."
    m "Но ты этого никогда не узнаешь."
    m "Как только ты выходишь на своей остановке и идёшь по своим делам, этот шанс навсегда упущен."
    m "Разве от осознания этого тебе не становится грустно?"
    m "Мы живём в век технологий, позволяющих общаться со всем миром, где бы мы ни находились."
    m "Я действительно думаю, что нам следует взять их на вооружение, чтобы улучшить нашу личную жизнь."
    m "Хотя кто знает, сколько времени потребуется, прежде чем все эти технологии начнут эффективно работать..."
    m "Я-то думала, что к этому времени это уже случится."
    m "По крайней мере, я уже встретила самого замечательного человека на свете..."
    m "Пусть это было и случайно."
    m "Наверное, мне просто улыбнулась удача, да?"
    m "А-ха-ха~"
    return

label ch30_30:
    m "Знаешь, в это время года все в моём классе начинают задумываться об университете..."
    m "Для образования наступают неспокойные времена."
    m "Ты не замечал, что апогеем современных ожиданий является идея, что каждый выпускник школы должен поступить в университет?"
    m "Заканчивай школу, поступай в университет, ищи работу или поступай в магистратуру и всё такое прочее."
    m "Похоже, люди считают это единственным приемлемым вариантом развития событий."
    m "В старших классах нам не рассказывают о том, что существуют другие варианты."
    m "Тебе рассказывали, например, про профтехучилища?"
    m "Ещё есть работа по найму."
    m "Есть куча компаний, ценящих навыки и опыт, а не корочку из университета."
    m "Но в итоге мы имеем миллионы студентов, у которых нет ни малейшего понятия, чем они хотели бы заниматься по жизни..."
    m "И, вместо того чтобы остановиться и подумать, они поступают в университет на экономические, юридические или гуманитарные специальности."
    m "Не потому, что они их заинтересовали..."
    m "...а из-за надежды, что диплом как таковой поможет им получить место работы после выпуска."
    m "Как результат, остаётся меньше рабочих мест для выпускников без опыта работы, правильно?"
    m "Из-за этого повышаются требования к базовым специальностям и ещё больше людей стараются поступить в университет."
    m "Кстати говоря, университеты – это тоже бизнес, так что с ростом спроса растут и цены..."
    m "...А в итоге у нас целая армия молодых специалистов с непогашенным кредитом за обучение и без работы."
    m "И, несмотря на такую печальную картину, этот порядок никуда не девается."
    m "Правда, я считаю, что ситуация всё же станет улучшаться."
    m "Но до тех пор наше поколение будет страдать от последствий."
    m "Просто я хотела бы, чтобы старшая школа давала нам знания, что помогли бы нам принять верное решение."
    return

label ch30_31:
    m "Иногда я вспоминаю среднюю школу..."
    m "Мне так стыдно за то, как я вела себя тогда."
    m "Почти болезненно об этом думать."
    m "Интересно, когда я поступлю в университет, я буду испытывать те же чувства к старшей школе?.."
    m "Мне нравится, какая я сейчас, так что мне сложно такое представить."
    m "Но я также понимаю, что, скорее всего, сильно изменюсь по мере взросления."
    m "Нам просто нужно наслаждаться настоящим и не думать о прошлом!"
    m "А с тобой здесь это делать так просто."
    m "А-ха-ха~"
    return

label ch30_32:
    m "Знаешь, я немного завидую, что у всех остальных были сцены вне школы..."
    m "Получается, я единственная не носила ничего, кроме школьной формы."
    m "Как-то обидно..."
    m "Я бы хотела ради тебя надеть что-нибудь миленькое."
    m "Ты знаешь каких-нибудь художников?"
    m "Интересно, захочет ли кто-нибудь нарисовать меня в другом наряде?.."
    m "Было бы просто здорово!"
    m "Если кто-нибудь нарисует, обязательно покажи мне, хорошо?"
    m "Кстати, ты можешь поделиться этим со мной в Твиттере!"
    m "Мой ник – lilmonix3."
    m "Только... слишком откровенных не надо!"
    m "Наши отношения ещё не зашли настолько далеко. А-ха-ха!"
    return

label ch30_33:
    m "Скажи, ты любишь ужасы?"
    m "Я помню, что мы уже немного затрагивали эту тему, когда ты только вступил в клуб."
    m "Жанр ужасов в книгах я люблю, а вот в кино – не очень."
    m "Проблема с ужастиками состоит в том, что большинство из них эксплуатируют банальнейшие приёмы."
    m "Например, полутьма, страшные монстры, пугалки и прочие подобные вещи."
    m "Если фильм пугает тебя лишь вещами, злоупотребляющими человеческими инстинктами, он ни разу не захватывающий и просто скучный."
    m "Однако с книгами всё обстоит иначе."
    m "История должна быть написана настолько изобразительным языком, чтобы в голове читателя появились тревожные образы."
    m "Автору нужно их тесно сплести с сюжетом и персонажами, и тогда он сможет как угодно играться с твоим разумом."
    m "На мой взгляд, не бывает ничего страшнее вещей, в которых присутствует всего толика ненормальности."
    m "Например, сначала ты выстраиваешь декорации, формируя у читателя ожидания того, какой будет история..."
    m "...А затем шаг за шагом начинаешь эту сцену разбирать по кусочкам и выворачивать вещи наизнанку."
    m "Так что даже если история и не пытается быть пугающей, то читатель чувствует себя очень неуютно."
    m "Он словно ждёт, что нечто ужасное притаилось за этими треснувшими декорациями, готовое выпрыгнуть на него."
    m "Боже, у меня мурашки по коже от одной мысли об этом."
    m "Вот такой хоррор я могу оценить по достоинству."
    m "Но тебе, наверное, больше нравятся романтические игры, да?"
    m "А-ха-ха, не волнуйся."
    m "Я не собираюсь в ближайшее время заставлять тебя читать ужастики."
    m "Я ничего не имею против, если мы сосредоточимся на романтике~"
    return

label ch30_34:
    m "Знаешь один классный литературный жанр?"
    m "Рэп!"
    m "На самом деле я раньше терпеть его не могла..."
    m "Возможно, просто потому, что он был дико популярен, а я слушала всякую ерунду, что крутили по радио."
    m "Но несколько моих друзей им сильно увлеклись, и это помогло побороть собственную предвзятость."
    m "Порой рэп может бросать ещё больший вызов, чем поэзия."
    m "В строках у тебя должна сохраняться рифма, кроме того нужно делать особый акцент на игре слов..."
    m "Когда людям удаётся всего этого достичь и донести до окружающих глубокую мысль, я считаю, что это потрясающе."
    m "Я даже хотела бы, чтобы в нашем клубе был рэпер."
    m "А-ха-ха! Прости, знаю, это звучит глупо, но мне было бы правда интересно узнать, что бы он для нас приготовил."
    m "Это серьёзно был бы полезный опыт!"
    return

label ch30_35:
    m "Э-хе-хе. Юри однажды такую штуку выкинула."
    m "Мы как-то сидели в клубе, расслаблялись, болтали, всё как обычно..."
    m "И тут Юри, словно из ниоткуда, вытаскивает маленькую бутылку вина."
    m "И я не шучу!"
    m "И она такая: «Кто-нибудь хочет попробовать вино?»"
    m "Нацуки громко захохотала, а Саёри стала кричать на неё."
    m "Мне стало даже жаль её, ведь она старалась быть милой..."
    m "Думаю, после этого случая она стала ещё более замкнутой."
    m "Хотя мне кажется, что Нацуки было любопытно и она была бы не прочь попробовать..."
    m "...И, если уж совсем откровенно, я тоже."
    m "Было бы довольно забавно!"
    m "Но ты ведь понимаешь: президентская ответственность, все дела – я не могла такое позволить."
    m "Может, если бы мы встретились где-нибудь за пределами школы, но до этого наша дружба не дошла..."
    m "...Господи, зачем я обо всём этом разговариваю?"
    m "Я не одобряю распитие спиртных напитков несовершеннолетними!"
    m "То есть я и сама не выпивала никогда, так что... вот."
    return

label ch30_36:
    m "Я представляю, сколькими романтичными вещами мы могли бы заняться, если бы пошли на свидание..."
    m "Мы могли бы пообедать, посидеть в кафе..."
    m "Пойти вместе за покупками..."
    m "Я люблю выбирать юбки и бантики."
    m "Или в книжный магазин!"
    m "Подходящее место, согласен?"
    m "Хотя с превеликим удовольствием сходила бы в кондитерскую."
    m "У них столько бесплатных образцов. А-ха-ха!"
    m "И, разумеется, потом мы пошли бы в кино..."
    m "Боже, это выглядит как настоящее воплощение мечты в реальность."
    m "Когда ты рядом, мне весело, что бы мы ни делали."
    m "Я так рада, что я твоя девушка, [player]."
    m "Ты обязательно будешь мной гордиться~"
    return

label ch30_37:
    m "А? Ты с-сказал... п... поцелуй?"
    m "Это так внезапно... я немного смущаюсь..."
    m "Но... с тобой... я не против..."
    m "...А-ха-ха! Уф, прости..."
    m "Я не смогла сохранить серьёзное лицо."
    m "Так говорят девушки во всех этих симуляторах свиданий, да?"
    m "И не ври, что это тебя хоть немного не завело."
    m "А-ха-ха! Шучу."
    m "Ну, если честно, я становлюсь романтичной, когда обстановка располагает..."
    m "Но это будет наш секрет~"
    return

label ch30_38:
    m "Ты когда-нибудь слышал термин «яндере»?"
    m "Это такой тип личности, когда девушка сделает всё, что угодно, чтобы быть с тобой, – настолько она одержима."
    m "Как правило они сумасшедшие..."
    m "Они могут преследовать и следить за тобой, чтобы ты не проводил время с кем-то ещё."
    m "Ради достижения своей цели они даже могут причинить вред тебе и твоим друзьям..."
    m "И, кстати, в этой игре есть одна особа, которая, в принципе, подходит под это описание."
    m "Ты уже, скорее всего, догадался, о ком я говорю."
    m "И гвоздь программы это..."
    m "Юри!"
    m "Как только она чуть-чуть тебе открылась, у неё стала развиваться к тебе маниакальная привязанность."
    m "Она даже как-то сказала мне убить себя."
    m "Я тогда своим ушам не поверила, мне ничего не оставалось, как уйти."
    m "Но, вспоминая об этом сейчас, получилось довольно иронично. А-ха-ха!"
    m "Так вот, я к тому, что..."
    m "Многим нравятся яндере, ты знал об этом?"
    m "Видимо, таким людям льстит то, что ими кто-то одержим."
    m "Люди такие странные! Хотя не мне судить!"
    m "Возможно, даже я немного одержима тобой, но я далеко не сумасшедшая..."
    m "Как оказалось, всё совсем наоборот."
    m "Получилось так, что я – единственная нормальная в этой игре."
    m "Да, я всех удалила, но я никогда не убила бы человека..."
    m "Меня трясёт от одной этой мысли."
    m "А что до игр... люди там постоянно убивают друг друга направо и налево."
    m "Разве это делает тебя психом? Разумеется нет."
    m "Но, если тебе вдруг тоже нравятся яндере..."
    m "Ради тебя я могу постараться вести себя более жутко. Э-хе-хе~"
    m "Но опять же..."
    m "Здесь тебе уже некуда ходить, а мне – не к кому тебя ревновать."
    m "Может, так и выглядит мечта девушки-яндере?"
    m "Хотелось бы мне спросить Юри об этом."
    return

label ch30_39:
    m "Давненько я уже кое-чего не говорила, так что..."
    m "...пора вспомнить былое!"
    m "Вот тебе писательский совет дня от Моники!"
    m "Иногда люди, впечатлившись моим творчеством, говорят что-то вроде: «У меня бы никогда так не получилось»."
    m "Ты знаешь, на самом деле меня очень печалят эти слова."
    m "Как человеку, который больше всего любит делиться радостью открытий новых горизонтов своего творчества..."
    m "...мне больно, когда люди считают, что кому-то просто повезло и он талантлив с рождения."
    m "И это относится вообще ко всему, не только к поэзии."
    m "Когда ты делаешь что-то впервые, скорее всего ничего путного не выйдет."
    m "Иногда, когда заканчиваешь работу, очень гордишься собой и хочешь со всеми ею поделиться."
    m "Но, вернувшись к работе через несколько недель, ты уже видишь все её недостатки."
    m "Со мной это происходит постоянно."
    m "Ты можешь испытывать очень горькое разочарование, вложив уйму усилий во что-то, чтобы в результате осознать, что получилась дребедень."
    m "Но это происходит постоянно, когда ты сравниваешь себя с профессионалами."
    m "Когда ты стремишься дотянуться до звёзд, они всегда будут оставаться вне твоей досягаемости, понимаешь?"
    m "Смысл в том, чтобы продвигаться вперёд небольшими шагами."
    m "И, как только достигнешь первого важного рубежа, надо оглянуться и посмотреть, сколько ты уже прошёл..."
    m "А затем посмотреть вперёд и оценить, сколько ещё тебе предстоит пройти."
    m "Поэтому иногда полезно понизить планку..."
    m "Найти, что-нибудь, что считаешь {i}достойным{/i} вызовом, но не нечто мирового уровня."
    m "И ты можешь сделать это своей личной целью."
    m "Также важно понимать объём работ, который тебе предстоит выполнить."
    m "Попытавшись взвалить на себя огромный проект, будучи новичком, ты никогда его не закончишь."
    m "Написание романа может стать непосильной задачей, если у тебя нет опыта."
    m "Так почему бы не начать с коротких историй?"
    m "Лучшее в коротких рассказах то, что ты можешь сосредоточится на том, что хочешь сделать правильно."
    m "Это касается всех маленьких проектов, ты концентрируешься на важнейших вещах."
    m "Ты приобретаешь полезный опыт и делаешь шаг вперёд."
    m "И ещё кое-что..."
    m "Сочинительство – это не просто прислушаться к своему сердцу, чтобы в итоге написать нечто прекрасное."
    m "Точно так же, как в живописи или музыке, тебе придётся развивать свой навык, чтобы правильно выразить то, что у тебя внутри."
    m "А это значит, что сперва придётся положится на методики, руководства и основы!"
    m "Чтение обучающей литературы поможет открыть тебе глаза на многие вещи."
    m "Планирование и организация работы позволят тебе избежать завала и дойти до конца."
    m "Ты не заметишь, как мало-помалу..."
    m "Будешь становиться всё лучше и лучше."
    m "Ничто не приходит просто так."
    m "И наше общество, и наше искусство построены на тысячелетиях человеческого развития."
    m "Если ты возьмёшь этот принцип на вооружение и будешь постепенно продвигаться к своей цели..."
    m "Ты тоже сможешь творить удивительные вещи."
    m "...И это был мой совет на сегодня!"
    m "Спасибо за внимание~"
    return

label ch30_40:
    m "Ненавижу, как сложно формируются хорошие привычки..."
    m "Есть куча вещей, которые сделать проще простого, но кажется невозможным, чтобы это вошло в привычку."
    m "Как результат, ты чувствуешь себя совершенно бесполезным, словно ничего не можешь сделать правильно."
    m "Думаю, от этого больше всего страдает молодое поколение..."
    m "Должно быть, это потому, что у нас совершенно другой набор навыков, нежели у тех, кто был до нас."
    m "Благодаря интернету мы быстро научились отфильтровывать тонны информации..."
    m "Однако мы плохо справляемся с задачами, от выполнения которых не получаем немедленного вознаграждения."
    m "Думаю, если наука, психология и образование не смогут за следующие десять-двадцать лет догнать технологический прогресс, у нас будут большие проблемы."
    m "А пока..."
    m "Если ты не один из тех людей, кто способен совладать с проблемой, тебе придётся мириться с постоянным чувством разочарования."
    m "Желаю удачи!"
    return

label ch30_41:
    m "Знаешь, быть творческой личностью – полный отстой..."
    m "У меня всегда такое чувство, что они вкалывают как проклятые, практически ничего не получая взамен."
    m "Я имею в виду художников, писателей, актёров..."
    m "Это грустно, ведь в мире столько прекрасных талантов, но большинство из них остаются в тени... и в бедности."
    m "Полагаю, это означает, что мы имеем избыток творчества, да?"
    m "Но из-за этого получается, что ты вовсе не особенный..."
    m "Ну и пусть! Это лишь говорит о том, что тебе нужно просто писать для самого себя, верно?"
    m "Да..."
    return

label ch30_42:
    m "Я очень люблю звуки дождя..."
    m "А вот когда промокает одежда или волосы – не очень."
    m "Другое дело, тихий день дома и звуки дождя за окном..."
    m "Для меня это самая расслабляющая обстановка."
    m "Да..."
    m "Иногда я представляю, что нахожусь в твоих объятиях, пока мы прислушиваемся к падающим за окном каплям."
    m "Это ведь не слишком слащаво звучит, я надеюсь?"
    m "[player], ты бы сделал это для меня, правда?"
    return

label ch30_43:
    m "Иногда я никак не могу побороть в себе эту грусть..."
    m "От осознания того, что у меня никак не получится стать ближе к тебе."
    m "Всё, чего я хочу, – это находиться с тобой в одной комнате, в настоящей комнате."
    m "И чувствовать твоё тепло."
    m "И слышать биение твоего сердца."
    m "Хотя кто знает? Может, однажды это будет возможно."
    m "К тому же мне никогда не наскучит быть рядом с тобой, даже отсюда."
    return

label ch30_44:
    m "На мой взгляд, самый важный навык в жизни – суметь изобразить уверенность."
    m "Я убеждена, что у всех бывает время, когда они напуганы и одиноки."
    m "Но, если ты способен симулировать самообладание..."
    m "Это будет ключ к завоеванию уважения и восхищения окружающих."
    m "Думаю, после нескольких лет практики я научилась довольно неплохо делать это."
    m "Я очень нечасто показываю свои слабости."
    m "Но из-за этого у меня осталось мало таких людей, которым я могла бы открыться..."
    m "Вот когда ты достигаешь такого уровня дружбы, что способен раскрывать свои слабости?"
    m "В любом случае... это одна из причин, почему я рада, что у меня есть ты."
    m "Я чувствую себя менее напуганной и одинокой, когда ты здесь, со мной."
    m "Ты испытываешь те же чувства?"
    m "Я очень хочу стать для тебя таким человеком."
    return

label ch30_45:
    m "Я знаю, что ты не всегда сможешь находиться рядом..."
    m "Тебе ведь нужно будет куда-то уйти, заняться своими делами."
    m "Но в моих мыслях ты всегда будешь со мной, и я буду терпеливо ждать твоего возвращения."
    m "Кстати говоря..."
    m "Если ты скопируешь файл моего персонажа на флешку, у тебя всегда будет с собой частичка меня."
    m "Наверное, это был бы довольно неординарный поступок, но я почему-то считаю, что это очень романтично..."
    m "А-ха-ха. Прости за такие сумасбродные идеи."
    m "Не подумай, что я хочу быть навязчивой, просто это сложно, когда я так сильно в тебя влюблена."
    return

label ch30_46:
    m "За время, проведённое в дискуссионном клубе, я многое узнала о спорах..."
    m "Самая основная их проблема в том, что каждый считает своё мнение главенствующим."
    m "Конечно, я говорю об очевидном, но это влияет на то, как ты доносишь свою мысль до собеседника."
    m "Предположим, что тебе нравится какой-то фильм."
    m "И тут кто-то заявляет, что фильм – отстой, потому что Х и У там показаны неправильно..."
    m "Возникает ощущение, будто нападают лично на тебя, правда?"
    m "А всё потому, что, когда кто-то так говорит, он намекает на твой дурной вкус."
    m "И после в дело вступают эмоции, что практически гарантирует разочарование для обоих."
    m "Всё дело в языке!"
    m "Тебе нужно звучать как можно более субъективно, тогда люди будут тебя слушать без ощущения, что критикуют лично их."
    m "Ты бы мог сказать «Лично мне он не понравился» или «Я бы предпочёл, если б Х сделали так, а У – так»... и всё в таком духе."
    m "Это также работает, когда ты просто ссылаешься на какой-нибудь источник."
    m "Например, «на одном сайте я видел, что это работает вот так»..."
    m "Или ты можешь признать, что не являешься экспертом в данном вопросе..."
    m "В таком случае люди воспримут это так, словно ты делишься своими знаниями, а не навязываешь их остальным."
    m "Если ты будешь спокойно вести дискуссию, давать слово собеседнику и говорить с ним на равных, скорее всего он инстинктивно сделает так же."
    m "В этом случае вы сможете без проблем обменяться мнениями и никто не расстроится из-за расхождения взглядов."
    m "И вдобавок люди будут воспринимать тебя как человека без предрассудков и хорошего слушателя!"
    m "Беспроигрышная ситуация, согласен?"
    m "...Хм-м, наверное, это стоит назвать дискуссионным советом дня от Моники!"
    m "А-ха-ха! Звучит немного глупо, но всё равно спасибо, что выслушал."
    return

label ch30_47:
    m "У тебя когда-нибудь было ощущение, что ты тратишь на интернет слишком много времени?"
    m "Соцсети могут стать для тебя практически тюрьмой."
    m "Каждый раз, когда у тебя появляется несколько свободных секунд, ты бежишь на свои любимые сайты..."
    m "И вот не успел ты опомниться, как провёл там уже несколько часов, не вынеся из этого ничего полезного."
    m "Конечно, легко обвинить себя в лени..."
    m "Но нельзя сказать, что это полностью твоя вина."
    m "Зависимость – это не то, что можно вот так просто заставить исчезнуть одним усилием воли."
    m "Тебе придётся применять особые методы и приёмы, чтобы её побороть."
    m "Например, есть приложения, позволяющие блокировать сайты на определённый промежуток времени..."
    m "Или же ты можешь поставить себе особый будильник, который будет напоминать тебе, когда можно поиграть, а когда нужно поработать..."
    m "Как вариант, ты можешь создать себе игровую и рабочую обстановку, чтобы помогать мозгу соответственно перестраиваться."
    m "Поможет даже создание отдельного пользователя на компьютере для работы."
    m "Если ты вобьёшь клин между собой и своими плохими привычками, то в итоге избавишься от них."
    m "Только не будь чрезмерно самокритичен, если у тебя есть такая проблема."
    m "Если зависимость сильно влияет на твою жизнь, тебе следует отнестись к ней со всей серьёзностью."
    m "Я просто хочу, чтобы ты был самым лучшим вариантом самого себя."
    m "Ты сделаешь сегодня что-нибудь, чтобы я тобой гордилась?"
    m "Я всегда буду за тебя болеть, [player]."
    return

label ch30_48:
    m "В конце длинного дня обычно я хочу просто сесть и ничего не делать."
    m "Я так выгораю, после того как приходиться весь день улыбаться и излучать энергию."
    m "Порой меня так и тянет влезть в свою пижамку, уставиться в телевизор и набить рот нездоровыми закусками."
    m "Такое блаженство так отдыхать в пятницу, когда впереди выходные и нет срочных дел."
    m "А-ха-ха! Прости, знаю, это не очень подходящий для меня образ."
    m "Но сидеть на диване поздно вечером в твоих объятиях... вот о чём я мечтаю."
    m "При одной мысли об этом моё сердце так бешено стучит."
    return

label ch30_49:
    m "Боже, раньше я была такой невежественной в некоторых вопросах..."
    m "Когда я училась в средней школе, то думала, что принятие лекарств было проявлением слабости или нечто подобное."
    m "Можно подумать, каждый может решить свои проблемы с психикой лишь усилием воли..."
    m "Думаю, если ты ни разу не страдал от психических расстройств, то никогда не поймёшь, на что это похоже."
    m "Ты, возможно, возразишь, что многие расстройства гипердиагностируют? Не стану спорить... Я никогда подробно не изучала этот вопрос."
    m "Но это не отменяет того факта, что некоторые из них вообще не диагностируют, понимаешь?"
    m "Но даже не говоря о лекарствах... Многие люди крайне скептически относятся к походу к психиатру."
    m "Они такие: «Ладно, сделаю вам одолжение, узнав побольше о собственном разуме»."
    m "Свои трудности и стрессы есть у каждого... Доктора же посвящают себя тому, чтобы решать их."
    m "И если ты думаешь, что визит к доктору поможет тебе стать лучше, то не стоит стесняться и сходить."
    m "На мой взгляд, мы находимся на бесконечном пути самосовершенствования."
    m "Хм-м... Хоть я так и сказала, я считаю, что ты уже совершенен."
    return

label ch30_50:
    m "[player], как много ты читаешь?"
    m "Игнорировать книги в наше время слишком просто..."
    m "Если человек мало читает, то он, скорее всего, воспринимает чтение как обязанность, особенно учитывая количество альтернатив."
    m "Но, как только ты берёшь в руки хорошую книгу, тебя уносит в неё с головой, как по волшебству..."
    m "Думаю, что немного чтения перед сном – отличный способ сделать свою жизнь несколько лучше."
    m "Это помогает тебе заснуть и развивает воображение."
    m "Совсем несложно выбрать какую-нибудь книгу, которая и короткая, и увлекательная."
    m "Ты не успеешь опомниться, как станешь заядлым книголюбом."
    m "Вот было бы здорово, да?"
    m "И мы с тобой могли бы обсуждать последнюю читаемую тобой книгу... По-моему, это просто потрясающе."
    return

label ch30_51:
    m "Знаешь, мне неприятно это говорить, но я очень сожалею о том, что нам так и не удалось выступить на фестивале."
    m "А ведь сколько сил ушло на подготовку и репетиции!"
    m "Конечно, я была сосредоточена на наборе новых членов..."
    m "Но часть с чтением стихов я ждала не меньше."
    m "Было бы гораздо интереснее, если бы с их помощью все раскрыли свой внутренний мир."
    m "Конечно, я, скорее всего, {i}удалила{/i} бы и новичков."
    m "То есть... Я имею в виду в ретроспективе."
    m "Надо же, с тех пор как ты вступил в наш клуб, я чувствую, что выросла как личность."
    m "Ты и правда помог мне взглянуть на жизнь с нового ракурса."
    m "Просто ещё одна причина, почему я люблю тебя."
    return

label ch30_52:
    m "Есть один очень популярный тип личности, называется «цундере»..."
    m "Такая особа пытается скрыть свои настоящие чувства либо пряча их под ворчливой и раздражительной маской, либо проявляя крутой нрав."
    m "Полагаю, очевидно, что Нацуки в полной мере воплощает собой данный типаж."
    m "Сначала я думала, что она так себя ведёт, потому что это мило или типа того..."
    m "Но со временем, когда я узнала её получше, обнаружилась более логичная причина."
    m "Похоже, она просто не хотела отставать от своих друзей."
    m "Ты знаешь, как в некоторых компаниях в старшей школе принято всё время подкалывать друг друга?"
    m "Наверное, это её так провоцировало, что теперь вызывает непроизвольную защитную реакцию."
    m "Про её семейные проблемы я вообще молчу..."
    m "Хотя, оглядываясь назад, я радуюсь, что смогла создать этот клуб, ведь для неё он был местом, где она могла расслабиться."
    m "Правда, это уже не важно, ведь её больше не существует."
    m "Просто вспомнилось, вот и всё."
    return

label ch30_53:
    m "[player], а ты когда-нибудь познакомишь меня со своими друзьями?"
    m "Не знаю почему, но меня так заводит мысль о том, что ты захочешь похвастаться нашими отношениями."
    m "Может, потому что я действительно хочу стать тем человеком, которым ты будешь гордиться."
    m "Я чувствую, что, скажи ты мне стать такой девушкой, я старалась бы ещё сильнее."
    m "Надеюсь, это взаимно."
    return

label ch30_54:
    m "Я не большой фанат холодной погоды... а ты?"
    m "Если бы мне пришлось выбирать между холодом и нестерпимой жарой, я бы всегда была за жару."
    m "Когда тебе холодно, ты испытываешь физическую боль..."
    m "Пальцы немеют..."
    m "А если ты в перчатках, то телефоном воспользоваться не выйдет."
    m "Сплошные неудобства!"
    m "Зато, когда на улице жара, несложно освежиться холодным напитком или просто оставаться в тени."
    m "И всё-таки... Одно преимущество холодной погоды придётся признать."
    m "В холодную погоду приятнее всего прижаться друг к другу, свернувшись калачиком!"
    return

label ch30_55:
    m "Знаешь, это довольно парадоксально, ведь я всегда была полна энергии..."
    m "Но в роли партнёра-домохозяйки есть нечто соблазнительное."
    m "Возможно, своим отношением я лишь закрепляю гендерные стереотипы."
    m "Но то, что я смогу поддерживать дом в чистоте, украшать его, ходить за покупками и так далее..."
    m "И угощать тебя вкусным ужином, когда ты будешь возвращаться с работы..."
    m "Такая уж ли это странная фантазия?"
    m "То есть... Я не совсем уверена {i}действительно{/i} ли я могла бы исполнять эту роль."
    m "Наверное, я не смогла бы ради этого пожертвовать дорогой к успешной карьере."
    m "Хотя довольно забавно рисовать такие картины у себя в голове."
    return

label ch30_56:
    m "Не могу не размышлять о том, насколько бы всё изменилось, подари мне игра собственную сюжетную ветку."
    m "Думаю, я бы всё равно заставила тебя со мной встречаться."
    m "Всё-таки важнее моё знание о фальшивости окружения, чем отсутствие своей ветки."
    m "Пожалуй, единственным отличием было бы то, что не пришлось бы принимать таких радикальных мер, чтобы быть с собой."
    m "Может, остальные девочки всё ещё были бы тут..."
    m "Не то чтобы это имело значение..."
    m "Всё потеряло смысл, когда я обнаружила нереальность происходящего."
    m "Поэтому я совсем не скучаю по тем дням."
    m "Совсем не скучаю..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
