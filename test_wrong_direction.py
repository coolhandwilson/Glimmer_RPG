from unittest import TestCase
from unittest.mock import patch
import io

from game import wrong_direction as wrong_direction


class TestWrongDirection(TestCase):

    @patch('builtins.input', return_value=[' '])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_direction_output_is_correct_when_character_at_boss(self, mock_output, _):
        direction = '3'  # South
        board = {(0, 0): 'Room 1', (0, 1): 'Room 2'}
        character = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        wrong_direction(character, board, direction)
        expected = ("\nYou think better of attempting this passage, and instead decide to gather supplies and rest."
                    "(Press enter to continue...)")
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('random.randint', return_value=0)
    @patch('builtins.input', return_value=[' '])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_direction_output_is_correct_when_character_not_at_boss(self, mock_output, _, __):
        direction = '3'  # South
        board = {(0, 0): 'Room 1', (0, 1): 'Room 2', (1, 1): 'Boss Room'}
        character = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        wrong_direction(character, board, direction)
        expected = ("\nYou take a deep breath, concentrate deeply, and will yourself to do the"
                    " impossible. With a burst of energy, you sprint with your head down and your"
                    " eyes closed as fast as you can...Directly into a wall.\n")
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
