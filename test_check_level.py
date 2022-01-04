from unittest import TestCase
from unittest.mock import patch
import io

from game import check_level


class TestCheckLevel(TestCase):
    def test_check_level_max_level_remains_unchanged(self):
        user = {"Name": "Snake", "Level": 3, "HP": 110, "Max HP": 110, 'XP': 0,
                'Future Levels': [(2, 150), (3, 350)], 'Rank': 'Expert'}
        check_level(user)
        expected = {"Name": "Snake", "Level": 3, "HP": 110, "Max HP": 110, 'XP': 0,
                    'Future Levels': [(2, 150), (3, 350)], 'Rank': 'Expert'}
        self.assertEqual(expected, user)

    def test_check_level_not_enough_experience_remains_unchanged(self):
        user = {"Name": "Snake", "Level": 1, "HP": 110, "Max HP": 110, 'XP': 0,
                'Future Levels': [(2, 150), (3, 350)]}
        check_level(user)
        expected = {"Name": "Snake", "Level": 1, "HP": 110, "Max HP": 110, 'XP': 0,
                    'Future Levels': [(2, 150), (3, 350)]}
        self.assertEqual(expected, user)

    def test_check_level_new_level_updated(self):
        user = {"Name": "Snake", "Level": 1, "HP": 110, "Max HP": 110, 'XP': 160, 'Future Levels': [(2, 150), (3, 350)],
                'Attacks': [
                ['Concussive Blast', [9, 47]],
                ['Call of the Void', [19, 32]],
                ['Ild Beam', [26, 32]],
                ['Flee', [0, 0]]],
                'Rank': 'Novice'}
        check_level(user)
        expected = {"Name": "Snake", "Level": 2, "HP": 135, "Max HP": 135, 'XP': 160,
                    'Future Levels': [(2, 150), (3, 350)],
                    'Attacks': [
                     ['Concussive Blast', [13, 52]],
                     ['Call of the Void', [23, 37]],
                     ['Ild Beam', [30, 37]],
                     ['Flee', [0, 0]]],
                    'Rank': 'Intermediate'}
        self.assertEqual(expected, user)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_level_new_level_output(self, mock_output):
        user = {"Name": "Sly", "Level": 1, "HP": 110, "Max HP": 110, 'XP': 160, 'Future Levels': [(2, 150), (3, 350)],
                'Attacks': [
                ['Concussive Blast', [9, 47]],
                ['Call of the Void', [19, 32]],
                ['Ild Beam', [26, 32]],
                ['Flee', [0, 0]]],
                'Rank': 'Novice'}
        check_level(user)
        actual = mock_output.getvalue()
        expected = "Max HP is now 135"
        self.assertIn(expected, actual)
