from game.poem_game.py.poemgame_chibi_ren import Chibi, ChibiDB, ChibiTransform
from tests.utils.base_test import DDLCTest


class ChibiTest(DDLCTest):
    def test_chibi_creation(self):
        """
        Test the creation of a Chibi character.
        """
        self.start_test_time()

        # Setup
        chibi = self.create_chibi("bronya")

        # Assert
        self.assertIsInstance(chibi, Chibi)
        self.assertEqual(chibi.name, "bronya")

        self.end_test_time()

    def test_chibi_transform_creation(self):
        """
        Test the creation of a ChibiTransform instance.
        """
        self.start_test_time()

        # Setup
        chibi_transform = self.create_chibi_transform()

        # Assert
        self.assertIsInstance(chibi_transform, ChibiTransform)

        self.end_test_time()

    def test_chibi_add_points(self):
        """
        Test adding points to a Chibi character.
        """
        self.start_test_time()

        # Setup
        chibi = self.create_chibi("bronya")

        # Test
        chibi.add_points(10)

        # Assert
        self.assertEqual(chibi.charPointTotal, 10)

        self.end_test_time()

    def test_positive_appeal(self):
        """
        Test the appeal calculation for a Chibi character.
        """
        self.start_test_time()

        # Setup
        chibi = self.create_chibi("bronya")
        chibi.add_points(50)

        # Test
        appeal = chibi.calculate_appeal()

        # Assert
        self.assertEqual(appeal, 1)

        self.end_test_time()

    def test_negative_appeal(self):
        """
        Test the appeal calculation for a Chibi character with negative points.
        """
        self.start_test_time()

        # Setup
        chibi = self.create_chibi("bronya")
        chibi.add_points(20)

        # Test
        appeal = chibi.calculate_appeal()

        # Assert
        self.assertEqual(appeal, -1)

        self.end_test_time()

    def test_neutral_appeal(self):
        """
        Test the appeal calculation for a Chibi character with neutral points.
        """
        self.start_test_time()

        # Setup
        chibi = self.create_chibi("bronya")
        chibi.add_points(30)

        # Test
        appeal = chibi.calculate_appeal()

        # Assert
        self.assertEqual(appeal, 0)

        self.end_test_time()

    def test_chibi_reset(self):
        """
        Test resetting a Chibi character.
        """
        self.start_test_time()

        # Setup
        chibi = self.create_chibi("bronya")
        chibi.add_points(10)

        # Test
        chibi.reset()

        # Assert
        self.assertEqual(chibi.charPointTotal, 0)

        self.end_test_time()


class ChibiDBTest(DDLCTest):
    def test_chibi_db_creation(self):
        """
        Test the creation of a ChibiDB instance.
        """
        self.start_test_time()

        # Setup
        chibi_db = self.create_chibi_db()

        # Assert
        self.assertIsInstance(chibi_db, ChibiDB)

        self.end_test_time()

    def test_chibi_db_add_character(self):
        """
        Test adding a character to the ChibiDB.
        """
        self.start_test_time()

        # Setup
        chibi_db = self.create_chibi_db()

        # Test
        chibi_db.add_chibi("bronya")

        # Assert
        self.assertEqual(len(chibi_db.chibis), 1)
        self.assertEqual(chibi_db.chibis[0].name, "bronya")

        self.end_test_time()

    def test_get_chibi(self):
        """
        Test retrieving a Chibi character by name from the ChibiDB.
        """
        self.start_test_time()

        # Setup
        chibi_db = self.create_chibi_db()
        chibi_db.add_chibi("bronya")
        chibi_db.add_chibi("carlotta")

        # Test
        chibi = chibi_db.get_chibi("bronya")

        # Assert
        self.assertEqual(len(chibi_db.chibis), 2)
        self.assertEqual(chibi.name, "bronya")

        self.end_test_time()

    def test_get_chibi_not_found(self):
        """
        Test retrieving a Chibi character that does not exist in the ChibiDB.
        """
        self.start_test_time()

        # Setup
        chibi_db = self.create_chibi_db()
        chibi_db.add_chibi("bronya")

        # Assert
        with self.assertRaises(ValueError):
            chibi_db.get_chibi("bronie")

        self.end_test_time()

    def test_chibi_db_reset(self):
        """
        Test resetting the ChibiDB.
        """
        self.start_test_time()

        # Setup
        chibi_db = self.create_chibi_db()
        chibi_db.add_chibi("bronya")
        chibi_db.add_chibi("carlotta")
        bronya = chibi_db.get_chibi("bronya")
        carlotta = chibi_db.get_chibi("carlotta")
        bronya.add_points(10)
        carlotta.add_points(20)

        # Test
        chibi_db.reset()

        # Assert
        self.assertEqual(len(chibi_db.chibis), 2)
        self.assertEqual(bronya.charPointTotal, 0)
        self.assertEqual(carlotta.charPointTotal, 0)

        self.end_test_time()
