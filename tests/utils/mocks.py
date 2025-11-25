# This file is part of the tests for the Mod Template
# It contains mock implementations of Ren'Py specific classes and functions
# to allow for testing without the need for a full Ren'Py environment.

import random
import sys

_fake_store_dicts = {}
_fake_store_modules = {}
_fake_initialized_store_dicts = set()


class _FakeRenpyPersistent(object):
    """
    A fake persistent store to mimic Ren'Py's persistent store.
    This is used to simulate the persistent data that Ren'Py would normally handle i.e. persistent.X = <value>
    """

    def __setstate__(self, data):
        """
        Mimics the behavior of setting state in a Ren'Py persistent store.

        :param data: The data to set in the persistent store.
        """
        self.__dict__.update(data)

    def __getstate__(self) -> object:
        """
        Mimics the behavior of getting state in a Ren'Py persistent store.

        :return object: The current state of the persistent store.
        """
        return self.__dict__

    def __getattr__(self, attr):
        """
        Mimics the behavior of getting attributes in a Ren'Py persistent store.

        :param attr: The attribute to get.
        :return any | None: The value of the attribute or None if it doesn't exist.
        """
        if attr.startswith("__") and attr.endswith("__"):
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{attr}'"
            )

        return None

    def _hasattr(self, field_name):
        """
        Mimics the behavior of checking if an attribute exists in a Ren'Py persistent store.

        :param field_name: The name of the field to check.
        :return bool: True if the field exists, False otherwise.
        """
        return field_name in self.__dict__


class _FakeRenpyStoreModule(object):
    def __reduce__(self):
        """
        Mimics the behavior of reducing a Ren'Py store module for serialization.
        This is used to ensure that the Ren'Py store module can be serialized correctly.

        :return: A tuple that can be used to reconstruct the module.
        """
        return (_fake_get_store_module, (self.__name__,))  # type: ignore

    def __init__(self, d):
        """
        Initializes the fake Ren'Py store module with a dictionary.

        :param d: The dictionary to use as the store module's namespace.
        """
        object.__setattr__(self, "__dict__", d)

    def __setattr__(self, key, value):
        """
        Mimics the behavior of setting attributes in a Ren'Py store.

        :param key: The name of the attribute to set.
        :param value: The value to set for the attribute.
        """
        self.__dict__[key] = value

    def __delattr__(self, key):
        """
        Mimics the behavior of deleting attributes in a Ren'Py store.

        :param key: The name of the attribute to delete.
        :raises AttributeError: If the attribute does not exist.
        """
        if key in self.__dict__:
            del self.__dict__[key]

        raise AttributeError(f"'{self.__name__}' object has no attribute '{key}'")  # type: ignore


class _FakeRenpyStoreDict(dict):
    """
    A fake Ren'Py store dictionary to mimic Ren'Py's store behavior.
    This is used to simulate the Ren'Py store dictionary that holds game state.
    """

    def __init__(self):
        self.old = {}


class _FakeRenpyRandom:
    """
    A fake random module to mimic Ren'Py's random behavior.
    This is used to simulate random choices and integer generation in tests.
    """

    def choice(self, seq):
        return random.choice(seq)

    def randint(self, a, b):
        return random.randint(a, b)

    def random(self):
        return random.random()


class _FakeRenpyEasy:
    """
    A fake easy module to mimic Ren'Py's easy behavior.
    """

    @staticmethod
    def displayable_or_none(displayable):
        """
        Mock implementation of renpy.easy.displayable_or_none.

        :param displayable: The displayable to check.
        :return: The displayable if valid, None otherwise.
        """
        if displayable is None:
            return None
        # Return a simple mock object instead of None
        return _FakeRenpyDisplayable(displayable)


class _FakeRenpyDisplayable:
    """
    A fake displayable to mimic Ren'Py's displayable behavior.
    """

    def __init__(self, path):
        self.path = path


class _FakeRenpyNull:
    """
    A fake Null displayable to mimic Ren'Py's Null behavior.
    """

    def __init__(self):
        self.path = "null"


class _FakeRenpyTextTextText:
    """
    A fake Ren'Py Text class to mimic the behavior of renpy.text.text.Text.
    This is used to simulate text display in tests.
    """

    def __init__(self, text, style=None, **kwargs):
        self._text = text
        self.style = style
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __repr__(self):
        return f"<FakeRenpyTextText: {self.text}>"


def _fake_renpy_(s):
    """
    A fake Ren'Py function to mimic the behavior of `renpy._()` for translations.
    This is used to simulate the translation of text in tests.

    :param s: The string to translate.
    :return: The translated string (in this case, just the original string).
    """
    return s


def _fake_renpy_window_hide():
    """
    Mock method to simulate hiding the window.
    """
    print("Window hidden.")
    pass


def _fake_get_store_module(name):
    """
    Retrieves a fake Ren'Py store module by name.

    :param name: The name of the store module to retrieve.

    :return module: The fake Ren'Py store module.
    :raises ImportError: If the store module does not exist.
    """
    return sys.modules[name]


def _fake_create_store(name):
    """
    Creates a fake Ren'Py store module.

    :param name: The name of the store module to create.
    """
    parent, _, var = name.rpartition(".")

    if parent:
        _fake_create_store(parent)

    name = str(name)

    if name in _fake_initialized_store_dicts:
        return

    _fake_initialized_store_dicts.add(name)

    # Create the dict.
    d = _fake_store_dicts.setdefault(name, _FakeRenpyStoreDict())

    pyname = name
    d.update(__name__=pyname, __package__=pyname)
    eval("1", d)

    if name in _fake_store_modules:
        sys.modules[pyname] = _fake_store_modules[name]
    else:
        _fake_store_modules[name] = sys.modules[pyname] = _FakeRenpyStoreModule(d)  # type: ignore

    if parent:
        _fake_store_dicts[parent][var] = sys.modules[pyname]


## Create the fake store module.
_fake_create_store("store")

# Setup the fake Ren'Py random module.
_fake_renpy_random = _FakeRenpyRandom()

# Setup the fake Ren'Py store module.
_fake_renpy_store = sys.modules["store"]
_fake_renpy_exports_store = _fake_renpy_store
sys.modules["renpy.store"] = sys.modules["store"]

# Setup the fake Ren'Py persistent store and assign it to the fake store module i.e. `renpy.store.persistent`
_fake_renpy_store.persistent = _FakeRenpyPersistent()  # type: ignore

# Assign the fake store to the fake store module i.e. `renpy.store.store`
_fake_renpy_store.store = sys.modules["store"]  # type: ignore

# Declare fake Ren'Py store variables.
_fake_renpy_store._ = _fake_renpy_  # type: ignore

_fake_renpy_store.chapter = 0  # type: ignore
_fake_renpy_store.ch1_choice = "sayori"  # type: ignore
_fake_renpy_store.skipping = None  # type: ignore
_fake_renpy_store._skipping = False  # type: ignore
_fake_renpy_store.dissolve = None  # type: ignore
_fake_renpy_store.i11 = None  # type: ignore

# Declare fake Ren'Py persistent variables.
_fake_renpy_store.persistent.playthrough = 0  # type: ignore
_fake_renpy_store.persistent.seen_sticker = False  # type: ignore
