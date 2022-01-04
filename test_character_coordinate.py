from unittest import TestCase

from game import character_coordinate


class TestCharacterCoordinate(TestCase):

    def test_character_coordinate_generate_standard_coordinate(self):
        character = {'X-Coordinate': 8, 'Y-Coordinate': 10}
        expected = (8, 10)
        actual = character_coordinate(character)
        self.assertEqual(expected, actual)

    def test_character_coordinate_dictionary_input_is_unchanged(self):
        character = {'X-Coordinate': 54, 'Y-Coordinate': 1234}
        expected = {'X-Coordinate': 54, 'Y-Coordinate': 1234}
        character_coordinate(character)
        self.assertEqual(expected, character)
