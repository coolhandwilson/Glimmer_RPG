from unittest import TestCase
from unittest.mock import patch
import io

from game import faux_information as faux_information


class TestFauxInformation(TestCase):

    @patch('builtins.input', return_value="")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_faux_information(self, mock_output, _):
        faux_information()
        actual = mock_output.getvalue()
        expected = ("""
    Ah ha! Looking for spoilers, are you!? Well you won't find them here. But I will tell you a few things, since you
    did go to the trouble of coming.
    
    1. Enemies scale to your level. Call it an apex predator's innate desire for a challenge, but the real baddies won't
       come out until you've toughened up a bit.
       
    2. If you read the lore you know that something happened to destroy eons of Dwarven history, and you've stumbled
       smack-dab into your very own adventure story that ties into it. Maybe animated crypt statues and afflicted 
       undead (or unliving, maybe) dwarves would have been your first hint but you probably didn't get that far before 
       coming here. That's okay. I'm curious by nature, too.
       
    3. The real piece of information I have for you is this: there is a significantly powerful enemy between you and
       freedom. They will never flee. After all, YOU are the one that barged into THEIR home. I shouldn't have to
       explain this but here we are. Anyways. You can flee if you're losing the fight, but they will regenerate. 
       Why? Definitely because of a real piece of lore and not because I wanted this to be challenging... 
       (No, really! I mean it. How did you think those dwarves got to be 'unliving'?).
    
    That's all for now, I think. Good luck!! (Press enter to continue)\n\n\n
    """)
        self.assertIn(expected, actual)
