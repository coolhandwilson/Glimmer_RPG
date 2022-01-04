from unittest import TestCase
from unittest.mock import patch

from game import boss_combat_loop


class TestBossCombatLoop(TestCase):

    @patch('game.flee', return_value=True)
    @patch('builtins.input', return_value='')
    @patch('random.randint', side_effect=[5, 29, 21])
    @patch('game.user_combat_options', side_effect=['1', '4'])
    def test_boss_combat_one_round_combat_and_flee_no_damage(self, _, __, ___, ____):
        character = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        king = {'Name': "Afflicted King", 'Damage': [15, 30], 'HP': 225}
        boss_combat_loop(character, king)
        expected_character = {"Name": "Snake", "Level": 1, "HP": 81, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected_character, character)
