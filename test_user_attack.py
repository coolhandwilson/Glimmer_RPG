from unittest import TestCase
from unittest.mock import patch
import io

from game import user_attack


class TestUserAttack(TestCase):

    def test_user_attack_return_value_if_fleeing(self):
        character = {"Name": "Snake", "HP": 110}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        attack = "4"
        actual = user_attack(character, foe, attack)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='')
    def test_user_attack_return_value_if_fighting(self, _):
        character = {"Name": "Snake", "HP": 110, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        attack = "1"
        actual = user_attack(character, foe, attack)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[15, 10])
    def test_user_attack_change_to_character_if_fleeing(self, _):
        character = {"Name": "Snake", "HP": 110}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        attack = "4"
        user_attack(character, foe, attack)
        expected = {"Name": "Snake", "HP": 100}
        self.assertEqual(expected, character)

    @patch('builtins.input', return_value='')
    @patch('random.randint', return_value=5)
    def test_user_attack_foe_change_if_lower_bound_attack(self, _, __):
        character = {"Name": "Snake", "HP": 90, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        attack = "1"
        user_attack(character, foe, attack)
        expected = {'Name': 'Banshee', 'HP': 65, 'Damage': [5, 20], 'XP': 35}
        self.assertEqual(expected, foe)

    @patch('builtins.input', return_value='')
    @patch('random.randint', return_value=42)
    def test_user_attack_foe_change_if_lower_bound_attack(self, _, __):
        character = {"Name": "Snake", "HP": 80, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        foe = {'Name': 'Banshee', 'HP': 80, 'Damage': [5, 20], 'XP': 35}
        attack = "1"
        user_attack(character, foe, attack)
        expected = {'Name': 'Banshee', 'HP': 38, 'Damage': [5, 20], 'XP': 35}
        self.assertEqual(expected, foe)

    @patch('random.randint', return_value=20)
    @patch('builtins.input', return_value="")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_attack_output_if_choosing_second_attack(self, mock_output, __, ___):
        character = {"Name": "Snake", "HP": 9001, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        foe = {'Name': 'Banshee', 'HP': 80, 'Damage': [5, 20], 'XP': 35}
        attack = "2"
        user_attack(character, foe, attack)
        actual = mock_output.getvalue()
        expected = "Call of the Void does 20 damage"
        self.assertIn(expected, actual)
