from unittest import TestCase
from unittest.mock import patch
import io

from game import class_information


class TestClassInformation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_information_output_for_valid_input(self, mock_output):
        choice = 'H1'
        user = "Bob"
        class_information(choice, user)
        actual = mock_output.getvalue()
        expected = "scouts use their stealth "
        self.assertIn(expected, actual)
