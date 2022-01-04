from unittest import TestCase
from game import types_of_foes


class TestTypesOfFoes(TestCase):
    def test_types_of_foes_correct_return(self):
        character = {"Level": 2}
        actual = types_of_foes(character)
        expected_length = 3
        expected_entry = "Banshee"
        self.assertEqual(expected_length, len(actual))
        self.assertIn(expected_entry, actual[2]["Name"])
