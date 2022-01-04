from unittest import TestCase

from game import attribute_boost


class TestAttributeBoost(TestCase):

    def test_attribute_boost_regular_level_increase(self):
        snake = {"Name": "Snake", "Level": 2, "HP": 110, "Max HP": 110, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        attribute_boost(snake)
        expected = {"Name": "Snake", "Level": 2, "HP": 135, "Max HP": 135, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [9, 47]],
            ['Call of the Void', [19, 32]],
            ['Ild Beam', [26, 32]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected, snake)

    def test_attribute_boost_special_item_equipped(self):
        snake = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [5, 42]],
            ['Call of the Void', [15, 27]],
            ['Ild Beam', [22, 27]],
            ['Flee', [0, 0]]]}
        attribute_boost(snake, 2, 8, True)
        expected = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0, 'Attacks': [
            ['Concussive Blast', [7, 50]],
            ['Call of the Void', [17, 35]],
            ['Ild Beam', [24, 35]],
            ['Flee', [0, 0]]]}
        self.assertEqual(expected, snake)
