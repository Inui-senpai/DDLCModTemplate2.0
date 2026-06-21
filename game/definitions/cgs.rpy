# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.

# В этом файле прописаны сценки из оригинальной игры, такие как Юри
# с шоколадкой во рту и Нацуки с коробкой манги в руках.

## Юри с шоколадкой во рту [Тропа Юри 2]
# Это задний план сценки (стена класса).
image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
    6.0
    "images/cg/y_cg2_bg2.png" with Dissolve(1)
    2
    "images/cg/y_cg2_bg1.png" with Dissolve(1)
    1
    repeat

# Это «тело» Юри, которая читает книгу и держит во рту шоколадку.
image y_cg2_base:
    "images/cg/y_cg2_base.png"

# Это изображение убирает шоколадку с «тела» Юри с открытым ртом.
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"
    on hide:
        linear 0.5 alpha 0

# Это изображение с трансформациями добавляет детали сценке, чтобы та «сверкала».
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

# Шокированное выражение лица Юри.
image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Смущённое выражение лица Юри.
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Эти изображения с трансформациями добавляют летающие частицы пыли,
# чтобы сценка «сверкала».
image y_cg2_dust1:
    "images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust2:
    "images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust3:
    "images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

## Нацуки, читающая мангу [Тропа Нацуки 1]
# Это задний план сценки (стена класса).
image n_cg1_bg:
    "images/cg/n_cg1_bg.png"

# Это «тело» Нацуки, которая наблюдает за читающим мангу игроком.
image n_cg1_base:
    "images/cg/n_cg1_base.png"

# Радостное выражение лица Нацуки.
image n_cg1_exp1:
    "images/cg/n_cg1_exp1.png"

# Обиженное выражение лица Нацуки.
image n_cg1_exp2:
    "images/cg/n_cg1_exp2.png"

# Смущённое выражение лица Нацуки.
image n_cg1_exp3:
    "images/cg/n_cg1_exp3.png"

# Спящее выражение лица Нацуки.
image n_cg1_exp4:
    "images/cg/n_cg1_exp4.png"

# Полусонное выражение лица Нацуки.
image n_cg1_exp5:
    "images/cg/n_cg1_exp5.png"

