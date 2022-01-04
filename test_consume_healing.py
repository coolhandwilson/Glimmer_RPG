from unittest import TestCase
from unittest.mock import patch
import io

from game import consume_healing


class TestConsumeHealing(TestCase):

    def test_consume_healing_valid_consumable_max_health(self):
        cher = {'Name': 'Cher', 'HP': 440, 'Max HP': 440, "Inventory": ['Stale Bread']}
        food = 'Stale Bread'
        consume_healing(food, cher)
        expected = {'Name': 'Cher', 'HP': 440, 'Max HP': 440, "Inventory": ['Stale Bread']}
        self.assertEqual(expected, cher)

    def test_consume_healing_valid_consumable_low_health(self):
        cher = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Stale Bread']}
        food = 'Stale Bread'
        consume_healing(food, cher)
        expected = {'Name': 'Cher', 'HP': 20, 'Max HP': 440, "Inventory": []}
        self.assertEqual(expected, cher)

    def test_consume_healing_valid_consumable_high_health(self):
        cher = {'Name': 'Cher', 'HP': 435, 'Max HP': 440, "Inventory": ['Stale Bread']}
        food = 'Stale Bread'
        consume_healing(food, cher)
        expected = {'Name': 'Cher', 'HP': 440, 'Max HP': 440, "Inventory": []}
        self.assertEqual(expected, cher)

    def test_consume_healing_invalid_consumable(self):
        cher = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Bucket of Nails']}
        food = 'Bucket of Nails'
        consume_healing(food, cher)
        expected = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Bucket of Nails']}
        self.assertEqual(expected, cher)

    def test_consume_healing_valid_consumable_is_mold(self):
        cher = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Grundar Mold']}
        food = 'Grundar Mold'
        consume_healing(food, cher)
        expected = {'Name': 'Cher', 'HP': 15, 'Max HP': 445, "Inventory": []}
        self.assertEqual(expected, cher)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_consume_healing_invalid_consumable_output_is_correct(self, mock_output):
        cher = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Paint']}
        food = 'Paint'
        consume_healing(food, cher)
        actual = mock_output.getvalue()
        expected = "Cher...Are..."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_consume_healing_valid_consumable_output_is_correct(self, mock_output):
        cher = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Stale Bread']}
        food = 'Stale Bread'
        consume_healing(food, cher)
        actual = mock_output.getvalue()
        expected = "is now 20, Cher"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_consume_healing_valid_mold_consumable_output_is_correct(self, mock_output):
        cher = {'Name': 'Cher', 'HP': 10, 'Max HP': 440, "Inventory": ['Grundar Mold']}
        food = 'Grundar Mold'
        consume_healing(food, cher)
        actual = mock_output.getvalue()
        expected = "max health is now 445, Cher"
        self.assertIn(expected, actual)
