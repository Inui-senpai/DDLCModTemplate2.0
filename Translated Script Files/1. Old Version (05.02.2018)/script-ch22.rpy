image yuri half = 'images/yuri/1l.png'
image yuri_half2:
    'images/yuri/1r.png'
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "Подходит к концу ещё один учебный день, и вот уже наступило время для очередной встречи клуба."
    "За последние пару дней я попривык и стал чувствовать себя комфортнее."
    "При входе в класс меня встретила привычная сцена."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "С возвращением, [player]..."
    hide yuri_half2
    mc "О, привет, Юри..."
    "Не уверен, мне показалось, или дело в выражении лица Юри..."
    "Но в комнате до сих пор чувствовалась тяжесть вчерашней ссоры."
    y 2v "Э-эм..."
    "Юри оглянулась через плечо, рассматривая комнату."
    "Нацуки сидела за партой и читала мангу."
    "А Моника, как ни удивительно, пока не пришла."
    "Юри вдруг схватила меня за руку и потащила в угол комнаты."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "Насчёт вчерашнего..."
    y "Я..."
    y 2v "Я должна извиниться."
    y "Раньше ничего подобного не случалось..."
    y 2t "И... на меня что-то нашло, кажется..."
    y "Я не понимала, что делаю."
    y 2w "Пожалуйста, не думай, что я всегда такая!"
    y "И это касается не только меня, но и Нацуки тоже..."
    show yuri 2t
    mc "Юри..."
    mc "Я рад, что ты сочла нужным извиниться."
    mc "Не переживай так сильно."
    mc "Пусть я здесь всего пару дней, но я догадался, что вчера произошло нечто из ряда вон..."
    mc "Может, ты отреагировала так остро из-за того, что это было первое стихотворение, которым ты с кем-то поделилась."
    mc "Но, как бы то ни было..."
    mc "Из-за этого я не стал думать о тебе хуже."
    mc "Я уже понял, что ты просто не можешь быть плохим человеком."
    mc "И теперь, когда ты извинилась, я понимаю, что ты действительно не хотела этого."
    y 3t "А-ах..."
    y "[player]..."
    y 3u "Не говори о подобных вещах так открыто..."
    y "От таких слов меня переполняет счастье."
    y 1s "Я очень рада, что ты такой понимающий человек..."
    y "И что ты присоединился к нашему клубу."
    y "Всё становится немного ярче, когда ты рядом, и—"
    y 1t "Ах—"
    y 4c "Прости, что я сейчас сказала?.."
    y "Я просто—"
    show natsuki 2c zorder 3 at f33
    n "Эй, вы Монику не видели?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "Ах—!"
    mc "Я не видел..."
    mc "Мне и самому интересно, куда она запропастилась."
    show natsuki zorder 3 at f33
    n 5g "Блин..."
    n 5c "Юри, я так понимаю, ты тоже не видела?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Юри явно сбило с толку то, как спокойно к ней обратилась Нацуки."
    y "Н-нет, не видела..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Это на неё совсем не похоже."
    n "Знаю, что это глупо, но не могу не волноваться за неё..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "Что?"
    n "Почему ты так на меня смотришь?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Э-эм..."
    y "Нацуки, насчёт вчерашнего..."
    y 3w "Я-я хочу извиниться!"
    y "Насчёт всего, что я наговорила... Клянусь, на самом деле я так вовсе не считаю!"
    y 3t "Впредь я буду делать всё, чтобы держать себя в руках..."
    y "Поэтому—"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Юри, ты, вообще, о чём?"
    n "Ты вчера что-то сделала?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "...А?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "Блин..."
    $ style.say_dialogue = style.edited
    n "Что бы ты там ни вбила себе в голову, уверена – это пустяки."
    n "Я даже не помню, чтобы случилось что-то плохое."
    n "Или ты из тех, кто раздувает из мухи слона?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."
    y "Н-но..."
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show yuri zorder 2 at t32
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "сетчатый канифас слепозрения по линии жизни Анат ректипетальностью безукоризненно предложил склеромаляцию заржавшему католикосу"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "Но, если тебе от этого станет легче, я принимаю твои извинения."
    n "Мне даже приятно это слышать, поскольку я всегда опасалась, что ты втайне ненавидишь меня или что-то в этом роде."
    n 2z "Э-хе-хе."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "В-вовсе нет!.."
    y "С чего мне тебя ненавидеть?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "А-ха-ха."
    n "Ум-м, ты довольно странная, но я тоже не испытываю к тебе ненависти."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "Нацуки повернулась ко мне."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "Между прочим, ты пока на испытательном сроке."
    show natsuki zorder 2 at t33
    mc "Эй!.."
    "Внезапно дверь с хлопком распахнулась."
    show monika 1g at l41
    m "Простите! Я ужасно виновата!"
    mc "А, вот и ты..."
    show monika zorder 3 at f41
    m "Я не хотела опаздывать..."
    m "Надеюсь, вы, ребята, за меня не волновались!"
    show monika zorder 2 at t41
    mc "Нет..."
    mc "Впрочем, Нацуки переживала."
    show natsuki zorder 3 at f33
    n 1p "Н-неправда!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "А-ха-ха."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "...Кстати, почему ты так задержалась?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "А..."
    m "Просто на последнем уроке у нас было самостоятельное обучение."
    m "И, если честно, я там потеряла счёт времени..."
    m "А-ха-ха..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "Ерунда какая-то."
    n "Ты бы, по крайней мере, услышала звонок."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "Я, наверное, не услышала из-за того, что практиковалась в игре на пианино..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "Пианино?.."
    y "Я не знала, что ты ещё и музыкой занимаешься."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "О, не стоит хвалить меня сильнее, чем я того заслуживаю."
    m 1m "Хоть я и занимаюсь уже довольно давно, но играю пока неважно."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "Но всё же..."
    y "Это наверняка требует много сил."
    y "Так что я всё равно впечатлена."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "Э, ну, спасибо, Юри~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "Ты просто обязана как-нибудь сыграть для нас!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "А-ха-ха, насчёт этого..."
    "Моника взглянула на меня."
    m 1a "Ну, я сейчас пишу песню, но она пока не готова..."
    m "Может быть, когда я стану лучше играть."
    show monika zorder 2 at t41
    mc "Было бы здорово."
    mc "Жду с нетерпением."
    show monika zorder 3 at f41
    m 1b "Правда?"
    m "В таком случае..."
    m "Я тебя не разочарую, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "На лице Моники появилась нежная улыбка."
    mc "Ах..."
    mc "Только ты не подумай, что я давлю на тебя или что-то такое!"
    m 1a "А-ха-ха, не волнуйся."
    m "Я сама надеялась, что смогу поделиться своей песней."
    m "Думаю, поэтому я столько и репетировала в последнее время."
    mc "Ясно..."
    "Не уверен, обращалась Моника ко всему клубу или только ко мне..."
    mc "В таком случае удачи тебе."
    m 1j "Спасибо~!"
    m 1a "Я ничего не пропустила?"
    mc "Нет... ничего такого."
    show monika zorder 1 at thide
    hide monika
    "Я предпочёл не упоминать о том, что здесь было сказано ранее."
    "Кроме того, Нацуки уже закрылась в кладовке."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Ум-м..."
    y "Поскольку ты своими комплиментами поднял мне настроение..."
    y "Я тут подумала, не хотел бы ты сегодня провести немного времени вместе?"
    y 3o "Я имею в виду— в клубе!"
    if poemwinner[0] == 'natsuki':
        $ y_appeal = 1
        mc "Да, пожалуй."
        mc "Не думаю, что могу отказаться, после того как ты дала мне ту книгу."
        mc "Только проверю, не ждёт ли меня Нацуки."
        mc "После того как мы вчера закончили читать, она—"
        if n_appeal >= 2:
            y 3r "Всё с ней нормально!"
            $ style.say_dialogue = style.normal
            y 3h "Вон она уже читает. Видишь?"
            $ style.say_dialogue = style.edited
            y 3f "Не думай о ней слишком много."
            y "Она привыкла, что на неё не обращают внимания."
            y "Ну же, давай сядем вон там."
            $ style.say_dialogue = style.normal
            window hide(None)
            define audio.t6_apg = '<from ' + str(get_pos()) + ' loop 10.893>bgm/6.ogg'
            stop music
            scene black
            window auto
            pause 2.0
            play music t6_apg
            jump ch22_main2
        else:
            y 3r "В-всё с ней нормально!"
            y 3h "Вон она уже читает."
            y 3y6 "Так что всё в порядке, верно?"
            mc "А—"
            mc "Тогда я не вижу никаких препятствий..."
    else:
        $ y_appeal = 2
        mc "Да, определённо."
        mc "Всё равно я так и собирался сделать."
    show yuri zorder 2 at h11
    y 3y5 "Отлично!"
    y "Значит, можем начинать?"
    y "Давай найдём, куда сесть—"
    y 3n "Ой—"
    y "Я была чересчур настойчива?.."
    y 4c "Прости!"
    y "У меня сердце... почему-то бешено колотится..."
    mc "Не переживай ты так."
    mc "Мне даже приятно видеть, что ты полна энтузиазма."
    y 3q "Д-да!"
    y "Но..."
    y 3j "Мне надо попробовать успокоиться."
    y "В таком состоянии я не смогу сосредоточиться на чтении..."
    mc "Не торопись."
    "Юри сделала глубокий вдох и достала из портфеля книгу."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = 'yuri'


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = 'yuri_exclusive2_' + str(eval('y_appeal')) + '_ch22'
    call expression nextscene

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("Вы разблокировали особое стихотворение.\nЖелаете прочесть?", Return(True), Return(False))
    if _return:
        call expression 'poem_special_' + str(persistent.special_poems[1])
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid('ff0000') as i1 onlayer front:
            additive 1.0
        show expression Solid('#440000') as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {'default': [
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head.png', 0, 0),
                                    ('gui/mouse/s_head.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head2.png', 0, 0),
                                    ('gui/mouse/s_head.png', 0, 0),
                                    ]}



    m "Итак, друзья!"
    m "Все закончили с чтением стихов?"
    $ config.mouse = None
    m "Я хотела со всеми вами поговорить кое о чём, не могли бы вы собраться передо мной?"
    show natsuki 3c zorder 3 at f31
    n "Это насчёт фестиваля?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Вроде того~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Уф, нам и правда нужно в нём участвовать?"
    n "Я сомневаюсь, что всего за несколько дней мы сможем подготовить что-нибудь интересное."
    n "Вместо привлечения новых членов мы, скорее всего, просто опозоримся."
    if faint_effect:
        define audio.t3_apg = '<from ' + str(get_pos() + 2.0) + ' loop 4.618>bgm/3.ogg'
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "Меня это также беспокоит."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music t3_apg
    y "Приготовления в последнюю минуту – не мой конёк..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "Да не волнуйтесь вы так!"
    m "Мы сделаем всё по-простому, идёт?"
    m 2a "Послушайте..."
    m 2m "Я знаю, что все стали несколько более... оживлёнными... с тех пор, как к нам присоединился [player] и мы начали заниматься клубной деятельностью."
    m 2d "Но сейчас нам нельзя сбавлять обороты."
    m "Нас по-прежнему всего четверо..."
    m 2a "И фестиваль – единственный наш шанс найти новых членов. Вы это понимаете?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "А что такого хорошего в новых участниках?"
    n "Нас уже достаточно для официальной регистрации клуба."
    n "Новые члены означают только то, что здесь станет более шумно и появятся новые организационные сложности."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Нацуки..."
    m "Я не думаю, что ты смотришь на это с верной точки зрения."
    m "Разве ты не хочешь поделиться своим увлечением с как можно большим количеством людей?"
    m 3e "Вдохновить их на поиски тех же чувств, что изначально привели тебя сюда?"
    m "Литературный клуб должен стать местом, где люди смогут проявить себя так, как не смогут ни в каком другом месте."
    m "Он должен стать настолько уютным, что тебе не захочется отсюда уходить."
    m 2e "Я знаю, что ты тоже разделяешь мои чувства."
    m 2b "Знаю, что все здесь их разделяют!"
    m "Ради этого мы должны как следует постараться и подготовить что-нибудь к фестивалю... пусть даже какую-нибудь мелочь!"
    m "Верно, [player]?"
    show monika 2a zorder 2 at t32
    mc "Э..."
    show natsuki zorder 3 at f31
    n 42c "Да ладно!"
    n "Что толку, что [player] согласится, если он вообще не умеет говорить «нет»."
    stop music fadeout 1
    n 1c "Послушай, Моника."
    n "Ты действительно считаешь, что хоть кто-то из нас, присоединяясь к клубу, думал о других?"
    n "Юри даже ни с кем не разговаривала, пока здесь не появился [player]."
    n 2b "Мне же просто больше нравится здесь, чем дома."
    n "А [player] изначально вообще литературой не увлекался."
    n "И так со всеми."
    n 4w "Прости, но ты тут единственная, кто заинтересован в новичках."
    n "Остальных и так всё устраивает."
    n 4q "Я понимаю, что ты президент и всё такое, но ты должна учитывать и наше мнение."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "Речь Нацуки явно ошарашила Монику."
    play music t9
    m 1m "Это... неправда."
    m 2m "Я уверена, что Юри и [player] тоже хотят, чтобы к нам присоединились новички..."
    m 2p "...Ведь так?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "За Юри не поручусь, но лично мне всё равно."
    "Если я продемонстрирую энтузиазм, которого так ждёт Моника, то совру."
    "Тем не менее, если уж разрешать эту ситуацию выпало мне..."
    mc "Эм—"
    show monika zorder 3 at f32
    m 1i "Ясно."
    m "Нацуки ведь права, да?"
    m 1g "Этот клуб..."
    m "Всего-лишь место, где несколько человек убивают время."
    m 1r "С чего я взяла, что все здесь смотрят на вещи так же, как и я?"
    show monika zorder 2 at t32
    mc "Но это не значит, что мы возражаем против новичков..."
    show monika zorder 3 at f32
    m 1i "[player], почему ты вступил в этот клуб?"
    m "Что ты надеялся здесь найти?"
    show monika zorder 2 at t32
    mc "Ну—"
    "Этот вопрос не из тех, на которые я могу ответить честно, ведь так?"
    show monika zorder 3 at f32
    m 1p "В общем-то..."
    m "Насколько я помню, выбора «не вступать» у тебя не было."
    show monika zorder 1 at thide
    hide monika
    "Моника села и уставилась в парту."
    m "Так какой во всём этом смысл?"
    m "Что, если создание клуба было ошибкой?"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "На этот раз виновата ты, Нацуки..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "А что я?"
    n 1s "Я просто сказала что думаю..."
    n "Или быть честной – преступление?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "Речь не о честности..."
    y "...а о выборе выражений."
    y 2h "У тебя нет права разговаривать в таком тоне ни с кем в клубе..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "Ты ничего не понимаешь!"
    n 5s "Я просто..."
    n "Я просто хотела, чтобы было место, где можно приятно провести время с друзьями."
    n 5u "Или есть какие-то проблемы в том, как я воспринимаю клуб?"
    n "Я нигде... нигде не смогу найти другое такое место..."
    n 5x "А теперь Моника хочет отобрать его у меня!"
    show natsuki zorder 2 at t31
    mc "Она ничего не отбирает—"
    show natsuki zorder 3 at f31
    n 1g "Нет, [player]."
    n "Он изменится."
    n 1q "Он не останется прежним с выбранным ей курсом."
    n "Если бы я хотела этого, то могла бы просто присоединиться к любому другому дурацкому клубу."
    n 12d "Но этот..."
    n "Я хочу сказать..."
    n 12e "Хотя бы какое-то время..."
    n "Здесь было здорово."
    "Нацуки начала собирать вещи."
    n 12d "Я иду домой."
    n "Я чувствую... что мне сейчас здесь не место."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Нацуки..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Нацуки, игнорируя Юри, пошла прямиком к выходу из класса."
    show yuri zorder 2 at t11
    y 3v "..."
    y "Это плохо..."
    y "Я не знаю, что делать..."
    mc "Ну..."
    mc "У тебя есть какое-нибудь мнение насчёт фестиваля?"
    y 4b "Н-не знаю..."
    $ style.say_dialogue = style.normal
    y "Думаю, мне всё равно..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    define audio.t9g_apg = '<from ' + str(get_pos() / 2.07) + ' loop 1.532>bgm/9g.ogg'
    play music t9g_apg
    y "Кому какое дело до этой несносной соплячки?"
    $ style.say_dialogue = style.normal
    define audio.t9_apg = '<from ' + str(get_pos() * 2.07) + ' loop 3.172>bgm/9.ogg'
    play music t9_apg
    hide black
    hide y_glitch_head
    y "Мне нравится, как сейчас тихо в клубной комнате, как хорошо..."
    y "И я просто... счастлива, что здесь есть ты..."
    y 2t "Но всё же!.."
    y "Я вице-президент..."
    y "Я не должна вот так наплевательски относиться к своим обязанностям..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    define audio.t9g_apg = '<from ' + str(get_pos() / 2.07) + ' loop 1.532>bgm/9g.ogg'
    play music t9g_apg
    y "Никто не заплачет, если она покончит с собой."
    $ style.say_dialogue = style.normal
    define audio.t9_apg = '<from ' + str(get_pos() * 2.07) + ' loop 3.172>bgm/9.ogg'
    stop music
    pause 0.5
    play sound 'sfx/stab.ogg'
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    pause 0.75
    stop sound
    play music t9_apg
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "Я должна сделать всё возможное, чтобы учесть мнение каждого и принять правильное для клуба решение."
    y 1t "Что насчёт тебя, [player]?"
    y "Что ты хотел найти в этом клубе?"
    "Юри повторила тот же вопрос, что и Моника."
    "Я решил, что уклончивый ответ лучше, чем ничего."
    mc "...Я думаю, что самое главное – чтобы все ладили друг с другом..."
    mc "...А для клуба – чтобы он мог предоставить то, что ты не сможешь получить больше нигде."
    mc "На мой взгляд, суть не в количестве участников, а в качестве каждого из них."
    mc "Именно это и делает литературный клуб особым местом."
    y 1u "Ясно..."
    y "Я полностью с тобой согласна."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Каждый участник реализует свои качества особым образом."
    y "Каждое изменение в составе клуба меняет и весь клуб в целом."
    y 1h "Я не считаю, что это обязательно плохо."
    y "Время от времени выходить из зоны комфорта..."
    y 1a "Так что если ты хочешь помочь Монике с фестивалем, то я тоже на твоей стороне."
    hide blood_eye2
    mc "Отлично."
    mc "Ну, может, завтра мы сможем все вместе поговорить с Нацуки..."
    "Юри кивнула."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Юри..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "А?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "М-м, я знаю, что вчера получилось довольно некрасиво..."
    m "Но я думаю, что ты заслуживаешь знать: я по-прежнему считаю тебя замечательным вице-президентом."
    m 1e "И прекрасной подругой."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "М-Моника..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "Я хочу выложиться на полную катушку, чтобы сделать этот клуб лучшим."
    m "Согласна?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...И я тоже."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Да..."
    m "Давайте сегодня разойдёмся по домам."
    m "О фестивале мы поговорим завтра."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Хорошо."
    y "Буду этого ждать."
    y 1a "Ну что, пойдём, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "М-м—"
    m 1p "Пожалуйста, не пойми неправильно, но..."
    m "Я и [player] поболтаем ещё немного перед уходом."
    m 1d "Просто чтобы узнать, что он думает о времени, которое проводит здесь, и всё такое..."
    m "Мне, как президенту, это важно."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Юри выглядела несколько обеспокоенной, но протестовать не стала."
    y 2t "Ладно."
    y 2s "Я доверяю твоему суждению, Моника."
    y "Увидимся завтра."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "До завтра~"
    show yuri zorder 1 at thide
    hide yuri
    "Моника помахала на прощание вышедшей из класса Юри."

    show monika 2a zorder 2 at t11
    m "Фух..."
    m 2e "В последнее время тут довольно беспокойно, согласен?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], я просто хотела удостовериться, что тебе нравится в клубе."
    m "Я ужасно не хочу видеть тебя несчастным."
    m 2m "Как президент, я чувствую себя ответственной за это..."
    stop music
    m 4e "И я искренне беспокоюсь за тебя... ты понимаешь?"
    m "Мне не нравится видеть, что у тебя проблемы из-за остальных девочек."
    m 4r "Учитывая вредный характер Нацуки и прочее..."
    m 4m "А Юри немного... ну, ты знаешь."
    m 5a "А-ха-ха..."
    m "Порой кажется, что мы с тобой здесь – единственные настоящие люди."
    m "Ты понимаешь, что я имею в виду?"
    m 1g "Но это странно, потому что за всё время, что ты здесь, мы вместе практически не бывали."
    m 1n "Ах... в смысле..."
    m "Чисто технически ты здесь, конечно, всего пару дней..."
    m 1l "Прости, я не хотела говорить ничего странного!"
    m 1e "Просто надеялась обсудить с тобой кое-что..."
    m "То, что, я знаю, понять сможешь только ты."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "Поэтому—\"{space=5000}{w=0.75}{nw}"
    m 1g "Стоп, ещё рано!\"{space=5000}{w=0.5}{nw}"
    m "Нет!\"{space=5000}{w=0.5}{nw}"
    m "Как это остановить?!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
