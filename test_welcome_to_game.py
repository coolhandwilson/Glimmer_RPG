from unittest import TestCase
import io
from unittest.mock import patch

from game import welcome_to_game as welcome_to_game


class TestWelcomeToGame(TestCase):

    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_to_game_output_for_correct_output_ascii_art(self, mock_output, _):
        welcome_to_game()
        actual_output = mock_output.getvalue()
        expected_output = r"""
                    .                  .-.    .  _   *     _   .
                       *          /   \     ((       _/ \       *    .
                     _    .   .--'\/\_ \     `      /    \  *    ___
                 *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
                   /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
              .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
                 /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
               /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
              /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
            @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
            @&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
            @88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
            `::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
             `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
                      _____   _   _                                       
                     / ____| | | (_)                                      
                    | |  __  | |  _   _ __ ___    _ __ ___     ___   _ __ 
                    | | |_ | | | | | | '_ ` _ \  | '_ ` _ \   / _ \ | '__|
                    | |__| | | | | | | | | | | | | | | | | | |  __/ | |   
                     \_____| |_| |_| |_| |_| |_| |_| |_| |_|  \___| |_|    
                            
                            Press enter to Continue...
        """
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_to_game_output_for_correct_output_first_paragragh(self, mock_output, _):
        welcome_to_game()
        actual_output = mock_output.getvalue()
        expected_output = ("Darkness surrounds you. You are an Avgrunnjagr. An Abyss Hunter. "
                           "You chart the forgotten paths and \ntrails that your ancestors carved "
                           "from the very stone of Mount Vrangir, forgotten since the Collapse.")
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_to_game_output_for_correct_output_second_paragragh(self, mock_output, _):
        welcome_to_game()
        actual_output = mock_output.getvalue()
        expected_output = ("\nThese streets, paths, and great halls sit abandoned under the Capital city of "
                           "Glittertind.\nYou hunt for precious ores and forgotten treasures. "
                           "You track and avoid the creatures you and your kin share the mountain with."
                           "\nYou chart safe paths for miners, surveyors, and tradesmen to follow.")
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_to_game_output_for_correct_output_third_paragragh(self, mock_output, _):
        welcome_to_game()
        actual_output = mock_output.getvalue()
        expected_output = ("\n\nBut today, you have made a mistake. Not your first. Maybe one of your last. "
                           "In the midst of exploring a crypt you discovered a trap door behind one of the tombs."
                           "\n\nA ladder carved directly into the stone of the crypt led down over 100 feet. "
                           "In your eagerness for the treasure you were sure you'd find, you were careless."
                           "\n\nThe rungs in the stone ladder had been worn away by father "
                           "time and many were weak and crumbling."
                           "\nIn your haste, you trust the wrong one with your full weight.")
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_to_game_output_for_correct_output_fourth_paragraph(self, mock_output, _):
        welcome_to_game()
        actual_output = mock_output.getvalue()
        expected_output = ("\nYou plummet, tumble, and land in a heap. You awaken in a haze. "
                           "\nA primal instinct rises from your gut, telling you to escape. "
                           "\n\n\n\n\n\n\n(Press enter to wake up...)\n")
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', '', '', ''])
    def test_welcome_to_game_return_value_is_none(self, _):
        actual = welcome_to_game()
        expected = None
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', '1234', 'astronaut', '`', ' '])
    def test_welcome_to_game_not_affected_by_input_type(self, _):
        actual = welcome_to_game()
        expected = None
        self.assertEqual(expected, actual)
