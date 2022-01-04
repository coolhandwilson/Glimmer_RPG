from unittest import TestCase
from unittest.mock import patch
import io

from game import equip_item


class TestEquipItem(TestCase):

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_equip_item_one_special_items_output(self, mock_output, _):
        character = {"Name": "Snake", "Level": 1, "HP": 110, 'Max HP': 120, 'XP': 0,
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
        equip_item(character)
        actual = mock_output.getvalue()
        expected = "surge of power course through your veins"
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_equip_item_no_special_items_output(self, mock_output, _):
        character = {"Name": "Snake", "Level": 1, "HP": 110, 'Max HP': 120, 'XP': 0,
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
                     'Inventory': ["Water"]}
        equip_item(character)
        actual = mock_output.getvalue()
        expected = "no equippable items in your inventory, Snake"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['0', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_equip_item_one_special_item_output_invalid_and_valid_input(self, mock_output, _):
        character = {"Name": "Laser", "Level": 1, "HP": 110, 'Max HP': 120, 'XP': 0,
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
        equip_item(character)
        actual = mock_output.getvalue()
        expected = "surge of power course through your veins"
        self.assertIn(expected, actual)
