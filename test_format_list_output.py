from unittest import TestCase
from unittest.mock import patch
import io

from game import format_list_output


class TestFormatListOutput(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_format_list_output_with_normal_list(self, mock_output):
        normal_list = ["apple", "fruit", "cheddar"]
        format_list_output(normal_list)
        actual = mock_output.getvalue()
        expected = ("1:	apple\n"
                    "2:	fruit\n"
                    "3:	cheddar\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_format_list_output_with_nested_combat_list(self, mock_output):
        nested_combat_list = [["poke", [200, 300]], ['shank', [800, 1000]], ['flee', [0, 0]]]
        format_list_output(nested_combat_list)
        actual = mock_output.getvalue()
        expected = ("1 poke                     Min Damage: 200  Max Damage: 300 \n" 
                    "2 shank                    Min Damage: 800  Max Damage: 1000\n"
                    "3 flee                     Min Damage: 0    Max Damage: 0   \n"
                    "")
        self.assertEqual(expected, actual)
