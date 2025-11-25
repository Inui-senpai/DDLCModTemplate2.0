from tests.utils.base_test import DDLCTest

class TestConsole(DDLCTest):
    def test_console_creation(self):
        self.start_test_time()

        # Setup
        console = self.create_console()

        # Assert
        self.assertEqual(console.console_delay, 0.5)
        self.assertEqual(console.console_cps, 30)
        self.assertEqual(console.max_log_history, 5)
        self.assertEqual(len(console.console_history), 0)

        self.end_test_time()

    def test_console_call(self):
        self.start_test_time()

        # Setup
        console = self.create_console()
        input_text = 'os.remove("characters/yuri.chr")'
        output_text = "yuri.chr deleted successfully."

        # Test
        console(input_text, output_text)

        # Assert
        self.assertEqual(len(console.console_history), 1)
        self.assertIn(input_text, console.console_history)
        self.assertEqual(console.console_history[input_text], output_text)

        self.end_test_time()

    def test_console_with_limits(self):
        self.start_test_time()

        # Setup
        console = self.create_console(max_log_history=2)
        input_texts = [
            'os.remove("characters/monika.chr")',
            'os.remove("characters/natsuki.chr")',
            'os.remove("characters/sayori.chr")',
        ]
        output_texts = [
            "monika.chr deleted successfully.",
            "natsuki.chr deleted successfully.",
            "sayori.chr deleted successfully.",
        ]

        # Test
        for input_text, output_text in zip(input_texts, output_texts):
            console(input_text, output_text)

        # Assert
        self.assertEqual(len(console.console_history), 2)
        self.assertNotIn('os.remove("characters/monika.chr")', console.console_history)
        self.assertIn('os.remove("characters/natsuki.chr")', console.console_history)
        self.assertIn('os.remove("characters/sayori.chr")', console.console_history)

        self.assertEqual(
            console.console_history['os.remove("characters/natsuki.chr")'],
            "natsuki.chr deleted successfully.",
        )
        self.assertEqual(
            console.console_history['os.remove("characters/sayori.chr")'],
            "sayori.chr deleted successfully.",
        )

        self.end_test_time()

    def test_clear_console_history(self):
        self.start_test_time()

        # Setup
        console = self.create_console()
        input_text = 'os.remove("characters/monika.chr")'
        output_text = "monika.chr deleted successfully."

        # Test
        console(input_text, output_text)
        console.console_history.clear()

        # Assert
        self.assertEqual(len(console.console_history), 0)

        self.end_test_time()
