from unittest import TestCase
from game import class_storage


class TestClassStorage(TestCase):
    def test_class_storage_correct_return(self):
        expected_name = "Snake Plissken"
        expected_attack = "Whirlwind"
        class_name = "Berserker"
        actual = class_storage(class_name, expected_name)
        self.assertEqual(expected_name, actual["Name"])
        self.assertEqual(expected_attack, actual["Attacks"][0][0])
