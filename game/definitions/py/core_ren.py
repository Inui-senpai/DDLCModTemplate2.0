import os
import subprocess
import renpy  # type: ignore

"""renpy
init -3 python:
"""
# These are used so that IDEs don't report errors and Python code can access Ren'Py's store and persistent.
persistent = renpy.store.persistent
store = renpy.store

# The default splash message for the game that players will see when launching your mod.
splash_message_default = (
    "This mod is an unofficial fan game that is unaffiliated with Team Salvato."
)

# Stores multiple splash messages that can be used in the game.
splash_messages = [
    ":o",
    "Bronya... :o",
]


## DDLC Functions


def get_characters_folder():
    """
    Returns the path to the characters folder.

    :return: The path to the characters folder or None if it cannot be determined.
    :rtype: str | None
    """
    characters_folder = None
    if renpy.android:
        android_public_directory = os.environ.get("ANDROID_PUBLIC_DIRECTORY")
        if android_public_directory:
            characters_folder = os.path.join(android_public_directory, "characters")
    else:
        characters_folder = os.path.join(renpy.config.basedir, "characters")

    return characters_folder


def restore_character(characters: list[str]):
    """
    Restores the specified characters to the 'characters' folder.

    :param characters: A list of character names to restore.
    :type characters: list[str]
    """
    characters_folder = get_characters_folder()
    if characters_folder:
        for character in characters:
            character_file_path = os.path.join(characters_folder, f"{character}.chr")
            try:
                renpy.open_file(character_file_path)
            except OSError:
                open(character_file_path, "wb").write(
                    renpy.open_file(os.path.join("chrs", f"{character}.chr")).read()
                )


def restore_characters():
    """
    Restores all characters depending on the current playthrough.
    """
    if renpy.store.persistent.playthrough == 0:
        restore_character(["monika", "natsuki", "sayori", "yuri"])
    elif (
        renpy.store.persistent.playthrough == 1
        or renpy.store.persistent.playthrough == 2
    ):
        restore_character(["monika", "natsuki", "yuri"])
    elif renpy.store.persistent.playthrough == 3:
        restore_character(["monika"])
    else:
        restore_character(["natsuki", "sayori", "yuri"])


def delete_character(name: str):
    """
    Deletes a character file from the 'characters' folder.

    :param name: The name of the character to delete.
    :type name: str
    """
    characters_folder = get_characters_folder()
    if characters_folder:
        try:
            os.remove(os.path.join(characters_folder, f"{name}.chr"))
        except OSError:
            pass  # Ignore if the file does not exist


def initialize_characters_folder():
    """
    Initializes the characters folder by creating it if it does not exist.

    :return: The path to the characters folder.
    :rtype: str
    """
    characters_folder = get_characters_folder()
    if characters_folder and not os.path.exists(characters_folder):
        os.makedirs(characters_folder)

    restore_characters()


def delete_all_saves():
    """
    Deletes all save files in the game.
    """
    for savegame in renpy.list_saved_games(fast=True):
        renpy.unlink_save(savegame)


def get_music_pos(channel: str = "music"):
    """
    Returns the current position of the specified music channel.

    :param channel: The name of the music channel.
    :type channel: str

    :return: The current position of the music channel or 0 if not playing.
    :rtype: int
    """
    pos = renpy.music.get_pos(channel)
    if pos is not None:
        return pos
    return 0


def pause(time=None):
    """
    Pauses the game for a specified amount of time or indefinitely.

    :param time: The time to pause in seconds. If None, pauses indefinitely.
    """
    global _windows_hidden

    if not time:
        _windows_hidden = True
        renpy.ui.saybehavior(afm=" ")
        renpy.ui.interact(mouse="pause", type="pause", roll_forward=None)
        _windows_hidden = False
        return
    if time <= 0:
        return
    _windows_hidden = True
    renpy.pause(time)
    _windows_hidden = False


## OS Functions


def get_process_list():
    """
    Retrieves the list of currently running processes on the system.

    :return: A list of process names.
    :rtype: set[str]
    """
    process_list: set[str] = set()
    if renpy.windows:
        try:
            subprocess_list = subprocess.run(
                "powershell (Get-Process).ProcessName",
                shell=True,
                capture_output=True,
                text=True,
            ).stdout.splitlines()

            for _, process in enumerate(subprocess_list):
                process_list.add(process.strip().lower() + ".exe")
        except subprocess.CalledProcessError:
            pass
    else:
        try:
            subprocess_list = subprocess.run(
                "ps -eo comm=", shell=True, capture_output=True, text=True
            ).stdout.splitlines()

            for process in subprocess_list:
                process = process.strip().split()[
                    0
                ]  # Get the first part of the command
                if process:  # Ensure it's not empty
                    process_list.add(process.lower())
        except subprocess.CalledProcessError:
            pass

    return process_list


