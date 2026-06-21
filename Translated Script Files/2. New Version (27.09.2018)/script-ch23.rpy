

image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                'images/sayori/noface1.png'
            choice:
                'images/sayori/noface1b.png'
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    'images/sayori/noface2.png'
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound 'sfx/gnid.ogg'
        $ pause(7)
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "Привет, [player]!"
    y "Я ждала тебя."
    y 2d "Ты готов продолжить чтение?"
    y "Сегодня я приготовила свой лучший чай—"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Моника!"
    n "Я же говорила тебе не—"
    n 1g "Эх..."
    n "Офигеть, она снова опаздывает?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Бесцеремонна, как всегда, Нацуки."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Прошу прощения?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Ты так и будешь ежесекундно прерывать меня своим криком?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "О чём ты говоришь?!"
    n 1q "Тебя послушать, получается, будто я постоянно так делаю."
    n "Я просто не обращала внимания. Извини."
    n 4u "Серьёзно... Что с тобой в последнее время?"
    if n_appeal >= 2:
        n "Послушай..."
        n "Я тут думала о вчерашних событиях..."
        n 2q "Я была немного на взводе..."
        n 1q "Наверное, я чувствовала угрозу или что-то типа того."
        n 1h "Но я понимаю, что это наше общее дело."
        n 1q "Новички не навредят, если они будут клёвыми..."
        n 5w "И, думаю, было бы здорово, если на этот раз к нам присоединится девочка..."
        n 5u "Так что..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Нацуки..."
        $ style.say_dialogue = style.edited
        y 1f "Всем наплевать."
        y "Почему бы тебе не пойти искать монетки под торговыми автоматами или типа того?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "—!"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        $ pause(1.0)
        show monika 1g at l31
        m "Ой, ну надо же..."
        m "Я снова пришла последней!"
        show yuri zorder 3 at f32
        y 1f "Опять практиковалась в игре на пианино?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Да..."
        m "А-ха-ха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Ты полна решимости."
        y "Открыла новый клуб, стала учиться игре на пианино..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Хм, я не называла бы это решимостью..."
        m 3a "Скорее страстью."
        m "Она же побуждает меня хорошенько потрудиться для фестиваля."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "Со мной?"
        y 2o "Н-ничего..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Неужели всё настолько плохо?.."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "Видишь же, что {i}да{/i}."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "Я справлюсь!"
        y 3y6 "Это даже не заслуживает внимания..."
        y 3o "Просто я в последнее время немного на взводе..."
        y 3n "В общем, нам не за чем об этом говорить!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Ну, мне просто показалось, что это нужно обсудить."
        n 5q "Не то чтобы меня это действительно волновало..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Ой, ну надо же..."
        m "Я снова пришла последней!"
        show natsuki zorder 3 at f33
        n 2c "Да ладно, [player] тоже только что подошёл."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "Опять практиковалась в игре на пианино?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Да..."
        m "А-ха-ха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Ты полна решимости."
        y "Открыла новый клуб, стала учиться игре на пианино..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Хм, я не называла бы это решимостью..."
        m 3a "Скорее страстью."
        m "Она же побуждает меня хорошенько потрудиться для фестиваля."
        m 3n "Ой..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Точно..."
        m "Я-я забыла..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Нацуки, касательно этого..."
        y "Мы тут вчера поговорили и..."
        y 2t "Ум-м... решили, что тоже поддержим фестиваль."
        y 2l "Тем не менее!.."
        y 2h "Я понимаю твоё нежелание перемен в клубе."
        y "Думаю, мы все чувствуем то же самое."
        y 2f "Но до тех пор, пока мы работаем сообща, этот клуб никогда не станет чем-то, чего мы не хотим."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Ум-м, и ещё..."
        y "Если ты поможешь нам с фестивалем..."
        y 3r "...Я куплю тебе новую мангу!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "А-ха-ха-ха!"
        n "Извини, последняя часть была очень уж смешная."
        n 2c "Послушай..."
        n "Я тут думала о вчерашних событиях..."
        n 2q "Я была немного на взводе..."
        n 1q "Думаю, я действительно почувствовала что-то вроде угрозы."
        n 1h "Но я понимаю, что это наше общее дело."
        n 1q "Новички не навредят, если они будут клёвыми..."
        n 5w "И, думаю, было бы здорово, если на этот раз к нам присоединится девочка..."
        n 5e "...Но, что более важно, я не хочу увидеть, как вы облажаетесь только из-за того, что я решила не принимать в этом участия!"
        n "Я ведь профессионал, сами знаете!"
        n 5c "Так что я помогу и, можете быть уверены, всё получится на высшем уровне."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Слава богу..."
        y "Разве это не здорово, Моника?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...Моника?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Э—"
        m 1n "Да, это чудесно!"
        m "Без тебя было бы уже не то, Нацуки."
    m 5 "В любом случае, [player]..."
    m "Чем бы ты хотел сегодня заняться?"
    m "Думаю, мы могли бы—"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "У нас уже есть планы на сегодня."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "А..."
    m "Вот как, Юри?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "Именно так."
    y "[player] увлёкся романом, который мы вместе читаем."
    y 1y5 "Разве ты не рада, что я уже приобщила его к литературе, Моника?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "Я..."
    m "Пожалуй..."
    m "Я просто—"
    m 1r "Ладно, это не важно."
    m 1i "Правда не важно."
    m "Можете делать что хотите."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(Да!){/i}{w=0.5}{nw}"
    y 2u "Ум-м... Спасибо за понимание, Моника."
    if poemwinner[2] == 'natsuki':
        $ poemwinner[2] = 'yuri'
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    $ config.skipping = False
    call screen confirm('', Return(True), Return(True))
    if _return:
        call expression 'poem_special_' + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Итак, друзья!"
    m "Пора определиться с приготовлениями к фестивалю."
    m 1i "Давайте поскорее покончим с этим."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Блин..."
        n "Почему атмосфера сегодня такая странная?"
        n "Смотрите, даже Юри не избежала её влияния."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "У-у..."
    y "Затишье обычно предшествует буре..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Слушайте, мы можем просто сделать вот что:"
    m 2d "Я распечатаю и соберу буклеты со стихотворениями."
    if n_appeal >= 2:
        m 2i "Нацуки, ты можешь испечь кексы."
        m "Я знаю, что это у тебя хорошо получается."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Нацуки, ты—"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "Я хочу испечь кексы!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Да, именно это."
        m "Рада, что мы на одной волне."
    m 1m "Юри, ты можешь..."
    m 1r "...Впрочем, не важно."
    m 1i "Можешь делать что угодно, если считаешь, что это поможет."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Моника..."
    y "Я вовсе не бесполезная!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "З-знаю!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "Я уже решила, чем хочу заняться."
    y 1h "Мы не сможем провести успешное поэтическое мероприятие без соответствующей случаю атмосферы."
    y "Так что я займусь украшениями и освещением."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "Правда?"
    m "Замечательная идея!"
    m 1a "Значит, у каждого из нас есть дело."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Э?"
    y "А как же [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] будет помогать мне."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Погоди, тебе?"
    n "Моника, у тебя же самое простое задание!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Прости, но будет так, как я сказала."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Чёрта с два!"
    n "Чего ты пытаешься добиться?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "Я-я согласна с Нацуки!"
    y "Твоя задача как нельзя лучше подходит для одного человека..."
    y 3l "А вот моя достаточно трудоёмкая, чтобы извлечь немалую пользу из лишней пары рук."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Моя тоже!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "Что, твои кексы?"
    y "Я тебя умоляю."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    if persistent.allow_slang:
        n 1o "Будто {i}ты{/i} охуительно в этом разбираешься!"
    else:
        n 1o "Будто {i}ты{/i} что-то в этом понимаешь!"
    n 1x "Всё, что тебя сейчас волнует, – сделать так, чтобы [player] таскался рядом с тобой и твоими идиотскими книжками."
    n 1f "Тебя {i}и{/i} Монику!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Эй!"
    m "Я же ничего не делала!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Ладно, тогда пусть [player] решает, кому помогать, и нечего злоупотреблять своей властью!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "Я не... злоупотребляла."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Злоупотребляла, Моника."
    y "Просто пусть [player] выберет, хорошо?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Что ж, хорошо!"
    m "Идёт."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Блин..."
    n "[player], я знаю, как тебе уже надоели эти двое."
    n 3c "Мы можем просто—"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    if persistent.allow_slang:
        y 2r "Нацуки, завали ебало и дай ему выбрать самому."
    else:
        y 2r "Нацуки, захлопни пасть и дай ему выбрать самому."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    if persistent.allow_slang:
        n 1o "{i}Сама{/i} завали!"
    else:
        n 1o "{i}Сама{/i} захлопни!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Господи..."
    m 1i "Это никогда не закончится. Просто выбери кого-нибудь, хорошо?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("Нацуки.", "natsuki"), ("Юри.", "yuri"), ("Моника.", "monika")], screen='rigged_choice')

    if madechoice != 'monika':
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        $ pause(3.0)
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
        scene bg club_day
        $ audio.t3m = '<from ' + str(musicpos) + ' loop 4.618>bgm/3.ogg'
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "Ура, ты выбрал меня!"
    m "Можем на выходных встретиться у тебя дома."
    m "Обещаю, будет весело."
    m "В воскресенье тебе удобно?"
    show natsuki 1e zorder 3 at f31
    if persistent.allow_slang:
        n "Ты что, бля, издеваешься?"
    else:
        n "Ты что, издеваешься?"
    n "Это ни капельки не честно!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "Всё по-честному, Нацуки."
    m "Он сам так решил."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "Нет, это нечестно!"
    y "Свалила на нас всю эту работу, а теперь ещё и [player] будет с тобой."
    y "Тебе должно быть стыдно!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Юри, я тебя вообще ни о чём не просила."
    m 2i "Ты всё решила сама."
    m "Так что твои претензии безосновательны."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "Безосновательны?"
    y 2y3 "А-ха-ха-ха!"
    y "Моника, не могу поверить, что ты настолько помешанная и самовлюблённая!"
    y "Всякий раз, как ты оказываешься не у дел, из кожи вон лезешь, чтобы [player] пошёл с тобой."
    y 1y1 "Ты ревнуешь?"
    y "Съехала с катушек?"
    y 1y3 "Или, может, ты настолько сильно ненавидишь себя, что перекладываешь это на других?"
    y 1y4 "У меня к тебе предложение. Ты никогда не думала о самоубийстве?"
    y "Это будет полезно для твоего душевного здоровья."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Юри, ты меня немного пугаешь..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Нацуки, давай просто уйдём."
    m 1i "Не думаю, что она сейчас хочет нас видеть."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "Видишь? Это совсем не сложно."
    y "Всё, чего я хочу, – провести немного времени вместе с ним."
    y "Неужели я многого прошу?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Юри провожает Монику и Нацуки до двери."
    show monika 5a zorder 2 at t11
    m "Эй, [player]..."
    m "Юри у нас просто нечто, согласен?"
    show monika zorder 1 at thide
    hide monika
    "Юри выталкивает хихикающую Монику за дверь."
    python:
        try: open(user_dir + "/хороших выходных!", "rb") 
        except: open(user_dir + "/хороших выходных!", "w").write("0KfRgtC+INGN0YLQviDQt9CwINGH0LXQu9C+0LLQtdC6LCDQutC+0YLQvtGA0YvQuSDQvdC1INCy0LTQvtGF0L3Rg9C7INC90LDRgdGL0YnQtdC90L3Ri9C5INCw0YDQvtC80LDRgiDQsdGD0LTRg9GJ0LXQs9C+LCDQvdC1INC40YHQv9GL0YLQsNC7INGH0LDRgNGD0Y7RidC40LksINC60L7QvNC/0LvQtdC60YHQvdGL0Lkg0LHQsNC70LDQvdGBINC90LDRgdGC0L7Rj9GJ0LXQs9C+INC4INC90LUg0L7RidGD0YLQuNC7INCz0L7RgNGM0LrQvi3RgdC70LDQtNC60L7QtSDQv9C+0YHQu9C10LLQutGD0YHQuNC1INC/0YDQvtGI0LvQvtCz0L4/")
        try: os.remove(user_dir + "/счхстлхвые мхсли.png") 
        except: pass
        try: os.remove(user_dir + "/ТЫ МЕНЯ СЛЫШИШЬ.txt") 
        except: pass
        try: os.remove(user_dir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt") 
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Наконец-то."
    y 2y1 "Наконец-то!"
    y 2s "Это всё, чего я хотела."
    y 1y6 "[player], нет никакой необходимости встречаться на выходных с Моникой."
    y "Не слушай её."
    y 1y5 "Лучше приходи ко мне."
    y 3y5 "Целый день мы будем только вдвоём..."
    y "Правда, здорово звучит?"
    y 3y1 "А-ха-ха-ха!"
    y 3y4 "Ой... Кажется, со мной и правда что-то не так?"
    y "Но знаешь что?"
    y 1y3 "Мне уже наплевать."
    y "Я за всю свою жизнь не чувствовала себя так хорошо."
    y 1y4 "Просто быть с тобой – это куда большее удовольствие, чем я могла представить."
    y "Я связана с тобой."
    y 3y4 "Кажется, будто я умру, если не буду дышать с тобой одним воздухом."
    y 4a "Разве не замечательно, когда есть кто-то, кто так сильно заботится о тебе?"
    y "Тот, кто захочет посвятить тебе всю свою жизнь."
    y 2y6 "Это невообразимо приятное чувство..."
    y 2y4 "Так почему же во мне всё сильнее крепнет ощущение, что случится нечто ужасное?"
    y 2y6 "Наверное, из-за него я и пыталась поначалу сдерживать себя..."
    y "Но теперь это ощущение слишком сильно."
    y 3y1 "Мне уже всё равно, [player]!"
    y "Я должна сказать тебе!"
    y 3y4 "Я... я безумно люблю тебя!"
    y "Кажется, будто каждая клеточка моего тела... каждая капля крови... выкрикивает твоё имя."
    y 3y3 "Меня больше не волнуют последствия!"
    y "Плевать, если Моника услышит!"
    y 3w "Я просто хочу, чтобы ты знал, как сильно я люблю тебя, [player]."
    y 3m "Люблю так сильно, что ублажаю себя ручкой, которую украла у тебя."
    y 3y4 "Мне хочется разорвать твою плоть и заползти внутрь тебя."
    y 3y6 "Я хочу, чтобы ты полностью принадлежал мне."
    y "А я – только тебе."
    y "Разве не изумительно это звучит?"
    y 3s "Скажи мне, [player]."
    y "Скажи, что хочешь быть моим возлюбленным."
    y "Ты принимаешь моё признание?"

    menu:
        "Да.":
            jump yuri_kill
        "Нет.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    $ pause(1.0)


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = 'yuri_kill_1'
    $ renpy.save_persistent()
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "...А-ха-ха-ха-ха."
    y "А-ха-ха-ха-ха-ха-ха-ха!"
    $ style.say_dialogue = style.normal
    y 3y5 "А-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха!"
    $ style.say_dialogue = style.edited
    y 3y3 "А-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound 'sfx/yuri-kill.ogg'
    $ starttime = datetime.datetime.now()
    $ pause(1.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_1
    $ pause(2.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    $ pause(3.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_3
    $ pause(4.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve('images/yuri/stab/4_wipe.png', 0.25)
    $ pause(5.68 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_5
    $ pause(6.38 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    hide blood
    hide blood2
    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall
    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black
    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = 'yuri_kill_2'
    $ renpy.save_persistent()
    python:
        _history_list = []
        m.add_history(None, "", """Добро пожаловать в литературный клуб! Я всегда мечтала сделать из того, что мне нравится, нечто особенное. Теперь ты член клуба и можешь помочь мне воплотить мою мечту в реальность в этой милой игре!Каждый день будет полон болтовни и мероприятий со всеми моими обожаемыми и уникальными членами клуба:Саёри, молодого пучка солнца, который превыше всего ценит счастье;Нацуки, которая под обманчиво милой внешностью скрывает агрессивный характер;Юри, робкой и загадочной особы, которая находит отраду в мире книг;...И, разумеется, Моники, лидера клуба! Это я!Я очень рада, что ты со всеми подружился и помог сделать литературный клуб сокровенным местом для всех его участников. Но я уже поняла, что ты хороший,—обещаешь проводить большую часть времени со мной?Добро пожаловать в литературный клуб! Я всегда мечтала сделать из того, что мне нравится, нечто особенное. Теперь ты член клуба и можешь помочь мне воплотить мою мечту в реальность в этой милой игре!Каждый день будет полон болтовни и мероприятий со всеми моими обожаемыми и уникальными членами клуба:Саёри, молодого пучка солнца, который превыше всего ценит счастье;Нацуки, которая под обманчиво милой внешностью скрывает агрессивный характер;Юри, робкой и загадочной особы, которая находит отраду в мире книг;...И, разумеется, Моники, лидера клуба! Это я!Я очень рада, что ты со всеми подружился и помог сделать литературный клуб сокровенным местом для всех его участников. Но я уже поняла, что ты хороший,—обещаешь проводить большую часть времени со мной?Добро пожаловать в литературный клуб! Я всегда мечтала сделать из того, что мне нравится, нечто особенное. Теперь ты член клуба и можешь помочь мне воплотить мою мечту в реальность в этой милой игре!Каждый день будет полон болтовни и мероприятий со всеми моими обожаемыми и уникальными членами клуба:Саёри, молодого пучка солнца, который превыше всего ценит счастье;Нацуки, которая под обманчиво милой внешностью скрывает агрессивный характер;Юри, робкой и загадочной особы, которая находит отраду в мире книг;...И, разумеется, Моники, лидера клуба! Это я!Я очень рада, что ты со всеми подружился и помог сделать литературный клуб сокровенным местом для всех его участников. Но я уже поняла, что ты хороший,—обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со мной?обещаешь проводить большую часть времени со""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = '<from ' + audiostart + ' loop 43.572>bgm/6s.ogg'
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(user_dir + '/хороших выходных!') 
        except: pass
    $ persistent.autoload = 'yuri_kill_3'
    $ renpy.save_persistent()
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = '<from ' + audiostart + ' loop 43.572>bgm/6s.ogg'
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Ну вот и начался фестиваль!"
    show natsuki 4k zorder 2 at t11
    n "Ого, ты пришёл сюда раньше меня?"
    n "Я думала, что вышла довольно ра—{nw}"
    show natsuki scream at h11
    n "А-АГХ!!"
    n "А-А-А-А-А-А-А-А-А-А-А-А-А-А-А!!!"
    $ pause(1.0)
    show natsuki scream at h11
    $ pause(0.75)
    show natsuki vomit at h11
    $ pause(1.25)
    show natsuki at lhide
    hide natsuki
    "Нацуки убегает."
    m "..."
    show monika 2b zorder 2 at t11
    m "А вот и я!"
    m 2d "[player], что-то случилось?"
    m "Мимо меня только что пробежала Нацуки..."
    m 2i "...Ой..."
    m "...Ох."
    m 2r "..."
    m 2l "А-ха-ха-ха!"
    m "Ой, вот ведь незадача."
    m 2d "Подожди, [player], ты провёл здесь все выходные?"
    m "О боже..."
    m 2g "Я и не думала, что скрипт повреждён так сильно."
    m "Мне очень жаль!"
    m "Наверное, было довольно скучно..."
    m 2e "Я всё исправлю, ладно?"
    m "Дай мне секундочку..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character('yuri')
    $ pause(1.0)
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character('natsuki')
    $ pause(1.0)
    if persistent.allow_joke:
        m 2a "Я почти кончила."
    else:
        m 2a "Я почти закончила."
    m 2j "Просто захотелось по-быстренькому съесть кексик!"
    $ gtext = glitchtext(10)
    "Моника поднимает салфетку с подноса и берёт испечённый [gtext] кекс."
    m 2b "Серьёзно, они просто великолепны!"
    m "Я просто обязана взять один, ведь больше возможности не будет."
    m 2a "Я имею в виду, они скоро перестанут существовать."
    m "...Но я всё равно не должна больше заставлять тебя ждать."
    m 2j "Просто потерпи, ладно?"
    m 2a "Это займёт всего секунду."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = 'ch30_main'
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label='splashscreen')

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
