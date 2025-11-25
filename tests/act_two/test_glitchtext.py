from tests.utils.base_test import DDLCTest

class TestGlitchtext(DDLCTest):
    def test_generate_glitchtext(self):
        self.start_test_time()

        # Test
        text = self.generate_glitchtext(20)

        # Assert
        self.assertEqual(len(text), 20)
    
    def test_generate_glitchtext_with_different_lengths(self):
        self.start_test_time()

        # Test with different lengths
        for length in [10, 50, 100]:
            text = self.generate_glitchtext(length)
            self.assertEqual(len(text), length)

        self.end_test_time()
