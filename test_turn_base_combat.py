from unittest import TestCase
from unittest.mock import patch

from game import turn_base_combat


class TestTurnBaseCombat(TestCase):

    @patch('game.flee', return_value=True)
    @patch('builtins.input', side_effect=['', ''])
    @patch('random.randint', side_effect=[30, 10])
    @patch('game.user_combat_options', return_value='1')
    @patch('game.foe_selector', return_value={'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30, })
    def test_turn_base_combat_with_one_round_attack_and_foe_flee(self, _, __, ___, ____, _____):
        character = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        board = {(0, 0): ["Room"]}
        turn_base_combat(character, board)
        expected_character = {"Name": "Snake", "Level": 1, "HP": 100, 'XP': 15.0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected_character, character)

    @patch('game.flee', return_value=False)
    @patch('builtins.input', side_effect=['', ''])
    @patch('random.randint', side_effect=[40, 10])
    @patch('game.user_combat_options', return_value='1')
    @patch('game.foe_selector', return_value={'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30, })
    def test_turn_base_combat_with_one_round_attack_and_victory(self, _, __, ___, ____, _____):
        character = {"Name": "Sly", "Level": 1, "HP": 110, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        board = {(0, 0): ["Room"]}
        turn_base_combat(character, board)
        expected_character = {"Name": "Sly", "Level": 1, 'XP': 30, "HP": 110, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected_character, character)

    @patch('game.flee', return_value=False)
    @patch('builtins.input', side_effect=['', ''])
    @patch('random.randint', side_effect=[30, 10])
    @patch('game.user_combat_options', return_value='1')
    @patch('game.foe_selector', return_value={'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30, })
    def test_turn_base_combat_with_one_round_attack_and_loss(self, _, __, ___, ____, _____):
        chuck = {"Name": "Chuck", "Level": 1, "HP": 10, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        new_board = {(0, 0): ["Crypt"]}
        turn_base_combat(chuck, new_board)
        expected_character = {"Name": "Chuck", "Level": 1, "HP": 0, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected_character, chuck)

    @patch('random.randint', side_effect=[10, 10])
    @patch('game.user_combat_options', return_value='4')
    @patch('game.foe_selector', return_value={'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30, })
    def test_turn_base_combat_with_one_round_with_strategic_retreat(self, _, __, ___):
        chuck = {"Name": "Moe", "Level": 1, "HP": 50, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        new_board = {(0, 0): ["Crypt"]}
        turn_base_combat(chuck, new_board)
        expected_character = {"Name": "Moe", "Level": 1, "HP": 40, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected_character, chuck)
