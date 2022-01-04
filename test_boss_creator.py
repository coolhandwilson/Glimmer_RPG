from unittest import TestCase

from game import boss_creator


class TestBossCreator(TestCase):
    def test_boss_creator_correct_return_value(self):
        actual = boss_creator()
        expected_name = "Afflicted King"
        expected_damage = [15, 30]
        self.assertEqual(expected_name, actual['Name'])
        self.assertEqual(expected_damage, actual['Damage'])
