from unittest import TestCase
from unittest.mock import patch
import io

from game import tutorial as tutorial


class TestTutorial(TestCase):

    @patch('builtins.input', return_value="")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tutorial_print_output_is_correct(self, mock_output, _):
        tutorial()
        actual = mock_output.getvalue()
        expected = ("""
    Okay, here's the deal: You're being hunted by...something. You aren't sure what but it sure as hell isn't a 
    cave spider. I mean, those are after you too but that's a day in the life. No, you can sense that you aren't alone
    here, and whatever it is - it is smart enough to stay hidden. To watch. To take stock of a new factor in its home.
    Luckily you still have your gear, so you aren't totally helpless, but you need to get to safety. 
    
    Here's some things to keep in mind:
    
    1. You're a trained warrior, so with time you can refocus and even heal lesser wounds. You'll probably start to feel
       better as you move from room to room.
    
    2. You cannot heal during combat. I don't know why anyone would think that eating some bread would
       be feasible during a life-and-death struggle with animated statues or ferocious beasts. I have to imagine the
       last thought on a Dwarf's mind as they're being mauled by a Cave Spider is "I should eat some of that bread I
       found earlier. That would help right now, I'm sure of it!", but I digress. Bottom line: No healing in combat.
       Fight, Flee, or Die.
    
    3. You saw some konsentreriums around when you first got your bearings. No time for a history lesson but if you find
       one, you can meditate and regain some health. Thank your ancestors for their foresight while you're at it.
    
    4. Look, this is a bad situation but if you don't at least look around while you're here it'd be such a waste. You
       never know what you might find. Trinkets, jewelry, ancient objects of untold power...who knows.
    
    5. Whatever this place is, it's a grid. North-South, East-West - not much help in a deep, forgotten, underground
       horror-dungeon but you get the idea. Your internal compass, trained since birth, urges you to go Southeast.
       Whenever you think about heading that way, you see this thing: '[Ω]'. Ominous, right? 
       Anyways. Best not to tarry, I'd say.
       
    6. You'll figure out how to move as you go along, but your numpad is your friend. Most instructions can be done that
       way.
    
    7. One last thing. If you find food, maybe water, you should probably take it. Is the idea of eating centuries old
       somehow-still-preserved bread revolting? Yes. Is it instrumental to your survival? Also yes.\n\n
    """)
        self.assertIn(expected, actual)
