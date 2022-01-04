from unittest import TestCase
from unittest.mock import patch
import io

from game import experience_points


class TestExperiencePoints(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_experience_points_with_user_retreat(self, mock_output):
        chuck = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30}
        experience_points(chuck, enemy, True, False)
        actual = mock_output.getvalue()
        expected = "right call, Snake"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_experience_points_with_foe_retreat(self, mock_output):
        chuck = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30}
        experience_points(chuck, enemy, False, True)
        actual = mock_output.getvalue()
        expected = "your might, Snake!"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_experience_points_with_max_level_user(self, mock_output):
        chuck = {"Name": "Snake", "Level": 3, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 0, 'Damage': [1, 18], 'XP': 30}
        experience_points(chuck, enemy, False, False)
        actual = mock_output.getvalue()
        expected = "Cave Spider! You bask "
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_experience_points_max_level_user_foe_retreat(self, mock_output):
        chuck = {"Name": "Sly", "Level": 3, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 40, 'Damage': [1, 18], 'XP': 30}
        experience_points(chuck, enemy, False, True)
        actual = mock_output.getvalue()
        expected = "your might, Sly!\n"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_experience_points_with_level_one_user(self, mock_output):
        chuck = {"Name": "Norris", "Level": 3, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 0, 'Damage': [1, 18], 'XP': 30}
        experience_points(chuck, enemy, False, False)
        actual = mock_output.getvalue()
        expected = "You have defeated the Cave Spider!"
        self.assertIn(expected, actual)

    def test_experience_points_updated_for_level_one(self):
        snake = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 0, 'Damage': [1, 18], 'XP': 30}
        experience_points(snake, enemy, False, False)
        expected = {"Name": "Snake", "Level": 1, "HP": 110, 'XP': 30}
        self.assertEqual(expected, snake)

    def test_experience_points_updated_for_fleeing_foe(self):
        snake = {"Name": "Snake", "Level": 2, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 40, 'XP': 30, 'Damage': [1, 18]}
        experience_points(snake, enemy, False, True)
        expected = {"Name": "Snake", "Level": 2, "HP": 110, 'XP': 15.0}
        self.assertEqual(expected, snake)

    def test_experience_points_unchanged_for_retreat(self):
        snake = {"Name": "Snake", "Level": 2, "HP": 110, 'XP': 0}
        enemy = {'Name': 'Cave Spider', 'HP': 40, 'XP': 30, 'Damage': [1, 18]}
        experience_points(snake, enemy, True, False)
        expected = {"Name": "Snake", "Level": 2, "HP": 110, 'XP': 0}
        self.assertEqual(expected, snake)

    def test_experience_points_unchanged_for_max_level(self):
        snake = {"Name": "Snake", "Level": 3, "HP": 110, 'XP': 4053}
        enemy = {'Name': 'Cave Spider', 'HP': 40, 'XP': 30, 'Damage': [1, 18]}
        experience_points(snake, enemy, False, False)
        expected = {"Name": "Snake", "Level": 3, "HP": 110, 'XP': 4053}
        self.assertEqual(expected, snake)
