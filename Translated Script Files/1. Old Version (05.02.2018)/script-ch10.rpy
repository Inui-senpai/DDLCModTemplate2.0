label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(10)
    "Мне навстречу бежала одна надоедливая девушка. Она изо всех сил махала руками, кажется совершенно не осознавая, что этим привлекает излишнее внимание окружающих."
    "Её зовут [s_name], она моя подруга детства, и мы живём по соседству."
    "Она из тех людей, с кем сегодня ты вряд ли стал бы дружить, но так уж вышло, что вы знаете друг друга уже невесть сколько."
    "Мы всегда ходили в школу вместе, но, когда перешли в старшие классы, она стала просыпать всё чаще, а мне стало надоедать постоянно дожидаться её."
    "Когда она так агрессивно меня преследует, иногда хочется просто убежать."
    "Однако я только вздохнул и стал ждать на перекрёстке, пока [s_name] меня не догнала."

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = '<from ' + str(startpos) + ' to ' + str(currentpos) + '>bgm/2.ogg'
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat

    jump ch20_from_ch10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
