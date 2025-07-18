# This file contains the Python code to handle Mod Template specific exceptions
# and checks for Ren'Py 8 at bootstrap.

## This import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import renpy  # type: ignore

"""renpy
python early:
"""


class NotRenPyEight(Exception):
    def __str__(self):
        return "This version of the mod template is designed for Ren'Py 8.\nEither build/run your mod on Ren'Py 8, or install the 'py2' mod template using Ren'Py 6/7."


class DDLCRPAsMissing(Exception):
    def __init__(self, archive: str):
        self.archive = archive

    def __str__(self):
        return (
            "'"
            + self.archive
            + ".rpa' was not found in the game folder. Check your DDLC installation for missing RPAs and try again."
        )


class IllegalModLocation(Exception):
    def __str__(self):
        return (
            "DDLC mods/mod projects cannot be run from this folder as it is a OneDrive or another cloud folder.\n"
            "Move your mod/mod project to another location and try again."
        )


if renpy.version_tuple < (8, 0, 0, 22062402):
    raise NotRenPyEight
