from unittest import TestCase
from unittest.mock import patch
import io

from game import user_combat_options


class TestUserCombatOptions(TestCase):

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_options_print_out_of_options(self, mock_output, _):
        character = {"Name": "Snake", "HP": 110, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        user_combat_options(character)
        actual = mock_output.getvalue()
        expected = "Call of the Void         Min Damage: 15   Max Damage: 27"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value="1")
    def test_user_combat_options_return_value(self, _):
        character = {"Name": "Snake", "HP": 110, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        actual = user_combat_options(character)
        expected = '1'
        self.assertEqual(expected, actual)
