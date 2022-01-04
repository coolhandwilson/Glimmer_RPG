from unittest import TestCase
from unittest.mock import patch
import io

from game import heal_items


class TestHealItems(TestCase):

    @patch('builtins.input', return_value="")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_items_output_if_no_items_in_inventory(self, mock_output, _):
        dolly_partition = {"Name": "Dolly", "Inventory": []}
        heal_items(dolly_partition)
        actual = mock_output.getvalue()
        expected = "no items in your satch"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['1', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_items_output_if_no_healing_items_inventory(self, mock_output, _):
        dolly_partition = {"Name": "Dolly", "Inventory": ["Helm of the Deep"]}
        heal_items(dolly_partition)
        actual = mock_output.getvalue()
        expected = "Dolly...Are...Ar"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['1', ''])
    def test_heal_items_character_unchanged_if_no_healing_items_inventory(self, _):
        dolly_partition = {"Name": "Dolly", "Inventory": ["Helm of the Deep"]}
        heal_items(dolly_partition)
        expected = {"Name": "Dolly", "Inventory": ["Helm of the Deep"]}
        self.assertEqual(expected, dolly_partition)

    @patch('builtins.input', side_effect=['1', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_items_character_output_healing_items_from_inventory_consumed_and_health_is_low(self, mock_output, _):
        dolly_partition = {"HP": 10, "Max HP": 20, "Name": "Dolly", "Inventory": ["Stale Bread", "Water", "Water"]}
        heal_items(dolly_partition)
        actual = mock_output.getvalue()
        expected = "feel more rested and energet"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['1', ''])
    def test_heal_items_character_changed_healing_items_from_inventory_consumed_and_health_is_low(self, _):
        dolly_partition = {"HP": 10, "Max HP": 20, "Name": "Dolly", "Inventory": ["Stale Bread", "Water", "Water"]}
        heal_items(dolly_partition)
        expected = {"HP": 20, "Max HP": 20, "Name": "Dolly", "Inventory": ["Water", "Water"]}
        self.assertEqual(expected, dolly_partition)

    @patch('builtins.input', side_effect=['1', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_items_character_output_healing_items_from_inventory_consumed_and_health_full(self, mock_output, _):
        dolly_partition = {"HP": 20, "Max HP": 20, "Name": "Dolly", "Inventory": ["Stale Bread", "Water", "Water"]}
        heal_items(dolly_partition)
        actual = mock_output.getvalue()
        expected = "Dolly. Do not waste"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['1', ''])
    def test_heal_items_character_unchanged_healing_when_health_is_full(self, _):
        dolly_partition = {"HP": 20, "Max HP": 20, "Name": "Dolly", "Inventory": ["Stale Bread", "Water", "Water"]}
        heal_items(dolly_partition)
        expected = {"HP": 20, "Max HP": 20, "Name": "Dolly", "Inventory": ["Stale Bread", "Water", "Water"]}
        self.assertEqual(expected, dolly_partition)

    @patch('builtins.input', side_effect=['1', ''])
    def test_heal_items_character_unchanged_if_user_inputs_return_key(self, _):
        dolly_partition = {"HP": 18, "Max HP": 20, "Name": "Dolly", "Inventory": []}
        heal_items(dolly_partition)
        expected = {"HP": 18, "Max HP": 20, "Name": "Dolly", "Inventory": []}
        self.assertEqual(expected, dolly_partition)
