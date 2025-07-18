from unittest import mock
from game.poem_game.py.poemgame_ren import PoemGame
from tests.utils.base_test import DDLCTest
from tests.utils.mocks import (
    _fake_renpy_store,
    _fake_renpy_random,
)


class PoemGameTest(DDLCTest):
    def test_poemgame_initialization(self):
        """
        Test the initialization of the PoemGame class.
        """
        self.start_test_time()

        # Setup
        poem_game = self.create_poem_game()

        # Assert
        self.assertIsInstance(poem_game, PoemGame)
        self.assertFalse(poem_game.played_baa)
        self.assertFalse(poem_game.poemgame_glitch)
        self.assertEqual(poem_game.poem_progress, 1)
        self.assertTrue(poem_game.testing)

        self.end_test_time()

    @mock.patch("renpy.random", new=_fake_renpy_random)
    @mock.patch("renpy.store", new=_fake_renpy_store)
    def test_poemgame(self):
        """
        Test starting the PoemGame.
        """
        self.start_test_time()

        # Setup
        poem_game = self.create_poem_game()
        _fake_renpy_store.chapter = 1  # type: ignore

        # Test
        poem_game.start()
        poem_game.finish()

        # Assert
        self.assertEqual(poem_game.poem_progress, 21)

        self.end_test_time()

    @mock.patch("renpy.random", new=_fake_renpy_random)
    @mock.patch("renpy.store", new=_fake_renpy_store)
    def test_poemgame_start_act_one(self):
        """
        Test starting the PoemGame in Act One.
        """
        self.start_test_time()

        # Setup
        poem_game = self.create_poem_game()
        _fake_renpy_store.chapter = 0  # type: ignore

        # Test
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

        _fake_renpy_store.chapter = 1  # type: ignore
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

        _fake_renpy_store.chapter = 2  # type: ignore
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

        self.end_test_time()

    @mock.patch("renpy.random", new=_fake_renpy_random)
    @mock.patch("renpy.store", new=_fake_renpy_store)
    def test_poemgame_start_act_two(self):
        """
        Test starting the PoemGame in Act Two.
        """
        self.start_test_time()

        # Setup
        poem_game = self.create_poem_game()
        _fake_renpy_store.chapter = 0  # type: ignore
        _fake_renpy_store.persistent.playthrough = 2

        # Test
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

        _fake_renpy_store.chapter = 1  # type: ignore
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

        _fake_renpy_store.chapter = 2  # type: ignore
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

    @mock.patch("renpy.random", new=_fake_renpy_random)
    @mock.patch("renpy.store", new=_fake_renpy_store)
    def test_poemgame_start_act_three(self):
        """
        Test starting the PoemGame in Act Three.
        """
        self.start_test_time()

        # Setup
        poem_game = self.create_poem_game()
        _fake_renpy_store.persistent.playthrough = 3 # type: ignore

        # Test
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

    @mock.patch("renpy.random", new=_fake_renpy_random)
    @mock.patch("renpy.store", new=_fake_renpy_store)
    def test_poemgame_reset(self):
        """
        Test resetting the PoemGame.
        """
        self.start_test_time()

        # Setup
        poem_game = self.create_poem_game()
        poem_game.start()
        poem_game.finish()
        self.assertEqual(poem_game.poem_progress, 21)

        # Test
        poem_game.reset()

        # Assert
        self.assertFalse(poem_game.played_baa)
        self.assertFalse(poem_game.poemgame_glitch)
        self.assertEqual(poem_game.poem_progress, 1)

        self.end_test_time()
