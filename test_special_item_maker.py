from unittest import TestCase

from game import special_item_maker


class TestSpecialItemMaker(TestCase):

    def test_special_item_maker_three_possible_rooms_have_special_item(self):
        board = {(0, 0): ['Living Room', 'Grundar Mold'],
                 (0, 1): ['Living Room', 'Stale Bread'],
                 (0, 2): ['Living Room', 'Water'],
                 (0, 3): ['Living Room', 'Water'],
                 (0, 4): ['Living Room', 'Water'],
                 }
        special_item_maker(board)
        self.assertTrue(len(board[(0, 1)]) == 3)
        self.assertTrue(len(board[(0, 2)]) == 3)
        self.assertTrue(len(board[(0, 3)]) == 3)

    def test_special_item_maker_two_ineligible_rooms_are_unchanged(self):
        board = {(0, 0): ['Living Room', 'Water'],
                 (0, 1): ['Living Room', 'Stale Bread'],
                 (0, 2): ['Living Room', 'Water'],
                 (0, 3): ['Living Room', 'Water'],
                 (0, 4): ['Living Room', 'Water'],
                 }
        expected = {(0, 0): ['Living Room', 'Water'],
                    (0, 1): ['Living Room', 'Stale Bread', "Ring of Relvdrun"],
                    (0, 2): ['Living Room', 'Water', "Helm of the Deep"],
                    (0, 3): ['Living Room', 'Water', "Amulet of the First Flame"],
                    (0, 4): ['Living Room', 'Water'],
                    }
        special_item_maker(board)
        self.assertEqual(expected[(0, 0)], board[(0, 0)])
        self.assertEqual(expected[(0, 4)], board[(0, 4)])

    def test_special_item_maker_multiple_available_rooms_two_ineligible_rooms_unchanged(self):
        board = {(0, 0): ['Living Room', 'Nothing'],
                 (0, 1): ['Living Room', 'Stale Bread'],
                 (0, 2): ['Living Room', 'Water'],
                 (0, 3): ['Living Room', 'Water'],
                 (0, 4): ['Living Room', 'Stale Bread'],
                 (0, 5): ['Living Room', 'Water'],
                 (0, 6): ['Living Room', 'Water'],
                 (0, 7): ['Living Room', 'Water'],
                 }
        expected = {(0, 0): ['Living Room', 'Nothing'], (0, 7): ['Living Room', 'Water']}
        special_item_maker(board)
        self.assertEqual(expected[(0, 0)], board[(0, 0)])
        self.assertEqual(expected[(0, 7)], board[(0, 7)])
