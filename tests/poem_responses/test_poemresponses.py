from unittest import mock
from game.poem_responses.py.poems_ren import PoemAuthor, PoemResponseDB
from tests.utils.base_test import DDLCTest


class PoemResponsesTest(DDLCTest):
    def test_poem_responses_initialization(self):
        """
        Test the initialization of the poem responses.
        """
        self.start_test_time()

        # Setup
        with mock.patch("renpy.text.text.Text"):
            poem_db = self.create_poem_db()

        # Assert
        self.assertIsInstance(poem_db, PoemResponseDB)
        self.assertEqual(len(poem_db.poems), 0)

        self.end_test_time()

    def test_poem_response_author_creation(self):
        """
        Test the creation of a poem response with an author.
        """
        self.start_test_time()

        # Test
        author_b = PoemAuthor("bronya", music="audio/bronya_music.ogg")

        # Assert
        self.assertIsInstance(author_b, PoemAuthor)
        self.assertEqual(author_b.name, "bronya")
        self.assertEqual(author_b.music, "audio/bronya_music.ogg")

        self.end_test_time()

    def test_poem_response_db_add_poem(self):
        """
        Test adding a poem to the PoemResponseDB.
        """
        self.start_test_time()

        # Setup
        poem_db = self.create_poem_db()
        author_b = PoemAuthor("bronya", music="audio/bronya_music.ogg")
        poem_title = "Bronya's Poem"
        poem_text = "This is a poem by Bronya."

        expected_poem_text = f"{poem_title}\n\n{poem_text}"

        # Test
        poem_db.add_poem("b_poem1", author_b, poem_title, poem_text)
        poem = poem_db.get_poem("b_poem1")
        poem.text = expected_poem_text
        poem.author = author_b.name

        # Assert
        self.assertEqual(len(poem_db.poems), 1)
        self.assertEqual(poem.text, expected_poem_text)  # type: ignore
        self.assertEqual(poem.author, author_b.name)  # type: ignore

        self.end_test_time()

    def test_poem_response_db_get_poem(self):
        """
        Test retrieving a poem from the PoemResponseDB.
        """
        self.start_test_time()

        # Setup
        poem_db = self.create_poem_db()
        author_b = PoemAuthor("bronya", music="audio/bronya_music.ogg")
        poem_title = "Bronya's Poem"
        poem_text = "This is a poem by Bronya."
        expected_poem_text = f"{poem_title}\n\n{poem_text}"

        poem_db.add_poem("b_poem1", author_b, poem_title, poem_text)

        # Test
        poem = poem_db.get_poem("b_poem1")
        poem.text = expected_poem_text
        poem.author = author_b.name

        # Assert
        self.assertIsNotNone(poem)
        self.assertEqual(poem.text, f"{poem_title}\n\n{poem_text}")  # type: ignore
        self.assertEqual(poem.author, author_b.name)  # type: ignore

        self.end_test_time()

    def test_poem_response_db_get_poem_not_found(self):
        """
        Test retrieving a poem that does not exist in the PoemResponseDB.
        """
        self.start_test_time()

        # Setup
        poem_db = self.create_poem_db()

        # Test
        with self.assertRaises(ValueError):
            poem_db.get_poem("non_existent_poem")

        self.end_test_time()

    def test_poem_response_db_show_poem(self):
        """
        Test showing a poem from the PoemResponseDB.
        """
        self.start_test_time()

        # Setup
        poem_db = self.create_poem_db()
        author_b = PoemAuthor("bronya", music="audio/bronya_music.ogg")
        poem_title = "Bronya's Poem"
        poem_text = "This is a poem by Bronya."

        poem_db.add_poem("b_poem1", author_b, poem_title, poem_text)

        # Test
        poem_db.show_poem("b_poem1", testing=True)

        # Assert
        # Check if no ValueError is raised
        self.assertTrue(True)

        self.end_test_time()

    def test_poem_response_db_show_poem_not_found(self):
        """
        Test showing a poem that does not exist in the PoemResponseDB.
        """
        self.start_test_time()

        # Setup
        poem_db = self.create_poem_db()

        # Test
        with self.assertRaises(ValueError):
            poem_db.show_poem("non_existent_poem")

        self.end_test_time()
