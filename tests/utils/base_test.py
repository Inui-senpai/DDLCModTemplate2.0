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
    
    def create_poem_words_db(self):
        """
        Helper method to create a PoemWordsDB instance for testing.
        
        :return: An instance of PoemWordsDB.
        """
        from game.poem_game.py.poemwords_ren import PoemWordDB
        return PoemWordDB()
    
    def create_chibi_db(self):
        """
        Helper method to create a ChibiDB instance for testing.
        
        :return: An instance of ChibiDB.
        """
        from game.poem_game.py.poemgame_chibi_ren import ChibiDB
        return ChibiDB()
    
    def create_chibi(self, name: str):
        """
        Helper method to create a Chibi character for testing.
        
        :param name: Name of the Chibi character.
        :return: An instance of Chibi.
        """
        from game.poem_game.py.poemgame_chibi_ren import Chibi
        return Chibi(name)
    
    def create_chibi_transform(self):
        """
        Helper method to create a ChibiTransform instance for testing.
        
        :return: An instance of ChibiTransform.
        """
        from game.poem_game.py.poemgame_chibi_ren import ChibiTransform
        return ChibiTransform()
    
    def create_poem_game(self):
        """
        Helper method to create a PoemGame instance for testing.
        
        :param testing: If True, bypasses Ren'Py functions and screens for testing purposes.
        :return: An instance of PoemGame.
        """
        from game.poem_game.py.poemgame_ren import PoemGame
        return PoemGame(testing=True)