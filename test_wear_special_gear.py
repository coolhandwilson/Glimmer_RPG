from unittest import TestCase
from unittest.mock import patch
import io

from game import wear_special_gear


class TestWearSpecialGear(TestCase):
    def test_wear_special_gear_wear_helm_valid_changes_to_character(self):
        character = {"Name": "Snake", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                     'Attacks': [
                         ['Concussive Blast', [5, 42]],
                         ['Call of the Void', [15, 27]],
                         ['Ild Beam', [22, 27]],
                         ['Flee', [0, 0]]],
                     'Equipped': {
                        'Head': None,
                        'Hand': None,
                        'Neck': None,
                        },
                     'Inventory': ["Helm of the Deep"]}
        wear_special_gear('Helm of the Deep', character)
        expected = {"Name": "Snake", "Level": 1, "HP": 140, 'Max HP': 140, 'XP': 0,
                    'Attacks': [
                         ['Concussive Blast', [5, 42]],
                         ['Call of the Void', [15, 27]],
                         ['Ild Beam', [22, 27]],
                         ['Flee', [0, 0]]],
                    'Equipped': {
                        'Head': "Helm of the Deep",
                        'Hand': None,
                        'Neck': None,
                        },
                    'Inventory': []}
        self.assertEqual(character, expected)

    def test_wear_special_gear_wear_ring_valid_changes_to_character(self):
        character = {"Name": "Sly", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                     'Attacks': [
                         ['Concussive Blast', [5, 42]],
                         ['Call of the Void', [15, 27]],
                         ['Ild Beam', [22, 27]],
                         ['Flee', [0, 0]]],
                     'Equipped': {
                        'Head': None,
                        'Hand': None,
                        'Neck': None,
                        },
                     'Inventory': ['Ring of Relvdrun']}
        wear_special_gear('Ring of Relvdrun', character)
        expected = {"Name": "Sly", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                    'Attacks': [
                         ['Concussive Blast', [12, 44]],
                         ['Call of the Void', [22, 29]],
                         ['Ild Beam', [29, 29]],
                         ['Flee', [0, 0]]],
                    'Equipped': {
                        'Head': None,
                        'Hand': 'Ring of Relvdrun',
                        'Neck': None,
                        },
                    'Inventory': []}
        self.assertEqual(character, expected)

    def test_wear_special_gear_wear_amulet_valid_changes_to_character(self):
        character = {"Name": "Chuck", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                     'Attacks': [
                         ['Concussive Blast', [5, 42]],
                         ['Call of the Void', [15, 27]],
                         ['Ild Beam', [22, 27]],
                         ['Flee', [0, 0]]],
                     'Equipped': {
                        'Head': None,
                        'Hand': None,
                        'Neck': None,
                        },
                     'Inventory': ["Amulet of the First Flame"]}
        wear_special_gear('Amulet of the First Flame', character)
        expected = {"Name": "Chuck", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                    'Attacks': [
                         ['Concussive Blast', [7, 50]],
                         ['Call of the Void', [17, 35]],
                         ['Ild Beam', [24, 35]],
                         ['Flee', [0, 0]]],
                    'Equipped': {
                        'Head': None,
                        'Hand': None,
                        'Neck': 'Amulet of the First Flame',
                        },
                    'Inventory': []}
        self.assertEqual(character, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wear_special_gear_wear_amulet_valid_print_output(self, mock_output):
        character = {"Name": "Snoop Dogg", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                     'Attacks': [
                         ['Concussive Blast', [5, 42]],
                         ['Call of the Void', [15, 27]],
                         ['Ild Beam', [22, 27]],
                         ['Flee', [0, 0]]],
                     'Equipped': {
                        'Head': None,
                        'Hand': None,
                        'Neck': None,
                        },
                     'Inventory': ["Amulet of the First Flame"]}
        wear_special_gear('Amulet of the First Flame', character)
        actual = mock_output.getvalue()
        expected = "2 and maximum attack by 8."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wear_special_gear_wear_ring_valid_print_output(self, mock_output):
        character = {"Name": "Snoop Dogg", "Level": 1, "HP": 110, 'Max HP': 110, 'XP': 0,
                     'Attacks': [
                         ['Concussive Blast', [5, 42]],
                         ['Call of the Void', [15, 27]],
                         ['Ild Beam', [22, 27]],
                         ['Flee', [0, 0]]],
                     'Equipped': {
                        'Head': None,
                        'Hand': None,
                        'Neck': None,
                        },
                     'Inventory': ['Ring of Relvdrun']}
        wear_special_gear('Ring of Relvdrun', character)
        actual = mock_output.getvalue()
        expected = "7 and maximum attack by 2."
        self.assertIn(expected, actual)
