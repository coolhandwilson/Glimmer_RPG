from unittest import TestCase
from unittest.mock import patch
from game import turn_based_heal

import io


class TestTurnBasedHeal(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_turn_based_heal_correct_output(self, mock_output):
        madonna = {"HP": 50, "Max HP": 100, "Equipped": []}
        turn_based_heal(madonna)
        actual = mock_output.getvalue()
        expected = "time heals all wounds. Even"
        self.assertIn(expected, actual)

    def test_turn_based_heal_with_no_amulet_low_health(self):
        madonna = {"HP": 50, "Max HP": 100, "Equipped": []}
        turn_based_heal(madonna)
        expected = {"HP": 60, "Max HP": 100, "Equipped": []}
        self.assertEqual(expected, madonna)

    def test_turn_based_heal_with_no_amulet_full_health(self):
        madonna = {"HP": 100, "Max HP": 100, "Equipped": []}
        turn_based_heal(madonna)
        expected = {"HP": 100, "Max HP": 100, "Equipped": []}
        self.assertEqual(expected, madonna)

    def test_turn_based_heal_wth_no_amulet_high_health(self):
        madonna = {"HP": 95, "Max HP": 100, "Equipped": []}
        turn_based_heal(madonna)
        expected = {"HP": 100, "Max HP": 100, "Equipped": []}
        self.assertEqual(expected, madonna)

    def test_turn_based_heal_with_amulet_low_health(self):
        madonna = {"HP": 1, "Max HP": 100, "Equipped": ["Amulet of the First Flame"]}
        turn_based_heal(madonna)
        expected = {"HP": 16, "Max HP": 100, "Equipped": ["Amulet of the First Flame"]}
        self.assertEqual(expected, madonna)

    def test_turn_based_heal_with_amulet_full_health(self):
        madonna = {"HP": 100, "Max HP": 100, "Equipped": ["Amulet of the First Flame"]}
        turn_based_heal(madonna)
        expected = {"HP": 100, "Max HP": 100, "Equipped": ["Amulet of the First Flame"]}
        self.assertEqual(expected, madonna)

    def test_turn_based_heal_with_amulet_high_health(self):
        madonna = {"HP": 87, "Max HP": 100, "Equipped": ["Amulet of the First Flame"]}
        turn_based_heal(madonna)
        expected = {"HP": 100, "Max HP": 100, "Equipped": ["Amulet of the First Flame"]}
        self.assertEqual(expected, madonna)
