from unittest import TestCase
from game import health_check


class TestHealthCheck(TestCase):
    def test_health_check_if_character_at_full_health_recovery_at_default(self):
        character_dictionary = {'HP': 440, 'Max HP': 440}
        health_check(character_dictionary)
        expected = {'HP': 440, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_low_health_recovery_at_default(self):
        character_dictionary = {'HP': 1, 'Max HP': 440}
        health_check(character_dictionary)
        expected = {'HP': 11, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_near_full_health_recovery_at_default(self):
        character_dictionary = {'HP': 439, 'Max HP': 440}
        health_check(character_dictionary)
        expected = {'HP': 440, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_at_full_health_recovery_below_default(self):
        character_dictionary = {'HP': 440, 'Max HP': 440}
        health_check(character_dictionary, 5)
        expected = {'HP': 440, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_low_health_recovery_below_default(self):
        character_dictionary = {'HP': 1, 'Max HP': 440}
        health_check(character_dictionary, 5)
        expected = {'HP': 6, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_near_full_health_recovery_below_default(self):
        character_dictionary = {'HP': 439, 'Max HP': 440}
        health_check(character_dictionary, 5)
        expected = {'HP': 440, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_at_full_health_recovery_above_default(self):
        character_dictionary = {'HP': 440, 'Max HP': 440}
        health_check(character_dictionary, 30)
        expected = {'HP': 440, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_low_health_recovery_above_default(self):
        character_dictionary = {'HP': 1, 'Max HP': 440}
        health_check(character_dictionary, 30)
        expected = {'HP': 31, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)

    def test_health_check_if_character_near_full_health_recovery_above_default(self):
        character_dictionary = {'HP': 439, 'Max HP': 440}
        health_check(character_dictionary, 30)
        expected = {'HP': 440, 'Max HP': 440}
        self.assertEqual(expected, character_dictionary)
