# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# В этом файле прописаны все переходы и анимации, используемые игрой.

# Придаёт спрайту корректный размер в указанной координате X.
transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

# Приближает персонажа, когда тот говорит.
transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

# Заставляет персонажа слегка опуститься вниз.
transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

# Заставляет персонажа подпрыгнуть.
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# Заставляет персонажа подпрыгнуть и оказаться в фокусе.
transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

# Заставляет персонажа слегка опуститься вниз и вернуться в исходное положение.
transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

# Заставляет персонажа качаться.
# Скорее всего, это остатки кода из ранней версии DDLC для сценки с Нацуки в кладовке.
transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

# Заставляет персонажа «влететь» (оказаться на сцене) слева.
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# Заставляет персонажа «влететь» (оказаться на сцене) справа.
transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# Убирает спрайт персонажа с экрана.
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20

# Убирает спрайт персонажа, перемещая его влево.
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

# Убирает спрайт персонажа, перемещая его вправо.
transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

# Эти трансформации расставляют спрайты в заданной позиции исходя из того,
# сколько сейчас персонажей на экране и какой индекс им присвоен.
#     Допустим, Моника должна встать между двумя другими девушками; мы «передаём» Монике `at t32`
transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)

# Эти трансформации заставляют персонажа появиться без анимации.
transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

# Эти трансформации приближают говорящего к экрану.
transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)

# Эти трансформации заставляют персонажа слегка опуститься вниз.
transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

# Эти трансформации заставляют персонажа подпрыгнуть.
transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

# Эти трансформации заставляют персонажа подпрыгнуть и оказаться в фокусе.
transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)

# Эти трансформации заставляют персонажа слегка опуститься вниз и вернуться в исходное положение.
transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)

# Эти трансформации заставляют персонажа «влететь» слева.
transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)

# Эти трансформации заставляют персонажа «влететь» справа.
transform r41:
    rightin(200)
transform r42:
    rightin(493)
transform r43:
    rightin(786)
transform r44:
    rightin(1080)
transform r31:
    rightin(240)
transform r32:
    rightin(640)
transform r33:
    rightin(1040)
transform r21:
    rightin(400)
transform r22:
    rightin(880)
transform r11:
    rightin(640)

# Сильно приближает лицо персонажа к экрану.
transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

# Придаёт эффект растворения элементам сценки, которые должны появиться/скрыться.
transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

# Использовалась в сценке с Нацуки в кладовке; заставляет Нацуки качаться, когда та паникует.
transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

# Воспроизводит качание каждую секунду.
transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

# Использовалась в сценке с Нацуки в кладовке; заставляет Нацуки влететь лицом в экран.
transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200

# Указывает эффект, используемый объявлением «dissolve» персонажами.
define dissolve = Dissolve(0.25)

# Закрепляет Dissolve(X) за эффектами для сценок и обычных сцен.
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

# Заставляет экран плавно перейти в чёрный, чтобы позже показать другую сцену.
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# Растворяет экран на какое-то время, а затем показывает следующую сцену.
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# Заставляет экран плавно «погрузиться во мрак», как будто игрок сам закрыл свои глаза.
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

# Возвращает происходящее на экране, как будто игрок открыл свои глаза.
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

# Мгновенно «погружает» экран «во мрак».
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

# Удаляет спрайт персонажа с экрана «стиранием» с левого края.
define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

# Удаляет происходящее на сцене «стиранием» с левого края, оставляя только «мрак», а затем показывает другую сцену.
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

# Удаляет спрайт персонажа с экрана «стиранием» с правого края.
define wiperight = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True)

# Удаляет происходящее на сцене «стиранием» с правого края, оставляя только «мрак», а затем показывает другую сцену.
define wiperight_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    True])

# Скорее всего, это остатки кода из ранней версии DDLC.
# Приостанавливает действие игры на четверть секунды.
define tpause = Pause(0.25)

# Это изображение с трансформациями выводит на экран анимированный белый шум.
image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

# Делает анимированный шум прозрачным на четверть.
transform noise_alpha:
    alpha 0.25

# Заставляет анимированный шум появиться на мгновение, а затем исчезнуть.
transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

# Добавляет виньетку для создания эффекта виньетирования.
image vignette:
    truecenter
    "images/bg/vignette.png"

# Заставляет виньетку плавно проявиться.
transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00

# Заставляет виньетку моргать.
transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

# Заставляет экранный слой моргать.
transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

# Накладывает эффект обратной перемотки, который можно было видеть во втором акте.
transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

# Эти трансформации накладывают эффект сердцебиения по воле случая во втором акте.
transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

# Эти трансформация и функция отвечают за анимацию движения глаз Юри во втором акте.
transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

# Накладывает спрайт персонажа поверх всего и заставляет его проявляться постепенно
# во втором акте.
transform malpha(a=1.00):
    i11
    alpha a
