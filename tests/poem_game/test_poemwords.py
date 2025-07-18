from game.poem_game.py.poemwords_ren import PoemWord, PoemWordDB
from tests.utils.base_test import DDLCTest

class TestPoemWordDB(DDLCTest):
    def test_poemwords_creation(self):
        self.start_test_time()

        # Setup
        db = self.create_poem_words_db()

        # Assert
        self.assertIsInstance(db, PoemWordDB)
        self.assertEqual(len(db.words), 0)

        self.end_test_time()

    def test_poemwords_adding(self):
        self.start_test_time()

        # Setup
        db = self.create_poem_words_db()
        db.add_word("happiness", 3, 2, 1)

        # Assert
        self.assertEqual(len(db.words), 1)
        self.assertEqual(db.words[0].word, "happiness")
        self.assertEqual(db.words[0].sPoint, 3)
        self.assertEqual(db.words[0].nPoint, 2)
        self.assertEqual(db.words[0].yPoint, 1)

        self.end_test_time()
    
    def test_poemwords_get_words(self):
        self.start_test_time()

        # Setup
        db = self.create_poem_words_db()
        db.add_word("happiness", 3, 2, 1)
        db.add_word("sadness", 1, 3, 2)

        # Test
        words = db.get_words()

        # Assert
        self.assertEqual(len(words), 2)
        self.assertIn("happiness", [word.word for word in words])
        self.assertIn("sadness", [word.word for word in words])

        self.end_test_time()

    def test_poemwords_get_words_str(self):
        self.start_test_time()

        # Setup
        db = self.create_poem_words_db()
        db.add_word("happiness", 3, 2, 1)
        db.add_word("sadness", 1, 3, 2)

        # Test
        words_str = db.get_words_str()

        # Assert
        self.assertEqual(len(words_str), 2)
        self.assertIn("happiness", words_str)
        self.assertIn("sadness", words_str)

        self.end_test_time()

    def test_poemwords_get_word(self):
        self.start_test_time()

        # Setup
        db = self.create_poem_words_db()
        db.add_word("happiness", 3, 2, 1)
        db.add_word("sadness", 1, 3, 2)
        db.add_word("anger", 2, 1, 3)

        # Test
        word = db.get_word("sadness")

        # Assert
        self.assertEqual(len(db.words), 3)
        self.assertIsNotNone(word)
        self.assertEqual(word.word, "sadness")
        self.assertEqual(word.sPoint, 1)
        self.assertEqual(word.nPoint, 3)
        self.assertEqual(word.yPoint, 2)

        self.end_test_time()

class TestPoemWord(DDLCTest):
    def test_poemword_creation(self):
        self.start_test_time()

        # Test
        word = PoemWord("joy", 5, 3, 2)

        # Assert
        self.assertIsNotNone(word)
        self.assertEqual(word.word, "joy")
        self.assertEqual(word.sPoint, 5)
        self.assertEqual(word.nPoint, 3)
        self.assertEqual(word.yPoint, 2)

        self.end_test_time()
    
    def test_poemword_str(self):
        self.start_test_time()

        # Test
        word = PoemWord("love", 4, 1, 3)

        # Assert
        self.assertEqual(word.__str__(), "love")

        self.end_test_time()