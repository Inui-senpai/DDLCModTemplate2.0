# В этом файле прописан код, который удаляет устаревший/перенесённый функционал из DDLC или мод-шаблона.

import os
import renpy  # type: ignore

"""renpy
python early:
"""

RENPY_PYTHON_PACKAGES = "python-packages"


def cleanup_deprecated_features():
    """
    Удаляет устаревший и перенесённый функционал.
    """

    # Удаляет старую реализацию singleton, если она есть
    python_packages_dir = os.path.join(renpy.config.gamedir, RENPY_PYTHON_PACKAGES)
    if os.path.exists(os.path.join(python_packages_dir, "singleton.py")):
        try:
            os.remove(os.path.join(python_packages_dir, "singleton.py"))
        except OSError:
            pass


cleanup_deprecated_features()
