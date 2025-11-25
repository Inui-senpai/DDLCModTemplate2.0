import sys
import random
import types
from unittest import mock
from .mocks import (
    _FakeRenpyEasy,
    _FakeRenpyNull,
    _FakeRenpyRandom,
    _fake_renpy_store,
    _FakeRenpyTextTextText,
    _fake_renpy_,
    _fake_renpy_window_hide,
)


class RenPyMock:
    """
    A mock class to simulate specific Ren'Py behaviors for testing purposes.
    """

    def __init__(self):
        # Initialize initial state for the mock
        # Basically `renpy.X` modules
        self.random = _FakeRenpyRandom()
        self.easy = _FakeRenpyEasy()
        self.store = _fake_renpy_store
        self.persistent = _fake_renpy_store.persistent
        self.windows = random.choice([True, False])
        self.pure = mock.MagicMock()

        # Create a mock for the renpy.text.text.Text class
        self.text = mock.MagicMock()
        self.text.text = mock.MagicMock()
        self.text.text.Text = _FakeRenpyTextTextText

        # Create displayable and null mocks
        self.Null = _FakeRenpyNull()

        # Add translation mock
        self._ = _fake_renpy_

        # Add window mock
        self._window_hide = _fake_renpy_window_hide

        # Add a mock for other Ren'Py functions if needed
        self.game = mock.MagicMock()
        self.gui = mock.MagicMock()
        self.config = mock.MagicMock()
        self.audio = mock.MagicMock()
        self.sound = mock.MagicMock()
        self.audio.music = mock.MagicMock()
        self.music = self.audio.music

        self.store.audio = mock.MagicMock()  # type: ignore
        self.store.config = self.config  # type: ignore
        self.store.gui = mock.MagicMock()  # type: ignore

    def __getattr__(self, name):
        # Try to get attribute from self first
        if name in self.__dict__:
            return self.__dict__[name]
        # Try to get attribute from store
        if hasattr(self.store, name):
            return getattr(self.store, name)
        # Attribute not found
        raise AttributeError(f"'RenPyMock' object has no attribute '{name}'")

    def restart_interaction(self):
        """
        Mock method to simulate restarting an interaction.
        """
        print("Interaction restarted.")
        pass

    def _window_hide(self):
        """
        Mock method to simulate hiding the window.
        """
        print("Window hidden.")
        pass

    def _window_auto(self):
        """
        Mock method to simulate auto-hiding the window.
        """
        print("Window set to auto.")
        pass

    def transition(self, transition=None):
        """
        Mock method to simulate a transition.
        """
        print("Transition called.")
        pass


def install_mock():
    """
    Install the RenPyMock into the namespace.
    """
    renpy_mock = RenPyMock()
    renpy_module = types.ModuleType("renpy")
    for attr in dir(renpy_mock):
        if not attr.startswith("__"):
            setattr(renpy_module, attr, getattr(renpy_mock, attr))
    sys.modules["renpy"] = renpy_module
