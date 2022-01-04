from unittest import TestCase
from unittest.mock import patch
import io

from game import foe_selector


class TestFoeSelector(TestCase):

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_selector_output_in_sewer(self, mock_output, _):
        snake = {"Name": "Snake", "X-Coordinate": 0, "Y-Coordinate": 0, "HP": 20, "Level": 1, "Max HP": 50, 'XP': 25}
        game = {(0, 0): ["Sewer"]}
        foe_selector(snake, game)
        actual = mock_output.getvalue()
        expected = "Sewer Rat approaches!"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_selector_output_in_crypt(self, mock_output, _):
        snake = {"Name": "Snake", "X-Coordinate": 0, "Y-Coordinate": 0, "HP": 25, "Level": 2, "Max HP": 50, 'XP': 25}
        game = {(0, 0): ["Armoury"]}
        foe_selector(snake, game)
        actual = mock_output.getvalue()
        expected = "Crypt Warden approaches!"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='')
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_selector_output_general(self, mock_output, _, __):
        snake = {"Name": "Snake", "X-Coordinate": 0, "Y-Coordinate": 0, "HP": 20, "Level": 3, "Max HP": 50, 'XP': 25}
        game = {(0, 0): ["Rest Area"]}
        foe_selector(snake, game)
        actual = mock_output.getvalue()
        expected = "Afflicted Crypt Warden approaches!"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='')
    def test_foe_selector_return_value_in_sewer(self, _):
        snake = {"Name": "Snake", "X-Coordinate": 0, "Y-Coordinate": 0, "HP": 20, "Level": 1, "Max HP": 50, 'XP': 25}
        game = {(0, 0): ["Sewer"]}
        actual = foe_selector(snake, game)
        expected = "Sewer Rat"
        self.assertEqual(expected, actual["Name"])

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_selector_return_value_in_crypt(self, _, __):
        snake = {"Name": "Snake", "X-Coordinate": 0, "Y-Coordinate": 0, "HP": 25, "Level": 2, "Max HP": 50, 'XP': 25}
        game = {(0, 0): ["Armoury"]}
        actual = foe_selector(snake, game)
        expected = "Crypt Warden"
        self.assertIn(expected, actual["Name"])

    @patch('builtins.input', return_value='')
    @patch('random.randint', return_value=0)
    def test_foe_selector_return_value_general(self, _, __):
        snake = {"Name": "Snake", "X-Coordinate": 0, "Y-Coordinate": 0, "HP": 20, "Level": 3, "Max HP": 50, 'XP': 25}
        game = {(0, 0): ["Rest Area"]}
        actual = foe_selector(snake, game)
        expected = "Afflicted Crypt Warden"
        self.assertIn(expected, actual["Name"])
