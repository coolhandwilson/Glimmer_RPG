from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):

    @patch('game.get_class_choice', return_value="Scout")
    def test_make_character_check_proper_return_value(self, _):
        name = "Sly Stallone"
        actual = make_character(name)
        expected_health = 85
        expected_attack = "Sneak Attack"
        self.assertEqual(expected_health, actual["HP"])
        self.assertEqual(expected_attack, actual["Attacks"][0][0])
