from unittest import TestCase
import io
from unittest.mock import patch
from game import end_game as end_game


class TestEndGame(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_output_if_player_dead_ascii_art(self, mock_output):
        with self.assertRaises(SystemExit):
            end_game(dead=True, winner=False)
        actual = mock_output.getvalue()
        expected = r"""
                                         __________
                                      .~#########%%;~.
                                     /############%%;`\
                                    /######/~\/~\%%;,;,\
                                   |#######\    /;;;;.,.|
                                   |#########\/%;;;;;.,.|
                          XX       |##/~~\####%;;;/~~\;,|       XX
                        XX..X      |#|  o  \##%;/  o  |.|      X..XX
                      XX.....X     |##\____/##%;\____/.,|     X.....XX
                 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
                X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
                X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
                X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
                 X# \.X        @#%,.@                  @#%,.@        X./  #
                  ##  X          @#%,.@              @#%,.@          X   #
                , "# #X            @#%,.@          @#%,.@            X ##
                   `###X             @#%,.@      @#%,.@             ####'
                  . ' ###              @#%.,@  @#%,.@              ###`"
                    . ";"                @#%.@#%,.@                ;"` ' .
                      '                    @#%,.@                   ,.
                      ` ,                @#%,.@  @@                `
                                          @@@  @@@  
                                    
                                     You have died, Jagr.
            """
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_output_if_player_dead_message(self, mock_output):
        with self.assertRaises(SystemExit):
            end_game(dead=True, winner=False)
        actual = mock_output.getvalue()
        expected = ("\nYour bones join the legions of other brave "
                    "souls who thought they could survive the abyss. Farewell.")
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_output_if_player_exits(self, mock_output):
        with self.assertRaises(SystemExit):
            end_game(dead=False, winner=False)
        actual = mock_output.getvalue()
        expected = ("\nYou feel a calm coldness grip your heart and the call of your ancestors fills your ears. "
                    "\n\nYour struggle has ended, adventurer. Farewell...")
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_output_if_player_wins_farewell_message(self, mock_output):
        with self.assertRaises(SystemExit):
            end_game(dead=False, winner=True)
        actual = mock_output.getvalue()
        expected = r"""
                                       _
                                     _|=|__________
                                    /              \
                                   /                \
                                  /__________________\
                                   ||  || /--\ ||  ||
                                   ||[]|| | .| ||[]||
                                 ()||__||_|__|_||__||()
                                ( )|-|-|-|====|-|-|-|( ) 
                                ^^^^^^^^^^====^^^^^^^^^^^
                                    Home Sweet Home.
        """
        self.assertTrue(expected in actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game_output_if_player_wins_ascii_art(self, mock_output):
        with self.assertRaises(SystemExit):
            end_game(dead=False, winner=True)
        actual = mock_output.getvalue()
        expected = "Congratulations! You win! Thank you for playing my game :)"
        self.assertIn(expected, actual)
