from unittest import TestCase
from game import special_item_finder


class TestSpecialItemFinder(TestCase):

    def test_special_item_finder_return_value_of_normal_item(self):
        item = "Water"
        actual = special_item_finder(item)
        expected = False
        self.assertEqual(expected, actual)

    def test_special_item_finder_return_value_of_special_item(self):
        item = "Helm of the Deep"
        actual = special_item_finder(item)
        expected = True
        self.assertEqual(expected, actual)
