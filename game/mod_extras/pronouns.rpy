﻿## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

## pronoun_example.rpy
# В этом файле спрашивают предпочтительные местоимения игрока.

default pronoun_temp = ""

init python:
    # Азя, ты чёрт, можно же писать [he!c]... - прим. пер.
    def SetPronoun(type):
        global pronoun_temp
        if not pronoun_temp: return
        if type == "he":
            persistent.he = pronoun_temp.lower()
            he = pronoun_temp.lower()
            he_capital = pronoun_temp.lower().capitalize()
        elif type == "he's":
            persistent.hes = pronoun_temp.lower()
            hes = pronoun_temp.lower()
            hes_capital = pronoun_temp.lower().capitalize()
        elif type == "are":
            persistent.are = pronoun_temp.lower()
            are = pronoun_temp.lower()
            are_capital = pronoun_temp.lower().capitalize()
        elif type == "him":
            persistent.him = pronoun_temp.lower()
            him = pronoun_temp.lower()
            him_capital = pronoun_temp.lower().capitalize()
        pronoun_temp = ""

label pronoun_screen:
    $ renpy.call_screen("pronoun_input", message="Введите первое местоимение (Он/Она)", ok_action=Function(SetPronoun, type="he"))
    $ renpy.call_screen("pronoun_input", message="Введите второе местоимение (Его/Её)", ok_action=Function(SetPronoun, type="he's"), hes=True)
    $ renpy.call_screen("pronoun_input", message="Введите третье местоимение (Ему/Ей)", ok_action=Function(SetPronoun, type="him"))
    $ renpy.call_screen("pronoun_input", message="Введите четвёртое местоимение ((о) Нём/Ней)", ok_action=Function(SetPronoun, type="are"))
    return

screen pronoun_input(message, ok_action, hes=False):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5
            
            python:
                allowList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                # Бесполезно в русском языке. Оставлено для ввода английских местоимений - прим. пер.
                if hes:
                    allowList = allowList + "'"
                else:
                    allowList = allowList.replace("'", "")

            input default "" value VariableInputValue("pronoun_temp") length 12 allow allowList

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("ОК") action [ok_action, Return(0)]