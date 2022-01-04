from unittest import TestCase

from game import search_room


class TestSearchRoom(TestCase):
    def test_search_room_no_items_in_room_check_arguments_unchanged(self):
        game_board = {(0, 0): ['Living Room', 'Nothing'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ['Stale Bread']}
        search_room(game_board, character)
        expected_character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ['Stale Bread']}
        expected_board = {(0, 0): ['Living Room', 'Nothing'],
                          (0, 1): ['Living Room', 'Nothing'],
                          (0, 2): ['Living Room', 'Nothing']}
        self.assertEqual(expected_board, game_board)
        self.assertEqual(expected_character, character)

    def test_search_room_regular_item_in_room_correct_changes(self):
        game_board = {(0, 0): ['Living Room', 'Water'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ['Water']}
        search_room(game_board, character)
        expected_character = {'Name': 'Al', 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ['Water', 'Water']}
        expected_board = {(0, 0): ['Living Room', 'Nothing'],
                          (0, 1): ['Living Room', 'Nothing'],
                          (0, 2): ['Living Room', 'Nothing']}
        self.assertEqual(expected_board, game_board)
        self.assertEqual(expected_character, character)

    def test_search_room_special_item_and_regular_item_in_room_correct_changes(self):
        game_board = {(0, 0): ['Living Room', 'Water', 'Helm of the Deep'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {'Name': 'Chuck', 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ['Water']}
        search_room(game_board, character)
        expected_character = {'Name': 'Chuck', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                              'Inventory': ['Water', 'Helm of the Deep', 'Water']}
        expected_board = {(0, 0): ['Living Room', 'Nothing'],
                          (0, 1): ['Living Room', 'Nothing'],
                          (0, 2): ['Living Room', 'Nothing']}
        self.assertEqual(expected_board, game_board)
        self.assertEqual(expected_character, character)

    def test_search_room_special_item_and_no_regular_item_in_room_correct_changes(self):
        game_board = {(0, 0): ['Living Room', 'Nothing', 'Helm of the Deep'],
                      (0, 1): ['Living Room', 'Nothing'],
                      (0, 2): ['Living Room', 'Nothing']}
        character = {'Name': 'Chuck', 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Inventory': ['Stale Bread']}
        search_room(game_board, character)
        expected_character = {'Name': 'Chuck', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                              'Inventory': ['Stale Bread', 'Helm of the Deep']}
        expected_board = {(0, 0): ['Living Room', 'Nothing'],
                          (0, 1): ['Living Room', 'Nothing'],
                          (0, 2): ['Living Room', 'Nothing']}
        self.assertEqual(expected_board, game_board)
        self.assertEqual(expected_character, character)
