from unittest import TestCase
from game import coordinate_maker


class TestCoordinateMaker(TestCase):
    def test_coordinate_maker_standard_return(self):
        direction = "1"
        character = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        actual = coordinate_maker(direction, character)
        expected = (2, 1)
        self.assertEqual(expected, actual)

    def test_coordinate_maker_standard_return_dictionary_unchanged(self):
        direction = "1"
        character = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        coordinate_maker(direction, character)
        expected = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        self.assertEqual(expected, character)

    def test_coordinate_maker_standard_return_direction_unchanged(self):
        direction = "1"
        character = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        coordinate_maker(direction, character)
        expected = "1"
        self.assertEqual(expected, direction)
