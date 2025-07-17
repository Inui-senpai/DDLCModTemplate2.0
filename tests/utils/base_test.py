import time
import sys
from unittest import TestCase
from unittest import mock

sys.modules["renpy"] = mock.MagicMock()

class DDLCTest(TestCase):
    """
    Base class for all DDLC `_ren.py` tests.
    """

    def start_test_time(self):
        """
        Starts the timer for the test.
        """
        self.start_time = time.time()

    def end_test_time(self):
        """
        Ends the timer for the test and prints the time taken.
        """
        end_time = time.time()
        print(f"{self.id()} took {end_time - self.start_time:.2f} seconds")

    def create_console(self, **kwargs):
        """
        Helper method to create a Console instance with the given parameters.
        
        :param kwargs: Parameters to pass to the Console constructor.
        :return: An instance of Console.
        """
        from game.act_two.py.console_ren import Console
        defaults = {
            'console_delay': 0.5,
            'console_cps': 30,
            'max_log_history': 5,
            'testing': True
        }
        defaults.update(kwargs)
        return Console(**defaults)

    def generate_glitchtext(self, length: int):
        """
        Helper method to generate glitch text for testing.
        
        :param length: Length of the glitch text to generate.
        :return: A string of glitch text.
        """
        from game.act_two.py.glitchtext_ren import glitchtext
        return glitchtext(length)