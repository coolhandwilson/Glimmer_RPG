from unittest import TestCase
from game import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_entity_is_dead_return_value_if_exactly_zero(self):
        character = {"HP": 0, "X-Coordinate": 0, "Y-Coordinate": 1}
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_alive_entity_is_dead_return_value_if_less_than_zero(self):
        character = {"HP": -984, "X-Coordinate": 0, "Y-Coordinate": 1}
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_alive_entity_is_alive_return_value_if_health_is_one(self):
        character = {"HP": 1, "X-Coordinate": 0, "Y-Coordinate": 1}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_entity_is_dead_return_value_if_health_is_high(self):
        character = {"HP": 6546857491, "X-Coordinate": 0, "Y-Coordinate": 1}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)
