# Contents of the `core/py` folder

## Folders
- **\_\_pycache\_\_**: Contains the compiled Python files for the code used in the core features of DDLC and the mod template. This should normally not appear in your mod nor in packaged mod templates, but if it exists, ignore it.

## Files
- **README.md**: This file, which provides an overview of the contents of the `py` folder.
- **\_\_init\_\_.py**: An empty file used for testing purposes.
- **[0core_ren.py](./0core_ren.py)**: Contains the singleton code to prevent multiple instances of DDLC from running on the user's PC.
- **[core_ren.py](./core_ren.py)**: Contains the major code for all of DDLC and the Mod Template + Features.
- **[splash_ren.py](./splash_ren.py)**: Handles the checks for DDLC RPA files and Anti-Cloud folder checks.