from unittest import TestCase
from unittest.mock import patch
import io
from game import lore as lore


class TestLore(TestCase):

    @patch('builtins.input', side_effect=['', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lore_first_output_message_for_correct_output(self, mock_output, _):
        lore()
        actual_output = mock_output.getvalue()
        expected_output = ("""
    As you rest your bruised limbs, you reflect on your clan. A long line of Avgrunnjagrs, a role in Dwarven society
    made necessary by its own hubris. Why else would a specialized guild of warriors bent on investigating the ruins
    of your own civilization exist? Ancient Dwarves had thought themselves masters of the material world, and their
    hubris was such that they believed the Dwarven Age unending. Until it did. All things do.
    
    The conception that the other races have of Dwarves is true - hard workers, master artisans, metallurgists, 
    miners, smiths - masters of the Earthen skills. 
    
    But this conception is a narrow one, like viewing a mountain from a foot away. Only a glimpse.
    
    Dwarves had mastered many skills, and cared for more than just stone and ore. Yes, they made the finest jewelry and
    crafted perfect baguettes from the purist stones. But Dwarves had also mastered science. Chemistry. Poetry.
    War. The Old Ones had even mastered magic. Key word: 'Had'.
    
    You study a crack your gauntlet in the glow of the Orelight that surrounds you. You laugh at another one of the 
    stereotypes - that dwarves can see in the dark. Not true. The Orelight was old magic. So old that Dwarven society
    had no memory of it beyond sparse texts of how to concentrate it. The secret of making it had been lost in the 
    Collapse. (Press enter...)\n\n
    """)
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lore_second_output_message_for_correct_output(self, mock_output, _):
        lore()
        actual_output = mock_output.getvalue()
        expected_output = ("""
    The Collapse. A child's tale, now. A tale of the boogeyman. No one really knows what had happened. Ancient Dwarves
    hadn't prioritized record-keeping during their downfall. What they were escaping from, running from, fighting...
    just another mystery. But whatever it was, it was real. No make-believe Boogeyman had killed half of all Dwarves in
    Erithrain, collapsed the grand highways, or buried the Old Capital Cities. No, something happened. No idea what. 
    Not much sense in wondering, really. Your attention shifts to a glint from your armour in the Orelight.
    
    Weird stuff, it is. Whatever causes Orelight was imperceptible to the senses, but its effect was obvious. 
    Even the deepest corners of Mount Vrangir had a glow to them. Dwarves had, naturally, settled in areas where 
    concentrations of it were highest, to minimize the need for more brutish means of artificial light. 
    But as instrumental as it was, its uses spoke to a more nefarious origin. (Press enter...)\n\n
    """)
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['', '', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lore_third_output_message_for_correct_output(self, mock_output, _):
        lore()
        actual_output = mock_output.getvalue()
        expected_output = ("""
    Dwarven Warlocks, charlatans in comparison to ancient Dwarven mages if the history books that did survive are to 
    be trusted, can manipulate the Orelight into ferocious attacks. Melt through stone, golems, and even Admantium, 
    they can. But it came at a price. Orelight, whatever it is, is finite. The air is heavy after a spell is cast, 
    darker from the loss of the stuff. But it takes something from the Warlocks, too. They're ornery after a 
    spellcast, no doubt. Look days older, like they haven't slept in a month or eaten in longer. Talk about boogeyman, 
    wait til you see a Warlock after an Orebeam. Make sense that the Council regulates it so heavy. 
    But they still send out a Jagr patrol every week to explore some newfound section. A fool's hope that they'll 
    discover the secret to manufacturing more of it.
    
    You don't share the council's optimism, but...you do believe in treasure. There are pub stories about old weapons
    and jewelry imbued with Orelight. Ancient Dwarven artisans had, supposedly, been able to fuse the material into
    their wares. Some say they provide the wearer with special powers. You just think it'd be a nice addition to your
    retirement fund. Which is the whole damn reason you wound up in this situation in the first place...Time to get out
    of here...(Press enter)...\n\n\n
    """)
        self.assertIn(expected_output, actual_output)
