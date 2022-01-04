from unittest import TestCase
from unittest.mock import patch
import io

from game import print_directions


class TestPrintDirections(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_directions_output_and_valid_input(self, mock_output):
        character = {"Name": "Sly"}
        print_directions(character)
        actual = mock_output.getvalue()
        expected = "you wish to travel, Sly or"
        self.assertIn(expected, actual)
