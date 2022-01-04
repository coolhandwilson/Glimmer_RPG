from unittest import TestCase
from unittest.mock import patch
from game import view_inventory
import io


class TestViewInventory(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_view_inventory_valid_output_regular_items_only(self, mock_output):
        character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Inventory': ['Stale Bread', 'Water']}
        view_inventory(character)
        actual = mock_output.getvalue()
        expected = "Stale Bread"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_view_inventory_valid_output_special_items_only(self, mock_output):
        character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Inventory': ['Ring of Relvdrun', 'Helm of the Deep']}
        view_inventory(character)
        actual = mock_output.getvalue()
        expected = "Helm of the Deep"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_view_inventory_valid_output_special_item_and_normal_item(self, mock_output):
        character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Inventory': ['Water', 'Helm of the Deep']}
        view_inventory(character)
        actual = mock_output.getvalue()
        expected = "It appears you have found"
        self.assertIn(expected, actual)
