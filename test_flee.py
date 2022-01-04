from unittest import TestCase
from unittest.mock import patch
import io

from game import flee


class TestFlee(TestCase):

    @patch('random.randint', return_value=1)
    def test_flee_foe_successful_flee_low_bound(self, _):
        character = {"Name": "Snake"}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        expected = True
        actual = flee(character, foe, True)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=20)
    def test_flee_foe_successful_flee_upper_bound(self, _):
        character = {"Name": "Snake"}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        expected = True
        actual = flee(character, foe, True)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=21)
    def test_flee_foe_does_not_flee_low_bound(self, _):
        character = {"Name": "Snake"}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        expected = False
        actual = flee(character, foe, True)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=100)
    def test_flee_foe_does_not_flee_upper_bound(self, _):
        character = {"Name": "Snake"}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        expected = False
        actual = flee(character, foe, True)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[0, 10])
    def test_flee_user_flee_foe_low_bound_successful_attack_successful_damage(self, _):
        character = {"Name": "Snake", "HP": 100}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        flee(character, foe, False)
        expected = {"Name": "Snake", "HP": 90}
        self.assertEqual(expected, character)

    @patch('random.randint', side_effect=[20, 10])
    def test_flee_user_flee_foe_upper_bound_successful_attack_successful_damage(self, _):
        character = {"Name": "Snake", "HP": 90}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        flee(character, foe, False)
        expected = {"Name": "Snake", "HP": 80}
        self.assertEqual(expected, character)

    @patch('random.randint', return_value=21)
    def test_flee_user_flee_foe_misses_attack_lower_bound(self, _):
        character = {"Name": "Snake", "HP": 70}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        flee(character, foe, False)
        expected = {"Name": "Snake", "HP": 70}
        self.assertEqual(expected, character)

    @patch('random.randint', return_value=100)
    def test_flee_user_flee_foe_misses_attack_upper_bound(self, _):
        character = {"Name": "Snake", "HP": 65}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        flee(character, foe, False)
        expected = {"Name": "Snake", "HP": 65}
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=100)
    def test_flee_output_for_user_flee_and_foe_attacks(self, _, mock_output):
        character = {"Name": "Snake", "HP": 50}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        flee(character, foe, False)
        actual = mock_output.getvalue()
        expected = 'escape without'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[19, 10])
    def test_flee_output_for_user_flee_and_foe_hits(self, _, mock_output):
        character = {"Name": "Snake", "HP": 30}
        foe = {'Name': 'Banshee', 'HP': 70, 'Damage': [5, 20], 'XP': 35}
        flee(character, foe, False)
        actual = mock_output.getvalue()
        expected = 'your guard, Snake!'
        self.assertIn(expected, actual)
