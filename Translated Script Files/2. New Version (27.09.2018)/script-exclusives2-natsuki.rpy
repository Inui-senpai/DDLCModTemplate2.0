

init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid('#000'), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid('#000'), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid('#000'), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid('#000'), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid('#000'), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "Ух!.."
    "Из кладовки доносится сердитый вздох Нацуки."
    "Кажется, она чем-то раздражена."
    "Я подхожу к ней, намереваясь помочь."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "Ты что-то потеряла?"
    $ style.say_dialogue = style.edited
    if persistent.allow_slang:
        n 4x "ёбанная моникамммммммммммммммммммммммммммммммммммммммммммммм"
    else:
        n 4x "грёбанная моникамммммммммммммммммммммммммммммммммммммммммммммм"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Чтоб тебя, Моника..."
    n "Она никогда не возвращает мои вещи на место!"
    n "Какой смысл поддерживать здесь порядок, если кто-то постоянно устраивает бардак?!"
    "Нацуки двигает по полке стопки книг и коробки."
    mc "Манга..."
    n 2c "Ты ведь читаешь мангу, да?"
    mc "Э..."
    mc "...Иногда..."
    "Чтение манги – то, в чём не стоит признаваться человеку до тех пор, пока не выяснишь, как он к этому относится."
    mc "...Но как ты узнала?"
    n 2k "Ты как-то об этом упомянул, а я услышала."
    n "Кроме того, это у тебя на лице написано."
    "Что бы это значило?.."
    mc "Ясно..."
    "На краю одной из полок, по соседству с книгами разных жанров, приютился одинокий томик манги."
    "Он бросается в глаза, и я вытаскиваю его оттуда."
    n 1b "{i}Вот{/i} ты где!"
    "Нацуки выхватывает его из моей руки."
    "После чего поворачивается к коробке с мангой и впихивает томик в неё."
    n 4d "Ах, так гораздо лучше!"
    n "Зияющая дыра в полном издании – это, наверное, самое раздражающее зрелище на свете."
    mc "Мне знакомо это чувство..."
    "Я приглядываюсь к коллекции, которой она так любуется."
    mc "«Ванильные девочки»?.."
    "Никогда ничего не слышал об этой манге."
    "Это может означать, что она либо не соответствует моей возрастной группе, либо она просто ужасна."
    n 5g "Если ты собираешься меня осуждать, можешь делать это вон за той дверью."
    "Она показывает пальцем на дверь класса."
    mc "Эй, я никого осуждать не собирался!.."
    mc "Я ведь и слова не сказал."
    n 5c "Я поняла это по твоей физиономии."
    $ style.say_dialogue = style.normal
    n "Но я скажу тебе одно, [player]."
    n 4l "Считай это уроком от литературного клуба:{nw}"
    $ _history_list[-1].what = "Считай это уроком от литературного клуба: не суди книгу по обложке!"
    $ style.say_dialogue = style.edited
    n "не суди книггггггггггггггггггггггг ггггг гг{space=20}г{space=40}г{space=120}г{space=160}г{space=200}у"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "А вообще..."
    "Нацуки вытаскивает из коробки первый томик «Ванильных девочек»."
    n "Я сейчас покажу тебе почему!"
    "Она суёт книгу прямо мне в руки."
    mc "Э..."
    "Я смотрю на обложку."
    "На ней изображены четыре девушки в ярких одеждах и характерных девчачьих позах."
    "Выглядит... чрезвычайно «моэшно»."
    n 4b "Не стой как истукан!"
    mc "Уа..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Нацуки хватает меня за руку и оттаскивает от кладовки."
    "Затем подходит к окну и садится спиной к стене."
    "Она похлопывает рукой рядом, приглашая меня к ней присоединиться."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "На стульях разве не удобнее?.."
    "Я сажусь рядом с Нацуки."
    n 2k "Стулья не катят."
    n "Так мы не сможем читать вместе."
    mc "Э? Почему это?"
    mc "А... Так будет проще быть ближе друг к другу..."
    n 2o "...!"
    n 5r "Н-не говори об этом так!"
    n "Ты заставляешь меня чувствовать себя странно!"
    "Нацуки скрещивает руки и немного от меня отодвигается."
    mc "Извини..."
    show natsuki 5g
    "Хотя я и не собирался садиться к ней так близко, однако..."
    "Не могу сказать, что в этом есть что-то плохое."
    "Я открываю книгу."
    "Проходит всего несколько секунд, и Нацуки снова пододвигается ко мне, думая, что я не замечу."
    "Когда она заглядывает мне через плечо, я резко ощущаю её желание начать читать, желание куда более сильное, чем моё собственное."
    n 1k "Эх, сколько времени прошло с тех пор, как я читала первый том..."
    mc "А?"
    mc "Ты не пролистываешь порой уже прочитанные тома?"
    n 2k "Да нет."
    n "Разве что иногда, после того как прочту всё до конца."
    n 2c "Эй, не отвлекайся!"
    mc "Эх..."
    "Так как в сюжете ничего интересного не происходит, я могу одновременно читать и поддерживать диалог."
    "Похоже, манга повествует о группе друзей, учащихся в старшей школе."
    "Типичная повседневность."
    "Я в некотором роде уже вырос из подобного, потому что обилие картинок всё же недостаточно для компенсации недостатков сюжета."
    $ persistent.clear[0] = True
    $ renpy.save_persistent()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...Тебе не скучно?"
    n "Совсем нет!"
    mc "Хотя ты просто смотришь, как я читаю?"
    n "Ну..."
    n "Мне... этого достаточно."
    mc "Как скажешь..."
    mc "...Полагаю, это весело – делиться с кем-то любимыми вещами."
    mc "Я всегда немного волнуюсь, когда убеждаю кого-нибудь из своих друзей почитать понравившуюся мне мангу."
    mc "Понимаешь, что я имею в виду?"
    n "...?"
    mc "Хм?"
    mc "Нет?"
    show n_cg1_exp2 at cgfade
    n "М-м-м..."
    n "Это не..."
    n "Мне-то откуда знать."
    mc "...Что ты хочешь этим сказать?"
    mc "Разве ты не делишься мангой со своими друзьями?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Не мог бы ты не сыпать соль на рану?"
    n "Блин..."
    mc "Ой... Прости..."
    n "Хмф."
    n "Будто мои друзья согласились бы это прочитать..."
    n "Они считают, что манга – для детей."
    n "Стоит мне только завести об этом речь, как они такие..."
    n "«А? Ты что, ещё не выросла из всего этого?»"
    if persistent.allow_joke:
        n "Так и хочется врезать им ногой с разворота..."
    else:
        n "Так и хочется съездить им по физиономии..."
    mc "Эх, я знаю таких людей..."
    mc "Честно говоря, довольно сложно найти друзей, которые не осуждали бы тебя за это и уж тем более сами этим увлекались."
    mc "В некотором роде я неудачник, поэтому со временем обзавёлся такими же друзьями-неудачниками."
    mc "Но, видимо, для такой, как ты, всё гораздо сложнее."
    hide n_cg1_exp3
    n "Хм..."
    n "Да, пожалуй ты прав."
    "{i}...Постой, в каком именно месте???{/i}"
    $ style.say_dialogue = style.normal
    n "Я ведь даже не могу хранить мангу у себя дома..."

    $ style.say_dialogue = style.edited
    if persistent.allow_slang:
        if (not persistent.allow_joke or renpy.random.randint(0, 1) == 0):
            n "Мой отец пропишет мне знатных пиздюлей, если найдёт её."
        else:
            n "Мой отец выебет меня и высушит, если найдёт её."
    else:
        n "Мой отец изобьёт меня до полусмерти, если найдёт её."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Страшно представить, что сделает мой отец, если найдёт её."
    n "Но хотя бы в клубе можно спокойно её читать."
    show n_cg1_exp3 at cgfade
    n "Разве что Моника иногда гундит..."
    n "Уф! Всё против меня!"
    mc "Да, но в итоге ты добилась своего, верно?"
    mc "Вот, я читаю её с тобой."
    n "Увы, это не решает все мои проблемы."
    mc "Возможно..."
    mc "Но тебе ведь сейчас весело, да?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "—"
    n "..."
    n "...Думаешь?"
    mc "А-ха-ха."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Боже, хватит!"
    n "Ты будешь уже читать или как?"
    mc "Да, да..."
    "Я переворачиваю страницу."
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "Время идёт."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "Нацуки подозрительно хранит молчание."
    "Я смотрю на неё."
    hide black with dissolve_cg
    "Похоже, её клонит в сон."
    mc "Эй, Нацуки..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "Д-да?.."
    "Внезапно Нацуки заваливается на меня."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "Эй..."
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = '<from ' + str(currentpos) + ' loop 10.893>bgm/6g.ogg'
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "Ох ты ж..."
    m 1d "Нацуки, ты в порядке?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "..."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Вот..."
    show monika zorder 2 at t21
    "Моника запускает руку в портфель и вытаскивает оттуда протеиновый батончик."
    "Она бросает его Нацуки."
    "В глазах Нацуки снова загорается огонь."
    "Она хватает батончик с пола и молниеносно срывает обёртку."
    show natsuki zorder 3 at f22
    n 1s "Я говорила тебе не давать ом-ном-ном..."
    show natsuki zorder 2 at t22
    "Не успевает она договорить, как уже жуёт его."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "Не беспокойся, [player]."
    m "С ней всё в порядке."
    m "Время от времени такое случается."
    m 1a "Поэтому у меня в портфеле всегда есть что-нибудь съестное."
    m 5a "А теперь..."
    m "Почему бы нам не почитать друг другу стихи?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
