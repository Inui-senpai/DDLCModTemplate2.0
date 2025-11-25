# Contents of the `core` folder
> [!DANGER]
> The following files and folders in the `core` folder are crucial to DDLC and/or the mod template itself. **DO NOT** delete or edit these files unless you know what you are doing except for *[credits.rpy](./credits.rpy)*.

## Folders

- **[py](./py)**: Contains the Python code for the core features of DDLC and the mod template.
- **\_\_pycache\_\_**: Contains the compiled Python files for the code used in the core features of DDLC and the mod template. This should normally not appear in your mod nor in packaged mod templates, but if it exists, ignore it.

## Files
- **[0imports.rpy](./0imports.rpy)**: This file imports certain python modules after bootstrap but before game boot for DDLC and template features.
- **[credits.rpy](./credits.rpy)**: This file defines the code for the credits screen that plays at the end of Act Four.

## Moved Files/Contents
- **[0imports.rpy](./py/0imports_ren.py)**: The `python early` imports were moved from the `game/core` folder to the `game/core/py` folder for organizational purposes. Contains the imports for the core features of DDLC and the mod template to import at bootstrap.
- **[renpy_patches.rpy](./py/renpy_patches_ren.py)**: This file was moved from the `game/core` folder to the `game/core/py` folder as this is purely a Ren'Py file with Python patches. Contains several patches in order for DDLC to run properly on Ren'Py 8.
- **[exceptions.rpy](./py/template_checks_ren.py)** and **lockdown_check.rpy** - These files were combined into *template_checks_ren.py* file as they were purely Ren'Py files with Python code and exceptions. Contains custom exceptions and checks for the Mod Template to look for before DDLc boots up.
