from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckForFoes(TestCase):

    @patch('random.randint', return_value=0)
    def test_check_for_foes_low_bound_foes_present(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=30)
    def test_check_for_foes_upper_bound_foes_present(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=23)
    def test_check_for_foes_mid_range_foes_present(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=31)
    def test_check_for_foes_low_bound_no_foes(self, _):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=100)
    def test_check_for_foes_high_bound_no_foes(self, _):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=54)
    def test_check_for_foes_mid_range_no_foes(self, _):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)

