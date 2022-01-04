import io
from unittest import TestCase
from unittest.mock import patch
from game import print_map


class TestPrintMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_check_player_is_present(self, mock_output):
        game_map = [[' [δ]', ' [ ]'], [' [ ]', ' [Ω]']]
        print_map(game_map)
        actual = mock_output.getvalue()
        expected = ' [δ]'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_check_special_item_is_present(self, mock_output):
        game_map = [[' [δ]', ' [ ]'], [' [¿]', ' [Ω]']]
        print_map(game_map)
        actual = mock_output.getvalue()
        expected = ' [¿]'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_check_boss_is_present(self, mock_output):
        game_map = [[' [ ]', ' [ ]'], [' [δ]', ' [Ω]']]
        print_map(game_map)
        actual = mock_output.getvalue()
        expected = ' [Ω]'
        self.assertIn(expected, actual)
