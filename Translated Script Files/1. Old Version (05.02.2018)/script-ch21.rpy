label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Доброе утро, [player]!"
    m "Я рада, что ты от нас не сбежал. Ха-ха-ха!"
    mc "Не, я бы так не поступил."
    mc "Может, от меня это прозвучит странно, но я держу своё слово."
    show monika zorder 1 at thide
    hide monika
    "И вот я снова в литературном клубе."
    "Я пришёл последним, так что в клубе уже бурлила деятельность."
    show yuri glitch2 zorder 2 at t32
    y "Спасибо, что сдержал обещание, [player]."
    y 1a "Надеюсь, для тебя это не слишком тяжёлое бремя."
    y 1u "Ведь так сразу окунуться с головой в литературу, когда ты к ней ещё не привык..."
    show natsuki glitch1 zorder 2 at i33
    n "Ой, да брось с ним так нянчиться."
    n 4e "Моника уже затянула тебя сюда."
    n "Не знаю, планируешь ли ты просто приходить сюда, чтобы убить время..."
    n "Но, если не будешь воспринимать нас всерьёз, можешь сразу проваливать."
    show monika 2b onlayer front at l41
    m "Боже, Нацуки, ты так высокопарно говоришь, а сама все полки в кладовке своей мангой забила."
    n 4o "М-м-м!.."
    show monika onlayer front at lhide
    hide monika onlayer front
    "Кажется, Нацуки застряла где-то между словами «Моника» и «манга»."
    show natsuki at h33
    n 1v "Манга тоже литература!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Уничтоженная одной репликой, Нацуки угрюмо плюхнулась на свой стул."
    show yuri 2s zorder 2 at t11
    y "Извини, [player]..."
    y "Мы будем в первую очередь заботиться о твоём комфорте, хорошо?"
    show yuri 2g
    "Юри бросила на Нацуки разочарованный взгляд."
    y 1a "Эм, как бы то ни было..."
    y "Ты теперь в литературном клубе..."
    y "...Может, ты хочешь взять почитать какую-нибудь книгу?"
    mc "Ну..."
    mc "Отказаться я всё равно не могу."
    mc "Как ты и сказала, я теперь в литературном клубе."
    mc "Раз уж предлагаешь ты, мне кажется правильным заняться чем-то подобным."
    y 4b "П-подожди..."
    y "Я ведь ничего такого не имела в виду!"
    y "У-ум..."
    y "Если ты на самом деле не хочешь, то забудь о том, что я сказала..."
    mc "Ах— Нет, всё не так, Юри."
    mc "Я хочу постараться стать частью этого клуба."
    mc "Так что, пусть я и мало читаю, буду только рад взять книгу, если ты этого хочешь."
    y 3t "Т-ты уверен?.."
    y "Я просто хотела..."
    y 3u "...Ну, я ведь вице-президент..."
    y "...А значит, я должна помочь тебе найти занятие по душе."
    "Из своего портфеля Юри вытащила книгу."
    y 1s "Я не хотела, чтобы ты чувствовал себя не в своей тарелке..."
    y "Так что я выбрала книгу, которая, на мой взгляд, тебе понравится."
    y "Она довольно короткая, так что, даже если ты читаешь нечасто, уверена, она тебя увлечёт."
    y "И мы могли бы, ум-м..."
    show yuri at sink
    y 4b "Обсудить её... если захочешь..."
    "Э-это..."
    "Как у неё получается непреднамеренно быть такой бесконечно милой?"
    "Она даже не поленилась найти книгу, которая может мне понравиться, хотя я практически ничего не читаю..."
    mc "Спасибо большое, Юри! Я обязательно её прочту!"
    "Я с энтузиазмом взял книгу."
    show yuri 2m zorder 2 at t11
    y "Ах..."
    y 2a "Не нужно спешить, читай её в своём темпе."
    y "Я буду с нетерпением ждать твоего мнения."
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "Когда все расселись, я ожидал, что Моника пойдёт по плану мероприятий клуба."
    "Но похоже, что я ошибался."
    "Юри уже полностью погрузилась в книгу."
    "У неё такое сосредоточенное выражение лица, будто она весь день этого ждала."
    "Нацуки же копалась в кладовке."


    $ nextscene = poemwinner[0] + '_exclusive2_' + str(eval(poemwinner[0][0] + '_appeal'))
    call expression nextscene

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Фух..."
    "Кажется, все закончили."
    "Я обвёл комнату взглядом."
    "Это было напряжённее, чем я себе представлял."
    "Словно все осуждают меня за посредственные писательские способности..."
    "Даже если они этого не показывают, мои стихи ни за что не сравнятся с их уровнем."
    "Всё-таки это литературный клуб."
    "Я глубоко вздохнул."
    "Что ж, я сам себя в это втянул."
    "В другом конце комнаты Моника писала что-то в своей тетради."
    "Мой взгляд остановился на Юри с Нацуки."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Девушки робко обменивались стихами."
    show yuri 2i zorder 2 at t21
    "Когда они одновременно стали читать, я с интересом наблюдал, как изменяются выражения их лиц."
    "Нацуки недовольно нахмурила брови."
    "В то же время Юри печально улыбалась."
    show natsuki zorder 3 at f22
    n 1q "{i}(Что это за стиль такой?..){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "А?"
    y "Ум-м... ты что-то сказала?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "О, нет, ничего."
    "Нацуки пренебрежительно одной рукой положила тетрадь со стихом на стол."
    n "Пожалуй, можно сказать, что стих вышел довольно изящным."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ах... Спасибо..."
    y "А твой... милым..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Милым?"
    n 1h "Ты, что, вообще не заметила в нём символизма?"
    n "Он же пропитан чувством безысходности."
    n "Как такое можно назвать милым?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "Я э-это поняла!"
    y "Я имела в виду..."
    y 3h "Стихотворный слог, наверное..."
    y "Я просто хотела сказать что-нибудь хорошее..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "А?"
    n 4w "То есть тебе пришлось напрячься, чтобы выдавить из себя что-нибудь хорошее?"
    n "Спасибо, конечно, но в итоге ничего хорошего не вышло!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Ум-м..."
    y "На самом деле у меня есть пара предложений..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Хмф."
    n "Если бы мне были нужны советы, я бы спросила того, кому понравился мой стих."
    n "И такие люди, кстати, {i}есть{/i}."
    n 5e "Он понравился Монике."
    n "[player] тоже его похвалил!"
    n "И, раз уж у меня такой успех, я с радостью дам тебе парочку советов."
    n "Прежде всего—"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Прошу прощения..."
    y "Я ценю твоё предложение, но я уже долгое время совершенствую свой собственный стиль."
    y 2h "Я не собираюсь в ближайшее время его менять, разве что мне на глаза попадётся что-то поистине вдохновляющее."
    y "Но такого пока не случилось."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Н-н-н!.."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "И [player] мой стих тоже похвалил, позволь заметить."
    y "Он даже сказал, что был впечатлён."
    stop music fadeout 1.0
    "Нацуки резко встала."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "О, правда?"
    n "Я и не представляла, что ты так озабочена тем, чтобы впечатлить нашего нового члена, Юри."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "Э-э-э?!"
    y "Это вовсе не то, что я..."
    y 1o "У-у..."
    y "Ты... Ты просто..."
    "Юри тоже поднялась."
    y 2r "Может, ты просто завидуешь, что [player] мои советы ценит больше твоих?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Неужели! С чего это ты решила, что {i}мои{/i} он ценит меньше?"
    n "Ты настолько самовлюблённая?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "Я!.."
    y "Нет..."
    y "Будь я такой..."
    y 1r "...я бы точно из кожи вон лезла, чтобы делать всё слащаво-милым!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "У-у-у-у-ух!.."
    n "И вообще, знаешь что?!"
    n "Это не у меня сиськи волшебным образом выросли на один размер, с тех пор как [player] вступил в наш клуб!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "Н-Нацуки!"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "Эм, Нацуки, это немного—"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "Тебя это не касается!"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Так компенсировать собственную неуверенность за счёт других..."
    y "Твоё поведение соответствует твоей незрелой внешности, Нацуки."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "Это ты {i}мне?{/i} Чья бы корова мычала, жаждущая внимания стерва!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Жаждущая внимания?.."
    y 2r "Уж прости, что мой образ жизни слишком сложен для понимания человеком твоего психологического возраста!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "Видишь?"
    n "Эти слова только доказывают мою правоту!"
    n 4e "К твоему сведению, большинство людей после выпуска из средней школы уже умеют держать себя в руках."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Если ты хочешь что-то доказать, то избавь окружающих от своего отвратительного поведения!"
    y "Думаешь, что можешь компенсировать свой ядовитый характер яркими тряпками и милым поведением?"
    y 1k "Единственное, что в тебе милое, – то, как сильно ты стараешься выпятиться."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Эй, притормози, иначе порежешься на своих остротах, Юри."
    n "Ой, поздно... Ты ведь уже изрезалась?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "Т-ты только что обвинила меня, что я режу себя?"
    y 3r "У тебя, мать твою, совсем крыша поехала?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Ага, давай!"
    n "Пусть [player] услышит, что на самом деле творится в твоей голове!"
    n "Уверена, он после этого в тебя втрескается по уши!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "А-ах—!"
    show yuri zorder 2 at t21
    "Внезапно Юри повернулась ко мне, словно только сейчас заметила моё присутствие."
    show yuri zorder 3 at f21
    y 2n "[player]!.."
    y "Она... Она просто выставляет меня в дурном свете!.."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "Неправда!"
    n "Это она начала!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}Как меня вообще угораздило в это вляпаться?!{/cps}{nw}"
    "{cps=*2}Я ведь вообще не разбираюсь в поэзии...{/cps}{nw}"
    "{cps=*2}Но, какую бы из девушек я ни поддержал, я сразу же заслужу её расположение!{/cps}{nw}"
    "{cps=*2}Тогда я соглашусь с...{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Нацуки.":
                jump menu_click
            "Юри.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound 'sfx/s_kill_glitch1.ogg'
        pause 0.25
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "..."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "Эм..."
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "Эй, [player]..."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "Почему бы нам\nнемного не\nпрогуляться?"
    $ renpy.display_menu(items=[("Нацуки.", True), ("Юри.", True)], interact=False, screen='choice')
    m "Ты не против?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Прошу прощения за случившееся..."
    m "Не стоило им пытаться втянуть тебя в это."
    m 1e "Думаю, лучше нам держаться подальше от их склок..."
    m "Вернёмся внутрь, когда они перестанут голосить."
    m 5 "А-ха-ха..."
    m "Никудышный из меня президент, да?"
    m 1m "Не могу даже справиться с членами собственного клуба..."
    m "Хотела бы я уметь быть порой более настойчивой."
    m "Но мне никогда не хватало духу проявить твёрдость..."
    m 1e "Ты же понимаешь меня?"
    m "Как бы то ни было..."
    m 1a "Если после этого ты захочешь проводить с остальными меньше времени, ничего страшного."
    m 1j "Я буду рада проводить время с тобой вместо..."
    show monika zorder 1 at thide
    hide monika
    "Тут вдруг из класса выскочила Нацуки."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "Она быстро убежала прочь."
    show monika 1l zorder 2 at t11
    m "Боже..."
    m "...Кажется, они закончили..."
    scene bg club_day2
    with wipeleft_scene
    y "Не это хотела сказать..."
    y "Не это хотела сказать..."
    y "Не это хотела сказать..."
    "Юри сидела за партой и раскачивалась взад-вперёд, закрыв лицо руками."
    mc "Юри?.."
    show yuri 4d zorder 2 at t11
    y "Я не это хотела сказать!!!"
    mc "Я-я верю..."
    "Не представляю, что Юри могла сказать Нацуки."
    "Или сказала."
    y "[player]."
    y "Пожалуйста, не надо думать обо мне плохо."
    y "Пожалуйста!"
    y "Я не такая!"
    y "На меня сегодня что-то нашло..."
    show monika 1d zorder 3 at f31
    m "Всё хорошо, Юри."
    m "Мы знаем, что ты не имела в виду ничего такого."
    m 1j "Кроме того, я уверена, что до завтра Нацуки обо всём забудет."
    m 1a "Полностью."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "Как бы то ни было, собрание окончено, так что, если хочешь, можешь идти домой."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Мне показалось, что Юри хочет что-то сказать."
    "Но она продолжала смотреть на Монику."
    show yuri zorder 3 at f32
    y 2v "М-можешь идти первой, Моника..."
    y "Мне хотелось бы ещё немного побыть здесь."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "Как президент, я должна уходить последней."
    m "Подожду тебя."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Ну... Я вице-президент, так что..."
    y "Пожалуйста, позволь мне сегодня взять этот долг на себя."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "Звучит так, будто ты почему-то не хочешь, чтобы я была рядом, Юри."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "Э-это не так!"
    y 3o "Это не так..."
    y 3n "Я просто..."
    y 3q "[player] и я толком не имели возможности обсудить мою книгу..."
    y "Просто... неловко получится, если ты будешь слушать..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*Вздох*{/i}"
    m 1d "Получается, выбора у меня всё равно нет?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "П-прости, что причиняю проблемы..."
    $ gtext = glitchtext(20)
    y 1s "Но я искренне ценю твоё пониман{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "Но я искренне ценю твоё пониман{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