# Это изображение придаёт Нацуки искажённый вид во время прохождения второго акта.
image n_cg1b = Composite((1280,720), (0,0), "images/cg/n_cg1b.png", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

# Эти изображения с трансформациями закрывают глаза Нацуки чёрными квадратами во время прохождения второго акта.
image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    xysize (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    xysize (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    xysize (30, 20)

## Нацуки в кладовке [Тропа Нацуки 2]
# Это задний план сценки (внутренняя часть кладовки).
image n_cg2_bg:
    "images/cg/n_cg2_bg.png"

# Это «тело» Нацуки, которая переставляет свою мангу на другую полку.
image n_cg2_base:
    "images/cg/n_cg2_base.png"

# Обеспокоенное выражение лица Нацуки.
image n_cg2_exp1:
    "images/cg/n_cg2_exp1.png"

# Озлобленное выражение лица Нацуки.
image n_cg2_exp2:
    "images/cg/n_cg2_exp2.png"

## Инцидент на кухне с Нацуки [Тропа Нацуки 3]
# Это задний план сценки (пол кухни).
image n_cg3_base:
    "images/cg/n_cg3_base.png"

# Глазурь на пальце Нацуки.
image n_cg3_cake:
    "images/cg/n_cg3_cake.png"

# Радостное выражение лица Нацуки.
image n_cg3_exp1:
    "images/cg/n_cg3_exp1.png"

# Смущённое выражение лица Нацуки.
image n_cg3_exp2:
    "images/cg/n_cg3_exp2.png"

## Совместное чтение с Юри [Тропа Юри 1]
# Это задний план сценки (класс) и «тело» Юри, которая сидит за партой.
image y_cg1_base:
    "images/cg/y_cg1_base.png"

# Юри смотрит на игрока краем глаза.
image y_cg1_exp1:
    "images/cg/y_cg1_exp1.png"

# Радостное выражение лица Юри.
image y_cg1_exp2:
    "images/cg/y_cg1_exp2.png"

# Паникующее выражение лица (как у яндере) Юри.
image y_cg1_exp3:
    "images/cg/y_cg1_exp3.png"

## Инцидент с красками с Юри [Тропа Юри 3]
# Это задний план сценки (комната игрока) и «тело» Юри.
image y_cg3_base:
    "images/cg/y_cg3_base.png"

# Спокойное выражение лица Юри с закрытыми глазами.
image y_cg3_exp1:
    "images/cg/y_cg3_exp1.png"

## Сайори и её пиджак [Тропа Сайори 1]
# Это задний план сценки (класс) и «тело» Сайори.
image s_cg1:
    "images/cg/s_cg1.png"

## Инцидент с Сайори, стукнувшейся головой [Тропа Сайори 2]
# Это задний план сценки (кладовка) и «тело» Сайори.
image s_cg2_base1:
    "images/cg/s_cg2_base1.png"

# Альтернативный вариант сценки, где Сайори держит яблочный сок в руке.
image s_cg2_base2:
    "images/cg/s_cg2_base2.png"

# Сайори морщится от боли.
image s_cg2_exp1:
    "images/cg/s_cg2_exp1.png"

# Расстроенное выражение лица Сайори.
image s_cg2_exp2:
    "images/cg/s_cg2_exp2.png"
    
# Сайори сидит с закрытыми глазами.
image s_cg2_exp3:
    "images/cg/s_cg2_exp3.png"

## Игрок обнимает Сайори [День 4]
# Это задний план сценки (перед домом игрока) и «тело» Сайори.
image s_cg3:
    "images/cg/s_cg3.png"

## Самоубийство Сайори
# Это задний план сценки (комната Сайори).
image s_kill_bg:
    subpixel True
    "images/cg/s_kill_bg.png"

# Спрайт повесившейся Сайори во весь рост.
image s_kill:
    subpixel True
    "images/cg/s_kill.png"

# Искажённый вариант комнаты Сайори.
image s_kill_bg2:
    subpixel True
    "images/cg/s_kill_bg2.png"

# Искажённый спрайт повесившейся Сайори.
image s_kill2:
    subpixel True
    "images/cg/s_kill2.png"

## Самоубийство Юри в классе
# Это изображение с условием показывает разные варианты сценки с Юри, нанёсшей
# самой себе ножевые ранения, в зависимости от того, сколько времени прошло в игре.
image y_kill = ConditionSwitch(
    "persistent.yuri_kill >= 1380", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 1180", "images/cg/y_kill/3c.png",
    "persistent.yuri_kill >= 1120", "images/cg/y_kill/3b.png",
    "persistent.yuri_kill >= 920", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 720", "images/cg/y_kill/2c.png",
    "persistent.yuri_kill >= 660", "images/cg/y_kill/2b.png",
    "persistent.yuri_kill >= 460", "images/cg/y_kill/2a.png",
    "persistent.yuri_kill >= 260", "images/cg/y_kill/1c.png",
    "persistent.yuri_kill >= 200", "images/cg/y_kill/1b.png",
    "True", "images/cg/y_kill/1a.png",
    )

# Эта трансформация запускает анимацию фона во время показа сценки
# самоубийства Сайори.
transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

# Эта трансформация запускает анимацию спрайта повесившейся Сайори.
transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

# Это изображение с трансформацией приближает камеру к определённому участку фона.
image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

# Эта трансформация заставляет изображение или спрайт трястись, как будто у игрока головокружение.
transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

# Это изображение с трансформацией приближает камеру к спрайту повесившейся Сайори.
image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

# Это изображение с трансформацией приближает камеру к определённому участку искажённого фона.
image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

# Это изображение с трансформацией приближает камеру к искажённому спрайту повесившейся Сайори.
image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