def process_check(stream_list: list[str]):
    """
    Checks whether the given application stream list is running on the current system.

    :param stream_list: A list of application streams to check.

    :type stream_list: list[str]

    :return bool: True if the application is running, False otherwise.
    """
    if not renpy.windows:
        # Adjust for non-Windows systems
        for index, process in enumerate(stream_list):
            stream_list[index] = process.replace(".exe", "")

    process_list = get_process_list()
    for process in stream_list:
        for running_process in process_list:
            # Check if the process name matches exactly or is a prefix of the running process (followed by '/') [Linux/macOS]
            if running_process == process or running_process.startswith(process + "/"):
                return True
    return False


def get_user_account_name():
    """
    Retrieves the current user's account name.

    :return: The username of the current user or None if it cannot be determined.
    :rtype: str | None
    """
    if renpy.windows:
        # `whoami` and split name (DOMAIN\Username -> Username)
        return (
            subprocess.run("whoami", shell=True, capture_output=True, text=True)
            .stdout.strip()
            .split("\\")[-1]
            or None
        )
    else:
        return (
            subprocess.run(
                "id -un", shell=True, capture_output=True, text=True
            ).stdout.strip()
            or None
        )


currentuser = get_user_account_name()

## Template Functions


## TODO: Adjust to maybe Transform and MatrixColor
def recolorize(
    path: str, blackCol: str = "#ffbde1", whiteCol: str = "#ffe6f4", contr: float = 1.29
):
    """
    Recolorizes the image at the given path with the specified colors and contrast.

    :param path: The path to the image file.
    :param blackCol: The color to use for black areas.
    :param whiteCol: The color to use for white areas.
    :param contr: The contrast level to apply.

    :type path: str
    :type blackCol: str
    :type whiteCol: str
    :type contr: float

    :return: The recolorized image.
    """
    return renpy.im.MatrixColor(
        renpy.im.MatrixColor(
            renpy.im.MatrixColor(
                path, renpy.im.matrix.desaturate() * renpy.im.matrix.contrast(contr)
            ),
            renpy.im.matrix.colorize("#00f", "#fff") * renpy.im.matrix.saturation(120),
        ),
        renpy.im.matrix.desaturate() * renpy.im.matrix.colorize(blackCol, whiteCol),
    )


### Dynamic Super Positioning
def dsp(original_position_value: int | float) -> int:
    """
    Dynamically adjusts the position value of an element based on the
    original game's screen size (1280x720) against the set screen size.

    This assumes that the original position value is set for a 1280x720 resolution.
    """
    valueIsInt = isinstance(original_position_value, int)
    scale_position_by = renpy.config.screen_width / 1280.0
    if valueIsInt:
        return int(original_position_value * scale_position_by)
    return original_position_value * scale_position_by


### Dynamic Super Resolution
def dsr(image_path: str):
    """
    Dynamically adjusts the size of the image based on the original game's
    screen size (1280x720) against the set screen size.

    (It is recommended to use high-res images and use DSP than DSR.)
    """
    image_bounds = renpy.image_size(image_path)
    return renpy.Transform(
        image_path, size=(dsp(image_bounds[0]), dsp(image_bounds[1]))
    )


## Initialize Core Code

# Setup mapping for the game menu and hide windows.
renpy.config.keymap["game_menu"].remove("mouseup_3")
renpy.config.keymap["hide_windows"].append("mouseup_3")
renpy.config.keymap["self_voicing"] = []
renpy.config.keymap["clipboard_voicing"] = []
renpy.config.keymap["toggle_skip"] = []

# Register the music channel for the poem game.
renpy.music.register_channel("music_poem", mixer="music", tight=True)

# If using 'More Android Gestures', uncomment the following lines to initialize the gesture mapping.
# if renpy.android:
#     # Initialize the gesture mapping for Android devices.
#     renpy.config.keymap["rollback"] = []
#     renpy.config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]

renpy.pure(dsp)
