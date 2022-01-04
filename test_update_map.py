from unittest import TestCase
from game import update_map


class TestUpdateMap(TestCase):
    def test_update_map_with_player_movement_normal(self):
        board = {
            (0, 0): ['Dark Room', 'Nothing'],
            (1, 0): ['Crypt', 'Stale Bread'],
            (0, 1): ['Treasure Room', 'Water', 'Helm of the Deep'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        game_map = [[' [δ]', ' [ ]'], [' [¿]', ' [Ω]']]
        direction = '2'
        expected = [[' [ ]', ' [δ]'], [' [¿]', ' [Ω]']]
        character = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        update_map(direction, character, game_map, board)
        self.assertEqual(expected, game_map)

    def test_update_map_with_player_movement_onto_special_item(self):
        board = {
            (0, 0): ['Dark Room', 'Cheese'],
            (1, 0): ['Crypt', 'Stale Bread'],
            (0, 1): ['Treasure Room', 'Water', 'Helm of the Deep'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        game_map = [[' [δ]', ' [ ]'], [' [¿]', ' [Ω]']]
        direction = '3'
        expected = [[' [ ]', ' [ ]'], [' [δ]', ' [Ω]']]
        character = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        update_map(direction, character, game_map, board)
        self.assertEqual(expected, game_map)

    def test_update_map_with_player_movement_away_from_uncollected_special_item(self):
        board = {
            (0, 0): ['Dark Room', 'Milk'],
            (1, 0): ['Crypt', 'Stale Bread'],
            (0, 1): ['Treasure Room', 'Water', 'Helm of the Deep'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        game_map = [[' [ ]', ' [ ]'], [' [δ]', ' [Ω]']]
        direction = '1'
        expected = [[' [δ]', ' [ ]'], [' [¿]', ' [Ω]']]
        character = {'X-Coordinate': 0, 'Y-Coordinate': 1}
        update_map(direction, character, game_map, board)
        self.assertEqual(expected, game_map)

    def test_update_map_with_player_movement_onto_boss_room(self):
        board = {
            (0, 0): ['Dark Room', 'Cheddar', 'Helm of the Deep'],
            (1, 0): ['Crypt', 'Stale Bread'],
            (0, 1): ['Treasure Room', 'Water'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        game_map = [[' [¿]', ' [δ]'], [' [ ]', ' [Ω]']]
        direction = '3'
        expected = [[' [¿]', ' [ ]'], [' [ ]', ' [δ]']]
        character = {'X-Coordinate': 1, 'Y-Coordinate': 0}
        update_map(direction, character, game_map, board)
        self.assertEqual(expected, game_map)

    def test_update_map_with_player_movement_flee_from_boss(self):
        board = {
            (0, 0): ['Dark Room', 'Apple'],
            (0, 1): ['Crypt', 'Stale Bread'],
            (1, 0): ['Treasure Room', 'Water', 'Helm of the Deep'],
            (1, 1): ['Workshop', 'Grundar Mold']
        }
        game_map = [[' [ ]', ' [ ]'], [' [ ]', ' [δ]']]
        direction = '1'
        expected = [[' [ ]', ' [δ]'], [' [ ]', ' [Ω]']]
        character = {'X-Coordinate': 1, 'Y-Coordinate': 1}
        update_map(direction, character, game_map, board)
        self.assertEqual(expected, game_map)
