from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location
import io


class TestDescribeCurrentLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_latrine(self, mock_output):
        game_board = {(0, 0): ['Latrine', 'Nothing']}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        describe_current_location(game_board, character)
        actual = mock_output.getvalue()
        expected = "restrooms. This one looks nicer "
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output):
        game_board = {(0, 0): ['Crypt', 'Nothing']}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        describe_current_location(game_board, character)
        actual = mock_output.getvalue()
        expected = " so these dead are now nameless."
        self.assertIn(expected, actual)
