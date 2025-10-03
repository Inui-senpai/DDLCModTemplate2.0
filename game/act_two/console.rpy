# This file contains the Ren'Py code for Monika's console in DDLC.

# The logic for the console has been changed drastically compared to the original
# game to allow for better management of console inputs and outputs and display.
# It separates the Python logic from the display code, which is now in `py/console_ren.py`.

# To show the console, just do `$ console.show_screen()` or `show screen console_screen(console)`.

# For the Python code, see `console_ren.py` in the `py` directory.

init -1:
    default console = Console(console_delay=0.5, console_cps=30, max_log_history=5)

screen console_screen(console, input_text=None, output_text=None):
    """
    This screen shows the console in-game.
    """

    style_prefix "console_screen"

    default finish_actions = [SetScreenVariable("in_progress", False), Return()]

    # String of input to show.
    # It is put outside of the new_input variable so it doesn't
    # start over and over.
    default new_input_code = "_"

    # Changes to True once a new code_text 
    default in_progress = False

    # If text is not in the process of showing.
    if not in_progress:

        $ new_input_code = "_"

        if input_text:
            $ in_progress = True
            $ new_input_code = input_text

    # New code is showing.
    if in_progress:

        timer ( float(len(renpy.filter_text_tags(new_input_code, deny = []))) / float(console.console_cps) + console.console_delay ) action finish_actions

    frame:

        vbox:
            hbox:
                text ">" xpos 5 ypos 10

                text new_input_code xpos 15 ypos 10:
                    slow_cps 30
                    xmaximum 460

            vbox:
                xpos 26 ypos 30 
                spacing 5

                for output in console.console_history.values():
                    text output

style console_screen_frame:
    background Frame(Transform(Solid("#333"), alpha=0.75))
    xsize 480
    ysize 180

# This style declares the text appearance of the text shown in the console in-game.
style console_screen_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []

# This label clears all console history and commands from the console in-game.
# Decided to keep this for now as it just pauses stuff.
# This assumes the default console is used from the above init python import.
label updateconsole_clearall(text="", history=""):
    if config.developer:
        $ renpy.notify("This label call is deprecated. Use `console.clear_history()` instead.")
    $ console.clear_history()
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return