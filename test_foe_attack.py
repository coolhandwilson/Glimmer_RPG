from unittest import TestCase
from unittest.mock import patch
import io

from game import foe_attack


class TestFoeAttack(TestCase):

    @patch('random.randint', return_value=5)
    def test_foe_attack_low_bound_attack_health_change(self, _):
        character = {"Name": "Snake", "HP": 302}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        foe_attack(foe, character)
        expected = {"Name": "Snake", "HP": 297}
        self.assertEqual(expected, character)

    @patch('random.randint', return_value=20)
    def test_foe_attack_upper_bound_attack_health_change(self, _):
        character = {"Name": "Snake", "HP": 30}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        foe_attack(foe, character)
        expected = {"Name": "Snake", "HP": 10}
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=15)
    def test_for_attack_print_output(self, _, mock_output):
        character = {"Name": "Snake", "HP": 200}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        foe_attack(foe, character)
        actual = mock_output.getvalue()
        expected = "15 damage against you, Snake!"
        self.assertIn(expected, actual)
