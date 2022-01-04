# ----------------------------------------------------------------------------------- #
# ---------- ---------- ---------- TABLE OF CONTENTS ---------- ---------- ---------- #
# ----------------------------------------------------------------------------------- #
#
# --> LINE 55   ----  IMPORTED MODULES
#
# --> LINE 64   ----  GAME CRITICAL FUNCTIONS
#
# --> LINE 483  ----  BOARD AND MAP SYSTEM
#
# --> LINE 634  ----  USER NAME SYSTEM
#
# --> LINE 661  ----  CHARACTER CREATION SYSTEM
#
# --> LINE 882  ----  DESCRIBE LOCATION SYSTEM
#
# --> LINE 932  ----  MOVEMENT SYSTEM
#
# --> LINE 1102 ----  HEALTH SYSTEM
#
# --> LINE 1290 ----  FOE SELECTION SYSTEM
#
# --> LINE 1405 ----  COMBAT SYSTEM
#
# --> LINE 1555 ----  XP SYSTEM
#
# --> LINE 1650 ----  BOSS SYSTEM
#
# --> LINE 1763 ----  ITEM SEARCH SYSTEM
#
# --> LINE 1798 ----  INVENTORY SYSTEM
#
# --> LINE 1904 ----  CHOICE SYSTEM
#
# --> LINE 1959 ----  MAIN GAME LOOP
#
# --> LINE 2045 ----  MAIN()
#
# --> LINE 2052 ----  IF-MAIN-CONDITIONAL
#
# ---------------------------------------------------------------------------------- #
# ---------- ---------- ---------- ---------------- ---------- ---------- ---------- #
# ---------------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Imported Modules ---------- ---------- ---------- #
# ---------------------------------------------------------------------------------- #
import random
import itertools
import sys

# ----------------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Game Critical Functions ---------- ---------- ---------- #
# ----------------------------------------------------------------------------------------- #


def welcome_to_game():
    """
    Provides backstory to user on game start.

    :param: None
    :pre-condition: None
    :post-condition: print output, input prompts to pace user reading but no permanent changes to memory landscape
    :return: None
    """
    mountain = r"""
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

    intro_one = ("Darkness surrounds you. You are an Avgrunnjagr. An Abyss Hunter. You chart the forgotten paths and "
                 "\ntrails that your ancestors carved from the very stone of Mount Vrangir, "
                 "forgotten since the Collapse.")

    intro_two = ("\nThese streets, paths, and great halls sit abandoned under the Capital city of "
                 "Glittertind.\nYou hunt for precious ores and forgotten treasures. "
                 "You track and avoid the creatures you and your kin share the mountain with."
                 "\nYou chart safe paths for miners, surveyors, and tradesmen to follow.")

    intro_three = ("\n\nBut today, you have made a mistake. Not your first. Maybe one of your last. In the midst of "
                   "exploring a crypt you discovered a trap door behind one of the tombs."
                   "\n\nA ladder carved directly into the stone of the crypt led down over 100 feet. "
                   "In your eagerness for the treasure you were sure you'd find, you were careless."
                   "\n\nThe rungs in the stone ladder had been worn away by father "
                   "time and many were weak and crumbling."
                   "\nIn your haste, you trust the wrong one with your full weight.")

    intro_four = ("\nYou plummet, tumble, and land in a heap. You awaken in a haze. "
                  "\nA primal instinct rises from your gut, telling you to escape. "
                  "\n\n\n\n\n\n\n(Press enter to wake up...)\n")

    output_list = [mountain, intro_one, intro_two, intro_three, intro_four]

    for item in output_list:
        print(item)
        input()


def end_game(dead: bool = False, winner: bool = False) -> None:
    """
    End the game.

    :param dead: a boolean
    :param winner: a boolean
    :pre-condition: dead must be a boolean in True, False format
    :pre-condition: winner must be a boolean in True, False Format
    :pre-condition: both dead and winner cannot be True at the same time
    :post-condition: the program ends - if dead and winner are False, a regular goodbye output is printed
                     if dead is True, user gets some gnarley death art before sys.exit runs
                     if dead is False and winner is True, user gets a sweet victory message before sys.exit runs
    :post-condition: print output, end of program - no other changes to memory landscape
    :return: a farewell message in string form
    """
    dead_message = r"""
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

    dead_message_two = ("\nYour bones join the legions of other brave "
                        "souls who thought they could survive the abyss. Farewell.")

    goodbye_message = ("\nYou feel a calm coldness grip your heart and the call of your ancestors fills your ears. "
                       "\n\nYour struggle has ended, adventurer. Farewell...")

    sweet_victory_one = r"""
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

    sweet_victory_two = "Congratulations! You win! Thank you for playing my game :)"

    if dead:
        print(dead_message, dead_message_two)

    elif dead is False and winner is True:
        print(sweet_victory_one, sweet_victory_two)

    else:
        print(goodbye_message)

    sys.exit()


def lore() -> None:
    """
    Provide user with lore.

    :param: None
    :pre-condition: None
    :post-condition: print output, input prompts to pace user reading but no permanent changes to memory landscape
    :return: None
    """
    lore_one = ("""
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
    lore_two = ("""
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
    lore_three = ("""
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
    output_list = [lore_one, lore_two, lore_three]

    for item in output_list:
        print(item)
        input()


def tutorial() -> None:
    """
    Provide basic user interface information.

    :param: None
    :pre-condition: None
    :post-condition: print output, input prompts to pace user reading but no permanent changes to memory landscape
    :return: None
    """
    tutorial_message = ("""
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

    print(tutorial_message)
    input()


def faux_information() -> None:
    """
    Provide basic user with faux (like foe! Haha..ha..) information

    :param: None
    :pre-condition: None
    :post-condition: print output, input prompts to pace user reading but no permanent changes to memory landscape
    :return: None
    """
    foe_information = ("""
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

    print(foe_information)
    input()


def wrong_direction(character: dict, board: dict, direction: str) -> None:
    """
    Provide message to user regarding direction choice.

    :param character: a dictionary
    :param board: a dictionary
    :param direction: a string
    :pre-condition: character must be a dictionary in character format
    :pre-condition: board must be a dictionary in board format
    :pre-condition: direction must be a string in ['1', '2', '3', '4']
    :post-condition: print output, input prompts used to pace user reading but input not stored in memory landscape
    :post-condition: character, board, direction are unchanged by this function
    :return: None
    """
    invalid_directions = [
        ("\nYou take a deep breath, concentrate deeply, and will yourself to do the"
         " impossible. With a burst of energy, you sprint with your head down and your"
         " eyes closed as fast as you can...Directly into a wall.\n"),
        ("\nYou investigate the wall closely, looking for signs of weakness you could tunnel"
         " through or holes large enough to crawl in...But your search is in vain.\n"),
        ("\nYou notice the passage you intended to traverse has recently collapsed.\nYou "
         "inspect the rubble to determine whether there is any hope of clearing it..."
         "But to no avail. The way is shut.\n")
    ]
    if coordinate_maker(direction, character) == max(board):
        print("\nYou think better of attempting this passage, and instead decide to gather supplies and rest."
              "(Press enter to continue...)")
        input()

    else:
        print(invalid_directions[random.randint(0, len(invalid_directions) - 1)] +
              ("\nDespite your best efforts, you cannot go this way.\n"
               "Time to try another direction.\n"))
        input()


def format_list_output(game_list) -> None:
    """
    Neatly print user's input options.

    :param game_list: an iterable
    :pre-condition: game_list must be a non-empty list object containing the user's input options
    :pre-condition: game_iterable may be a non-empty nested list object in character dictionary attack list format
    :post-condition: neatly formatted output
    :post-condition: game_iterable is unchanged by this function
    :return: None
    """
    litmus_test = type(game_list[0])

    for number, choice in enumerate(game_list, 1):
        if litmus_test == list:
            print('{:<2}{:<25}Min Damage: {:<4} Max Damage: {:<4}'.format(str(number), choice[0], str(choice[1][0]),
                                                                          str(choice[1][1])))

        else:
            print(str(number) + ":\t" + choice)


def random_item_maker(board: dict) -> None:
    """
    Potentially spawn a basic item in a room with "Nothing".

    :param board: a dictionary
    :pre-condition: board must be a dictionary in game board format
    :post-condition: The items at index 1 of each value in the board dictionary may be changed at random
    :return: None
    """
    standard_item_list = ["Stale Bread", "Water", "Grundar Mold"]

    # The current odds are set at 30% chance of a new item - separate odds for which item is added
    lucky_room_list = [key for key, value in board.items() if value[1] == "Nothing" and random.randint(1, 100) <= 30]

    if len(lucky_room_list) != 0:
        # Lower odds for the better item (Grundar - permanent health buff)
        random_item_list = random.choices(standard_item_list, weights=[40, 40, 20], k=len(lucky_room_list))

    else:
        return

    for number, item in enumerate(lucky_room_list):
        board[item].insert(1, random_item_list[number])
        board[item].remove("Nothing")


def special_item_maker(board: dict) -> None:
    """
    Place rare equitable items randomly on the game board.

    :param board: a dictionary
    :pre-condition: board must be a dictionary in game board format
    :post-condition: three board[key] values will have special items added to their lists, but the starting room and
                     boss room will never receive special items
    :return: None
    """
    special_items = ["Ring of Relvdrun", "Helm of the Deep", "Amulet of the First Flame"]
    # Remove possibility that special items spawn in boss room and start room
    possible_rooms = list(board)
    possible_rooms.remove(max(board))
    possible_rooms.remove(min(board))
    # 3 rooms from possible_rooms without duplication
    rooms = random.sample(possible_rooms, k=3)
    for number, room in enumerate(rooms):
        board[room].append(special_items[number])


def character_coordinate(character: dict) -> tuple:
    """
    Give X-Y coordinates of character in tuple format.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: a tuple representing the player's x-y coordinates on the board
    :post-condition: character will is unchanged by this function
    :return: a tuple

    # Standard usage
    >>> small_dictionary = {'X-Coordinate': 8, 'Y-Coordinate': 10}
    >>> character_coordinate(small_dictionary)
    (8, 10)
    >>> small_dictionary == {'X-Coordinate': 8, 'Y-Coordinate': 10}
    True

    # With additional dictionary keys
    >>> bigger_dictionary = {'X-Coordinate': 21, 'favourite cheese': 'cheddar', 'Y-Coordinate': 31}
    >>> character_coordinate(bigger_dictionary)
    (21, 31)
    >>> bigger_dictionary == {'X-Coordinate': 21, 'favourite cheese': 'cheddar', 'Y-Coordinate': 31}
    True
    """
    return character['X-Coordinate'], character['Y-Coordinate']


# ------------------------------------------------------------------------------------ #
# ---------- ---------- ---------- Board & Map System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------------ #
def make_board(rows: int, columns: int) -> dict:
    """
    Create a game board for the game.

    :param rows: a number
    :param columns: a number
    :pre-condition: rows must be a positive, non-zero integer
    :pre-condition: columns must be a positive, non-zero integer
    :post-condition: a dictionary containing coordinates, descriptions, and random items for each room on the map in
                     game board format
    :post-condition: rows and columns are unchanged by this function
    :return: a list of coordinates and room names in dictionary form
    """
    # Base lists for room types and items
    items = ['Nothing',
             'Stale Bread',
             'Water',
             'Grundar Mold']

    room_descriptions = ['Dark Room',
                         'Crypt',
                         'Treasure Room',
                         'Workshop',
                         'Armoury',
                         'Cavern',
                         'Rest Area',
                         'Market',
                         'Sewer',
                         'Latrine']

    # Generate random board from room_descriptions and items based on number of rows and columns
    game_board = {coordinate: [random.choice(room_descriptions), random.choice(items)]
                  for coordinate in list(itertools.product(range(rows), range(columns)))}

    return game_board


def make_map(game_board: dict) -> list:
    """
    Generate a visual map for the User.

    :param game_board: a dictionary
    :pre-condition: game_board must be a dictionary in game board format
    :post-condition: a list of matrices representing a 2D, flattened version of the game_board
    :post-condition: game_board is unchanged by this function
    :return: a 2D map in list form
    """
    # determine number of rows and columns
    size_of_map = max(game_board)

    # Pycharm warnings if anything other than under or dunder used here
    game_map = [[' [ ]' for _ in range(size_of_map[0] + 1)] for __ in range(size_of_map[1] + 1)]

    # Add special items
    for number, value in enumerate(game_board.values()):
        if len(value) == 3:
            map_row = number // (size_of_map[1] + 1)
            map_room = number % (size_of_map[0] + 1)
            game_map[map_room].insert(map_row, ' [¿]')
            game_map[map_room].pop(map_row + 1)

    # Add User's initial position
    game_map[0][0] = ' [δ]'

    # Add Boss Symbol to final square
    game_map[-1][-1] = ' [Ω]'

    return game_map


def update_map(direction: str, character: dict, game_map: list, game_board: dict) -> None:
    """
    Update 2D map to show User's current position.

    :param direction: a string
    :param character: a dictionary
    :param game_map: a list
    :param game_board: a dictionary
    :pre-condition: direction must be a single character string in ['1', '2', '3', '4']
    :pre-condition: character must be a dictionary in character format
    :pre-condition: game_map must be a list in 2D map format
    :pre-condition: game_board must be a dictionary in game board format
    :post-condition: game_map is updated to reflect User's current position, other parameters are unchanged
    :return: an updated version of the game_map list

    # Standard Use
    >>> small_dictionary = {'X-Coordinate': 0, 'Y-Coordinate': 0}
    >>> small_game_board = {(0, 0): 'one', (0, 1): 'two', (1, 0): 'three', (1, 1): 'four'}
    >>> one_direction = '2'
    >>> one_game_map = [[' [δ]', ' [ ]'], [' [ ]', ' [Ω]']]
    >>> update_map(one_direction, small_dictionary, one_game_map, small_game_board)
    >>> one_game_map == [[' [ ]', ' [δ]'], [' [ ]', ' [Ω]']]
    True
    >>> small_dictionary == {'X-Coordinate': 0, 'Y-Coordinate': 0}
    True
    >>> small_game_board == {(0, 0): 'one', (0, 1): 'two', (1, 0): 'three', (1, 1): 'four'}
    True
    >>> one_direction == '2'
    True

    # boss room use
    >>> small_dictionary = {'X-Coordinate': 1, 'Y-Coordinate': 1}
    >>> small_game_board = {(0, 0): 'one', (0, 1): 'two', (1, 0): 'three', (1, 1): 'four'}
    >>> one_direction = '1'
    >>> one_game_map = [[' [ ]', ' [ ]'], [' [ ]', ' [δ]']]
    >>> update_map(one_direction, small_dictionary, one_game_map, small_game_board)
    >>> one_game_map == [[' [ ]', ' [δ]'], [' [ ]', ' [Ω]']]
    True
    >>> small_dictionary == {'X-Coordinate': 1, 'Y-Coordinate': 1}
    True
    >>> small_game_board == {(0, 0): 'one', (0, 1): 'two', (1, 0): 'three', (1, 1): 'four'}
    True
    >>> one_direction == '1'
    True
    """
    end_goal = max(game_board)
    current_coordinates = (character['X-Coordinate'], character['Y-Coordinate'])
    future_coordinates = coordinate_maker(direction, character)

    if current_coordinates == end_goal:
        game_map[-1][-1] = ' [Ω]'
        game_map[future_coordinates[1]][future_coordinates[0]] = ' [δ]'

    elif len(game_board[current_coordinates]) == 3:
        game_map[future_coordinates[1]][future_coordinates[0]] = ' [δ]'
        game_map[character['Y-Coordinate']][character['X-Coordinate']] = ' [¿]'

    else:
        game_map[future_coordinates[1]][future_coordinates[0]] = ' [δ]'
        game_map[character['Y-Coordinate']][character['X-Coordinate']] = ' [ ]'


def print_map(game_map: list) -> None:
    """
    Display map for User.

    :param game_map: a list
    :pre-condition: game_map must be a 2D list of board rooms ('[ ]')
    :post-condition: formatted game_map is printed out to user
    :return: None
    """
    for row in game_map:
        print()
        for cell in row:
            print(cell, end='')
    print()


# ---------------------------------------------------------------------------------- #
# ---------- ---------- ---------- User Name System ---------- ---------- ---------- #
# ---------------------------------------------------------------------------------- #
def get_user_name() -> str:
    """
    Get adventurer's preferred name.

    :parameter: None
    :pre-condition: None
    :post-condition: creates a string containing the user's preferred name
    :return: a string
    """
    print("You gather your senses slowly. A bump to the head has made you groggy, but your memory slowly returns. "
          "\nWhat is your name?")

    while True:
        user_name = input().title()

        if not user_name or not user_name.isalpha():
            print("\nStill struggling with your memory? Please try again, adventurer..."
                  "\n(Please use alpha characters only)\n")
        elif user_name in ['Q', 'Quit']:
            end_game()
        else:
            return user_name


# ------------------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Character Creation System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------------------- #
def class_information(help_choice: str, user_name: str) -> None:
    """
    Provide class information to user.

    :param help_choice: a string
    :param user_name: a string
    :pre-condition: help_choice must be a string in 'help' format - e.g. "H1"
    :pre-condition: character_name must be a string
    :post_condition: printed output describing a chosen character class; parameters are unchanged by this function
    :return: None
    """
    class_describe = {
        "Scout": ("Light armour, light weapons, and light on their feet, scouts use their stealth to "
                  "deal heavy damage in battle.\nMid-range HP points coupled with a consistent damage output "
                  "make them a reliable choice for combat."),
        "Berserker": ("This class exudes power. Berserkers are trained to ignore pain, so their Health Points "
                      "are the highest of\nthe classes, but their recklessness comes at a cost. Attacks, while "
                      "powerful, are more inconsistent.\n"),
        "Warlock": ("Able to manipulate orelight to suit their purposes. Not one for hand-to-hand combat, but "
                    "their magic packs\none hell of a punch. Stay clear of their Ild Beams. That stuff will "
                    "melt Admantium. \n\nOverall, they have high, but inconsistent, damage output "
                    "counterbalanced with low Health Points.\n"),
        "Archer": ("A master of projectiles. They wear lighter armour to stay mobile so their"
                   " Health Points are only\nslightly higher than sorcerers. A well placed arrow "
                   "or throwing knife is hard to dodge, and can do large\namounts of damage consistently. "
                   "\n\nMore experienced archers are some of the deadliest Jagrs.\n")
    }

    # Create bridge between user input and class descriptions
    help_dictionary = {'H' + str(number): value for number, value in enumerate(class_describe, 1)}

    print(f"Ah, a {help_dictionary[help_choice]} eh {user_name}? Here you go:\n")
    print('{:*^110}'.format(help_dictionary[help_choice]))
    print(class_describe[help_dictionary[help_choice]])


def get_class_choice(user_name: str) -> str:
    """
    Determine user's character class.

    :param user_name: a string
    :pre-condition: character_name must be a string
    :post-condition: a string representing the user's character class
    :post-condition: user_name is unchanged by this function
    :return: a string in class format
    """
    class_list = ["Scout", "Berserker", "Warlock", "Archer"]

    while True:
        print(f"\nOkay, {user_name}, now let's see if you can remember anything else...\n"
              "What class are you? (Please enter 1, 2, 3, 4, or 'H'+number (h1) for more information)")

        format_list_output(class_list)
        class_choice = input().title()

        if class_choice in ['Q', 'Quit']:
            end_game()

        elif class_choice in ['H1', 'H2', 'H3', 'H4']:
            class_information(class_choice, user_name)

        elif not class_choice.isnumeric() or class_choice not in ['1', '2', '3', '4']:
            print("\nStill groggy, are we? Please enter a number between 1 and 4 or 'h' plus the "
                  "class number for more information. (e.g. 'h1' for Scout info.)\n")

        else:
            user_class = class_list[int(class_choice) - 1]
            print(f"\nAh, yes, {user_name} the {user_class}. One of the mighty Avgrunjagrs.\n"
                  f"Welcome back to the land of the living.")

            return user_class


def class_storage(user_class: str, user_name: str) -> dict:
    """
    Store the classes used for character dictionaries.

    :param user_class: a string
    :param user_name: a string
    :pre-condition: user_class must be a string representing one of the four available classes
    :pre-condition: user_name must be a string in user name format
    :post-condition: a dictionary in character format, with key-value pairs representing user and class
                     attributes
    :post-condition: arguments are unchanged by this function
    :return: a character dictionary

    # Standard use
    >>> class_choice = 'Scout'
    >>> name = "Bob"
    >>> new_player = class_storage(class_choice, name)
    >>> new_player['Name'] == 'Bob'
    True
    >>> len(new_player)
    13
    >>> class_choice == 'Scout'
    True
    >>> name == "Bob"
    True
    """
    class_dictionary = {
        "Scout": {
            'X-Coordinate': 0,
            'Y-Coordinate': 0,
            'Name': '',
            'Max HP': 85,
            'HP': 85,
            'Attacks': [
                ['Sneak Attack', [10, 35]],  # reset this - changed for debugging
                ['Garrote', [5, 25]],
                ['Dwarven Nerve Pinch', [13, 22]],
                ['Flee', [0, 0]],
            ],
            'Equipped': {
                'Head': None,
                'Hand': None,
                'Neck': None,
                },
            'Inventory': ['Stale Bread'],
            'Level': 1,
            'XP': 0,
            'Prayer': 0,
            'Future Levels': [(2, 150), (3, 350)],
            'Rank': 'Novice',
        },
        "Berserker": {
            'X-Coordinate': 0,
            'Y-Coordinate': 0,
            'Name': '',
            'Max HP': 100,
            'HP': 100,
            'Attacks': [
                ['Whirlwind', [2, 50]],
                ['Fury', [10, 25]],
                ['Kick', [8, 27]],
                ['Flee', [0, 0]],
            ],
            'Equipped': {
                'Head': None,
                'Hand': None,
                'Neck': None,
                },
            'Inventory': ['Stale Bread'],
            'Level': 1,
            'XP': 0,
            'Prayer': 0,
            'Future Levels': [(2, 150), (3, 350)],
            'Rank': 'Novice',
        },
        "Warlock": {
            'X-Coordinate': 0,
            'Y-Coordinate': 0,
            'Name': '',
            'Max HP': 70,
            'HP': 70,
            'Attacks': [
                ['Concussive Blast', [5, 42]],
                ['Call of the Void', [15, 27]],
                ['Ild Beam', [22, 30]],
                ['Flee', [0, 0]],
            ],
            'Equipped': {
                'Head': None,
                'Hand': None,
                'Neck': None,
            },
            'Inventory': ['Stale Bread'],
            'Level': 1,
            'XP': 0,
            'Prayer': 0,
            'Future Levels': [(2, 150), (3, 350)],
            'Rank': 'Novice',
            },
        "Archer": {
            'X-Coordinate': 0,
            'Y-Coordinate': 0,
            'Name': '',
            'Max HP': 80,
            'HP': 80,
            'Attacks': [
                ['Broadhead Arrow', [5, 24]],
                ['Trap', [9, 20]],
                ['Throwing Knife', [27, 28]],
                ['Flee', [0, 0]],
            ],
            'Equipped': {
                'Head': None,
                'Hand': None,
                'Neck': None,
                },
            'Inventory': ['Stale Bread'],
            'Level': 1,
            'XP': 0,
            'Prayer': 0,
            'Future Levels': [(2, 150), (3, 350)],
            'Rank': 'Novice',
        },
    }

    # Add user's name to chosen class
    user_dictionary = class_dictionary[user_class]
    user_dictionary['Name'] = user_name

    return user_dictionary


def make_character(user_name: str) -> dict:
    """
    Generate user's character.

    :param user_name: a string
    :pre-condition: character_name must be a string
    :post-condition: a dictionary in character format containing the user's character information
    :return: a dictionary in character format
    """
    user_class = get_class_choice(user_name)
    return class_storage(user_class, user_name)


# ------------------------------------------------------------------------------------------ #
# ---------- ---------- ---------- Describe Location System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------------------ #
def describe_current_location(board: dict, character: dict) -> None:
    """
    Provide description of current board tile.

    :param board: a dictionary
    :param character: a dictionary
    :pre-condition: board must be a dictionary in game board format
    :pre-condition: character must be a dictionary in character format
    :post-condition: printed output in the form of a detailed description, but no changes to memory landscape
    :return: None
    """
    # Create dict of descriptions
    detailed_descriptions = {
        'Dark Room': ("\nThis dimly lit room is barren. You see cobwebs and scattering bugs "
                      "in your torch's light, but nothing of immediate interest.\n"),
        'Crypt': ("\nYou are surrounded by the bones of your ancestors and long-expired offerings "
                  "to Odin. \nTime has worn inscriptions away, so these dead are now nameless. "
                  "And legion. Tread with caution.\n"),
        'Treasure Room': ("\nEven in torch light you can see the glimmer of goldcrete on the walls. "
                          "This room is bound to be hiding something of value. \nAnd traps to "
                          "protect it...\n"),
        'Workshop': ("\nYou spot a workbench in the corner and tools still neatly organized in "
                     "various containers and wall mounts. \nThis room may be worth inspecting.\n"),
        'Armoury': ("\nThe flames from your torch dance across stacks of unfinished Dwerminium"
                    " breastplates.\n\nThe metal itself is worth a fortune, if only you could carry"
                    " it all. It is of no use to you in its current state.\n"),
        'Cavern': ("\nA roof collapse has destroyed whatever was unfortunate enough to have been "
                   "stored here. \nYou note that the collapse has exposed a massive cavern, "
                   "so vast that your torch does not even penetrate 5 feet beyond your eyes."
                   "\n\nYou decide against exploring the cavern any further.\n"),
        'Rest Area': ("\nYou spot an ancient konsentrerium in the corner. It looks functional, "
                      "though its effectiveness may be limited.\n"),
        'Market': ("\nEven after centuries have worn away the inscriptions, you can still see signs "
                   "of trade in this room.\nYou spot rusted coinage and molded ledgers, but nothing "
                   "of immediate interest.\n"),
        'Sewer': ("\nA scent of decay fills your nose as you step into a puddle of Odin-knows-what.\n"
                  "Even after hundreds of years, a sewer still smells like a sewer.\nGood to know.\n"),
        'Latrine': ("\nEven ancient Dwarves needed restrooms. This one looks nicer than the one in your "
                    "favourite pub, which says a lot about the pub.\n...Or maybe just your taste in pubs.\n")
    }

    location_coordinates = (character["X-Coordinate"], character["Y-Coordinate"])
    room_type = board[location_coordinates]

    print(detailed_descriptions[room_type[0]])


# --------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Movement System ---------- ---------- ---------- #
# --------------------------------------------------------------------------------- #
def print_directions(character: dict) -> None:
    """
    Print the direction input prompt.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: no changes in memory landscape aside from print output
    :return: None
    """
    full_directions = ['North', 'East', 'South', 'West', 'Action']

    print(f"\nPlease enter the direction you wish to travel, {character['Name']} or take further action. ('q' to quit)")
    format_list_output(full_directions)


def get_user_action(character: dict, board: dict) -> str:
    """
    Determine User's desired direction of travel or additional desired Actions.

    :param character: a dictionary
    :param board: a dictionary
    :pre-condition: board must be a dictionary in board format
    :pre-condition: character must be a dictionary in character format
    :post-condition: the user's direction of choice is stored as a string in movement_direction
    :post-condition: additional actions done via additional_actions() may change the memory landscape further
    :return: a string representing the direction the User wishes to travel in
    """
    while True:
        print_directions(character)
        movement_direction = input().upper()

        if movement_direction in ['Q', 'QUIT']:
            end_game()

        elif movement_direction not in ['1', '2', '3', '4', '0', '5']:
            print(f"\nInvalid input. Please try again, {character['Name']}! You may enter '0' for help!\n")

        elif movement_direction == "0":
            print("\nEnter '1' for North, '2' for East, and so on. "
                  "You may enter '5' for further actions or 'Q' to quit.\n")

        elif movement_direction == "5":
            additional_actions(board, character)

        else:
            return movement_direction


def coordinate_maker(direction: str, character: dict) -> tuple:
    """
    Create cartesian coordinates in a tuple.

    :param direction: a string
    :param character: a dictionary
    :pre-condition: direction must be a single character string in ['1', '2', '3', '4']
    :pre-condition: character must be a dictionary in character format
    :post-condition: a tuple containing x, y co-ordinates in format (x, y)
    :post-condition: arguments submitted to this function are not altered
    :return: a tuple

    # Standard use
    >>> character_dictionary = {'X-Coordinate': 0, 'Y-Coordinate': 0}
    >>> one_direction = '2'
    >>> coordinate = coordinate_maker(one_direction, character_dictionary)
    >>> coordinate == (1, 0)
    True
    >>> character_dictionary == {'X-Coordinate': 0, 'Y-Coordinate': 0}
    True
    >>> one_direction == '2'
    True

    # Standard use
    >>> character_dictionary = {'X-Coordinate': 0, 'Y-Coordinate': 1}
    >>> one_direction = '1'
    >>> coordinate = coordinate_maker(one_direction, character_dictionary)
    >>> coordinate == (0, 0)
    True
    >>> character_dictionary == {'X-Coordinate': 0, 'Y-Coordinate': 1}
    True
    >>> one_direction == '1'
    True
    """
    direction_dict = {
        '1': -1,
        '2': 1,
        '3': 1,
        '4': -1,
    }

    if direction in ["1", "3"]:
        tentative_direction = (character["X-Coordinate"], character["Y-Coordinate"] + direction_dict[direction])

    else:
        tentative_direction = (character["X-Coordinate"] + direction_dict[direction], character["Y-Coordinate"])

    return tentative_direction


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Validate the User's chosen direction of travel based on their current location.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :pre-condition: board must be a dictionary in game board format
    :pre-condition: character must be a dictionary in character format
    :pre-condition: direction must be a single character string in ['1', '2', '3', '4']
    :return: True if the User's direction will keep them in bound, False if the chosen direction
             will take them out of bounds
    """
    tentative_direction = coordinate_maker(direction, character)
    boss_fight = True
    # Check if heading to boss room
    if tentative_direction == max(board):
        boss_fight = boss_room_warning()  # create warning function that returns True or False

    if boss_fight is not True:
        return False

    else:
        return tentative_direction in board


def move_character(character: dict, direction: str) -> None:
    """
    Move the User's character to their chosen board position.

    :param character: a dictionary
    :param direction: a string
    :pre-condition: character must be a dictionary in character format
    :pre-condition: direction must be a single character string in ['1', '2', '3', '4']
    :post-condition: the X and Y-Coordinate in character are updated to reflect new position in map
    :return: None

    # Standard Use - X-Axis
    >>> character_dictionary = {'X-Coordinate': 0, 'Y-Coordinate': 0}
    >>> one_direction = '2'
    >>> move_character(character_dictionary, one_direction)
    >>> character_dictionary == {'X-Coordinate': 1, 'Y-Coordinate': 0}
    True
    >>> one_direction == '2'
    True

    # Standard use - Y-Axis
    >>> character_dictionary = {'X-Coordinate': 0, 'Y-Coordinate': 0}
    >>> one_direction = '3'
    >>> move_character(character_dictionary, one_direction)
    >>> character_dictionary == {'X-Coordinate': 0, 'Y-Coordinate': 1}
    True
    >>> one_direction == '3'
    True
    """
    direction_dict = {
        '1': -1,
        '2': 1,
        '3': 1,
        '4': -1,
    }

    if direction in ['1', '3']:
        character["Y-Coordinate"] += direction_dict[direction]

    else:
        character["X-Coordinate"] += direction_dict[direction]


# ------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Health System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------- #
def is_alive(entity: dict) -> bool:
    """
    Confirm that an entity's current HP is above 0.

    :param entity: a dictionary
    :pre-condition: entity must be a dictionary in character or foe format
    :post-condition: create a boolean value representing the entity's current status (alive or dead)
    :return: True if HP is above zero, False if HP is 0 or less

    # Standard use - return True
    >>> character_dictionary = {'HP': 1}
    >>> is_alive(character_dictionary)
    True

    # Standard use - return False
    >>> character_dictionary = {'HP': -2}
    >>> is_alive(character_dictionary)
    False
    """
    return entity["HP"] > 0


def heal_items(character: dict) -> None:
    """
    Consume perishable item in inventory.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: remove items from character['Inventory'] and increase character stats if 'food' class items are
                    present - water and stale bread increase 'HP', Grundar mold increase "Max HP" by 5.
    :post-condition: if no 'food' class items are present, print output but no other change to memory landscape
    :return: None
    """
    if not character["Inventory"]:
        print("\nYou have no items in your satchel. (Any key to continue)\n")
        input()
        return
    else:
        format_list_output(character["Inventory"])

    while True:
        decision = input("\nWhich item would you like to use? (Enter '0' to return)\n")
        if decision.isnumeric() is False or int(decision) > len(character["Inventory"]):
            print(f"\nThat is not valid input, {character['Name']}."
                  f"\nEnter a number between 1 and {len(character['Inventory'])}.\n")

        elif decision == '0':
            return

        else:
            consume_healing(character["Inventory"][int(decision)-1], character)
            return


def health_check(character: dict, health_recovery: int = 10) -> None:
    """
    Regenerate character health up to a maximum of character['Max HP'].

    :param character: a dictionary
    :param health_recovery: an integer
    :pre-condition: character must be a dictionary in character format
    :pre-condition: health_recovery must be a positive integer equal to or larger than 10
    :post-condition: character["HP"] value increased by health_recovery up to character["max HP"]
    :return: None

    # Standard use - near max health
    >>> character_dictionary = {'HP': 439, 'Max HP': 440}
    >>> health_check(character=character_dictionary)  # default 10 health recovery
    >>> character_dictionary == {'HP': 440, 'Max HP': 440}
    True

    # Standard use - almost dead
    >>> character_dictionary = {'HP': 10, 'Max HP': 440}
    >>> health_check(character=character_dictionary)  # default 10 health recovery
    >>> character_dictionary == {'HP': 20, 'Max HP': 440}
    True
    """
    if character['HP'] > character['Max HP'] - health_recovery:
        character['HP'] = character['Max HP']
    else:
        character['HP'] += health_recovery


def turn_based_heal(character: dict) -> None:
    """
    Heal user upon entering a room.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: character["HP"] will increase by 10 or more, capped by character["Max HP"] Value
    :post-condition: print output informing user of health increase
    :return: None
    """
    if "Amulet of the First Flame" in character["Equipped"]:
        recovery = 15
    else:
        recovery = 10

    print("\nThe passage of time heals all wounds. Even some of yours."
          f"\nYou have recovered some HP.")

    health_check(character, recovery)


def consume_healing(consumable: str, character: dict) -> None:
    """
    Use consumable to increase or replenish stats.

    :param consumable: a string
    :param character: a dictionary
    :pre-condition: consumable must be a string from the list associated with character["Inventory]
    :pre-condition: character must be a dictionary in character format
    :post-condition: character["HP"] or character["Max HP"] increased depending on consumable used
                     the consumable is deleted from the list stored at character["Inventory"]
    :return: None
    """
    # Need code to cap health regen at max health (e.g. if health > max health, health == max health
    if consumable in ['Stale Bread', 'Water'] and character['HP'] == character['Max HP']:
        print(f"\nYou are already at full health, {character['Name']}. Do not waste your supplies.\n")

    elif consumable in ['Stale Bread', 'Water']:
        health_check(character=character)
        character["Inventory"].remove(consumable)
        print(f"\nYou feel more rested and energetic after some {consumable}."
              f"\nYour health is now {character['HP']}, {character['Name']}.")

    elif consumable not in ['Stale Bread', 'Water', 'Grundar Mold']:
        print(f"{character['Name']}...Are...Are you okay? That's uh...You should probably try wearing that instead...")

    else:
        character["HP"] += 5
        character["Max HP"] += 5
        character["Inventory"].remove(consumable)
        print(f"\nThe {consumable} tastes revolting, but invigorates your body and mind."
              f"\nYou gain a permanent increase of 5 HP and are healed 5HP."
              f"\nYour max health is now {character['Max HP']}, {character['Name']}.")


def meditate(board: dict, character: dict) -> None:
    """
    Allow additional HP regeneration if in Rest Area.

    :param character: a dictionary
    :param board: a dictionary
    :pre-condition: character must be a dictionary in character format
    :pre-condition: board must be a dictionary in game board format
    :post-condition: increase character["HP"] once per visit to room
    :post-condition: add 1 to character["Prayer"] per meditation
    :return: None
    """
    current_room = character_coordinate(character)
    if board[current_room][0] != 'Rest Area':
        print(f"\nThis is no place to meditate, {character['Name']}. You must keep moving...")

    elif character['Prayer'] > 0:
        print(f"\nYou have already stayed here too long, {character['Name']}. You must keep moving!")

    else:
        # health recovery increases with level
        recovery = character['Level'] * 10
        health_check(character=character, health_recovery=recovery)
        print(f"\nYou focus on your clan's ancestors and hear their calls to you, {character['Name']}."
              f"\nYou feel invigorated. Your health is now {character['HP']}")
        character['Prayer'] += 1


def current_status(character: dict, foe: dict = None) -> None:
    """
    Print output of character and enemy status neatly.

    :param character: a dictionary
    :param foe: a dictionary
    :pre-condition: character must be a dictionary in character format
    :pre-condition: foe must be a dictionary in foe or boss format
    :post-condition: neatly printed output, no other changes to memory landscape
    :return: None
    """
    if foe is None:
        print(f"HP: {character['HP']}\t\tMax HP: {character['Max HP']}\t\tLevel: {character['Level']}"
              f"\t\tXP: {character['XP']}")

    else:
        print(f"Your HP: {character['HP']}\t\t\t\t{foe['Name']} HP: {foe['HP']}")


# -------------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Foe Selection System ---------- ---------- ---------- #
# -------------------------------------------------------------------------------------- #
def types_of_foes(character: dict) -> dict:
    """
    Retrieve dictionary of level appropriate foes for combat system.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: return a dictionary based on the value of character["Level"]
    :return: a dictionary of foes associated with the level of the user
    """
    foe_dictionary = {
        # Level One Foes
        1: {
            0: {
                'Name': 'Cave Spider',
                'HP': 40,  # Was 60 - too high
                'Damage': [1, 18],
                'XP': 30,
            },
            1: {
                'Name': 'Elemental',
                'HP': 60,  # Was 80 - too high
                'Damage': [1, 20],
                'XP': 30,
            },
            2: {
                'Name': 'Sewer Rat',
                'HP': 40,  # Was 60 - too high
                'Damage': [1, 15],
                'XP': 25,
            }
        },
        # Level Two Foes
        2: {
            0: {
                'Name': 'Crypt Warden',
                'HP': 100,  # Was 150 - too high
                'Damage': [8, 20],
                'XP': 35,
            },
            1: {
                'Name': 'Draugr',
                'HP': 85,  # Was 125 - too high
                'Damage': [9, 20],
                'XP': 35,
            },
            2: {
                'Name': 'Banshee',
                'HP': 70,  # Was 80 - too high
                'Damage': [5, 20],
                'XP': 35,
            }
        },
        # Level Three Foes
        3: {
            0: {
                'Name': 'Afflicted Crypt Warden',
                'HP': 130,  # was 210 - too high
                'Damage': [12, 25],
                'Inventory': 'Grundar Mold',
            },
            1: {
                'Name': 'Afflicted Dwarf',
                'HP': 125,  # was 200 - too high
                'Damage': [13, 25],
                'Inventory': 'Grundar Mold',
            },
            2: {
                'Name': 'Afflicted Elemental',
                'HP': 130,  # was 220 - too high
                'Damage': [5, 25],
                'Inventory': 'Stale Bread'
            },
        }
    }
    # return dictionary based on character level
    return foe_dictionary[character['Level']]


def foe_selector(character: dict, board: dict) -> dict:
    """
    Determine type of foe based on character stats and location.

    :param character: a dictionary
    :param board: a dictionary
    :pre-condition: character must be a dictionary in character form
    :pre-condition: board must be a dictionary in game board form
    :post-condition: a foe-format dictionary is selected at random or by room description
    :return: a dictionary
    """
    potential_foes = types_of_foes(character)
    room = board[character['X-Coordinate'], character['Y-Coordinate']][0]

    if room in ['Sewer', 'Latrine']:
        print(f"\nA {potential_foes[2]['Name']} approaches! Prepare for battle, {character['Name']}!"
              f"(Press enter to continue)")
        input()
        return potential_foes[2]

    elif room in ['Armoury', 'Crypt']:
        print(f"\nA {potential_foes[0]['Name']} approaches! Prepare for battle, {character['Name']}!"
              f"(Press enter to continue)")
        input()
        return potential_foes[0]

    else:
        random_foe = potential_foes[random.randint(0, 2)]
        print(f"\nA {random_foe['Name']} approaches! Prepare for battle, {character['Name']}!"
              f"(Press enter to continue)")
        input()
        return random_foe


# ------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Combat System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------- #
def check_for_foes() -> int:
    """
    Determine if User will encounter a foe in the current room.

    :param: None
    :pre-condition: None
    :post-condition: Creates and immediately returns a boolean value depending on the random number generated
    :return: True if a foe is present, False if no foe is present
    """
    return random.randint(1, 100) <= 30  # Increase from 20 to 30 - combat necessary to progress in game.


def flee(character: dict, current_foe: dict, foe: bool = False) -> bool:
    """
    Return True if user or foe decides to flee
    :param character: a dictionary
    :param current_foe: a dictionary
    :param foe: a boolean
    :pre-condition: character must be a dictionary in character format
    :pre-condition: current_foe must be a dictionary in foe format
    :pre-condition: foe must be a boolean value
    :post-condition: if foe is false the function returns True. If a random number is between 1 and 20 (inclusive)
                    the foe will attack the player causing a change in the character["HP"] value
    :post-condition: if foe is True, 20% chance that function returns True, else False
    :return: True or False
    """
    if foe is True:
        return random.randint(1, 100) <= 20

    elif foe is False and random.randint(1, 100) <= 20:
        print(f"\nIn your rush to escape you drop your guard, {character['Name']}! The {current_foe['Name']}"
              f" takes one last swipe at you...\n")
        foe_attack(current_foe, character)

    else:
        print("\nYou manage to escape without any damage!\n")

    return True


def foe_attack(foe: dict, character: dict) -> None:
    """
    Determine the amount of damage done to user's character.

    :param foe: a dictionary
    :param character: a dictionary
    :pre-condition: current_foe must be a dictionary in foe format
    :pre-condition: character must be a dictionary in character format
    :post-condition: character['HP'] is reduced by a random number in range of foe["Damage"] values
    :return: None
    """
    damage = random.randint(foe["Damage"][0], foe["Damage"][1])

    print(f"\nThe {foe['Name']} does {damage} damage against you, {character['Name']}!!")

    character["HP"] -= damage


def user_attack(character: dict, foe: dict, attack: str) -> bool:
    """
    Determine the amount of damage, if any, done to Foe.

    :param character: a dictionary
    :param foe: a dictionary
    :param attack: a string
    :pre-condition: character must be a dictionary in character format
    :pre-condition: foe must be a dictionary in for format
    :pre-condition: attack must be a string representing an integer between 1 and 3
    :post-condition: foe's HP is decreased by a random number in range of the character's chosen attack value
    :return: False if the user chose to attack, or True (the return of flee()) if the user chose to run
    """
    if attack == '4':
        return flee(character=character, current_foe=foe)

    else:
        damage = random.randint(character["Attacks"][int(attack) - 1][1][0],
                                character["Attacks"][int(attack) - 1][1][1])

        print(f"\nYour {character['Attacks'][int(attack) - 1][0]} does {damage} damage to the {foe['Name']}!!"
              f"\n(Enter to continue...)")
        input()

        foe["HP"] -= damage

    return False


def user_combat_options(character: dict) -> str:
    """
    Get user's choice of actions.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character form
    :post-condition: a string is created representing the user's choice of action in the combat cycle
    :return: the user's choice in string format
    """
    print("\nWhich do you want to attack with?")

    format_list_output(character['Attacks'])
    return input()


def turn_base_combat(character: dict, board: dict) -> None:
    """
    Operate turn-based combat mechanism.

    :param character: a dictionary
    :param board: a dictionary
    :pre-condition: character must be a dictionary in character format
    :pre-condition: board must be a dictionary in board format
    :post-condition: if user 'HP' reaches 0, the game ends
    :post-condition: if the foe flees, the character['XP'] increases by half of foe['XP'] value
    :post-condition: if foe 'HP' reaches 0, character['XP'] increases by foe['XP'] and combat ends
    :return: None
    """
    # Set main variables
    current_foe = foe_selector(character, board)
    strategic_retreat = False
    cowardly_foe = False

    # Start Combat Loop - if foe is alive, user is alive, foe hasn't run (like a coward), and user hasn't
    # made the prudent decision to strategically retreat
    while is_alive(current_foe) and is_alive(character) and not cowardly_foe and not strategic_retreat:
        # Show health status
        current_status(character, current_foe)
        # User always gets first attack
        attack_choice = user_combat_options(character)

        if attack_choice not in ['1', '2', '3', '4']:
            print("\nInvalid input! Please enter a number between '1' and '4'.")
            # Don't run anything else if the input is invalid
            continue

        else:
            strategic_retreat = user_attack(character, current_foe, attack_choice)

        # Foe is able to attack and run (like a true coward)
        if is_alive(current_foe) and not strategic_retreat:
            foe_attack(current_foe, character)

        if is_alive(character) and not strategic_retreat and is_alive(current_foe):
            cowardly_foe = flee(character, current_foe, True)

    if is_alive(character):
        experience_points(character, current_foe, strategic_retreat, cowardly_foe)


# ----------------------------------------------------------------------------- #
# ---------- ---------- ----------  XP System  ---------- ---------- ---------- #
# ----------------------------------------------------------------------------- #
def experience_points(character: dict, foe: dict, strategic_retreat: bool, cowardly_foe: bool) -> None:
    """
    Add Experience Points to Character based on combat outcome.

    :param character: a dictionary
    :param foe: a dictionary
    :param strategic_retreat: a boolean
    :param cowardly_foe: a boolean
    :pre-condition: character must be a dictionary in character format
    :pre-condition: foe must be a dictionary in foe format
    :pre-condition: strategic_retreat must be a boolean
    :pre-condition: cowardly_foe must be a boolean
    :post-condition: the character['XP'] may be increased depending on the outcome of the combat loop
    :return: None
    """
    if strategic_retreat:
        print(f"\nNo XP for running, even if it's the right call, {character['Name']}!")

    elif cowardly_foe and character['Level'] < 3:
        print(f"The {foe['Name']} flees in terror of your might, {character['Name']}!"
              f"\nYou gain {foe['XP'] / 2} Experience Points!")
        character["XP"] += foe["XP"] / 2

    elif cowardly_foe and character['Level'] == 3:
        print(f"The {foe['Name']} flees in terror of your might, {character['Name']}!")

    elif foe["HP"] <= 0 and character['Level'] < 3:
        print(f"You have defeated the {foe['Name']}!"
              f"\nYou gain {foe['XP']} Experience Points!")
        character["XP"] += foe["XP"]

    elif foe["HP"] <= 0 and character['Level'] == 3:
        print(f"You have defeated the {foe['Name']}! You bask in the glory of your might.")


def attribute_boost(character: dict, minimum_attack: int = 4, maximum_attack: int = 5, special: bool = False) -> None:
    """
    Increase user's attributes.

    :param character: a dictionary
    :param minimum_attack: an integer
    :param maximum_attack: an integer
    :param special: a boolean
    :pre-condition: character must be a dictionary in character format
    :pre-condition: minimum_attack must be a positive integer
    :pre-condition: maximum_attack must be a positive integer
    :pre-condition: special_gear is False if function is called for level increase, True if special gear equipped
    :post-condition: values within 'HP', 'Attack' keys in character will be increased
    :return: None
    """
    # Increase minimum and maximum damage
    for number, attack in enumerate(character['Attacks']):
        # Flee has no min/max damage
        if attack[0] != 'Flee':
            attack[1][0] += minimum_attack  # minimum
            attack[1][1] += maximum_attack  # maximum

    if special is True:
        return

    # Increase health
    character['HP'] += 25
    character['Max HP'] += 25


def check_level(character: dict) -> None:
    """
    Determine if player has achieved new level.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: function may call increase_leve() which will impact several values of character dictionary
    :return: None
    """
    # Do nothing if max level attained
    if character["Level"] == 3:
        return

    # Current XP goal (based on current level)
    required_experience = character['Future Levels'][character['Level'] - 1][1]
    rank = ["Novice", "Intermediate", "Expert"]

    if character['XP'] >= required_experience:
        attribute_boost(character=character)
        character['Level'] += 1
        character['Rank'] = rank[character['Level'] - 1]
        print(f"\nCongratulations, {character['Name']}!! You are now an {character['Rank']}."
              f"\nYour Max HP is now {character['Max HP']}"
              f"\nYour combat status have increased as well: ")
        format_list_output(character["Attacks"])


# ------------------------------------------------------------------------------- #
# ---------- ---------- ----------  Boss System  ---------- ---------- ---------- #
# ------------------------------------------------------------------------------- #
def boss_room_warning() -> bool:
    """
    Warn User about entry into Boss Room.

    :param: None
    :pre-condition: None
    :post-condition: boolean created representing the user's choice; printout into interface
    :return: True if user wants boss fight, False if not
    """
    print("A powerful enemy awaits you in this room. Do you wish to proceed? (1 - Yes, 2 - No)")

    while True:
        boss_fight = input().upper()
        if boss_fight in ['Q', 'Quit']:
            end_game()

        elif boss_fight == '1':
            return True

        elif boss_fight == '2':
            print("A wise choice...")
            return False

        else:
            print("That is not valid input. Please enter 1 for yes or 2 for no.")


def boss_creator() -> dict:
    """
    Create King Kveldulfr the Afflicted

    :param: None
    :pre-conditions: None
    :post-conditions: A dictionary in boss format
    :return: a dictionary

    # Standard Use
    >>> get_boss = boss_creator()
    >>> get_boss == {'Name': "Afflicted King", 'Damage': [15, 30], 'HP': 400,}
    True
    """
    final_boss = {
        'Name': "Afflicted King",
        'Damage': [15, 30],
        'HP': 225,
    }

    return final_boss


def boss_combat_loop(character: dict, boss: dict) -> None:
    """
    Drives the Final Boss combat mechanism.

    :param character: a dictionary
    :param boss: a dictionary
    :pre-condition: character must be a dictionary in character format
    :pre-condition: boss must be a dictionary in boss format
    :post-condition: if boss dies, game ends in victory, if character dies, game ends in defeat
    :return: None
    """
    # Start Boss Fight Loop - This is adapted from main combat loop with key changes.
    # if foe is alive, user is alive and user hasn't made a prudent decision to strategically retreat
    strategic_retreat = False

    while is_alive(boss) and is_alive(character) and not strategic_retreat:
        # Show Health Stats
        current_status(character, boss)

        attack_choice = user_combat_options(character)

        if attack_choice not in ['1', '2', '3', '4']:
            print("Invalid input!!")
            # Don't run anything else if the input is invalid
            continue

        else:
            strategic_retreat = user_attack(character, boss, attack_choice)

        if is_alive(boss) and is_alive(character) and not strategic_retreat:
            # Foe can't do anything if they are dead
            foe_attack(boss, character)

    if strategic_retreat and is_alive(character):
        print("The affliction has begun to heal the forgotten King even as you flee...")
        input()


def dead_king(boss: dict) -> bool:
    """
    Determines if goal has been achieved by user.

    :param boss: a dictionary
    :pre-condition: boss must be a dictionary in boss format
    :post-condition: a boolean, True if boss is dead, False if boss is alive
    :return: a boolean

    # Standard - boss alive
    >>> boss_example = {'HP': 400}
    >>> dead_king(boss_example)
    False

    # Standard - boss dead
    >>> boss_example = {'HP': 0}
    >>> dead_king(boss_example)
    True
    """
    return boss['HP'] <= 0


# ------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Search System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------- #
def search_room(board: dict, character: dict) -> None:
    """
    Search the current room for items and equipment.

    :param board: a dictionary
    :param character: a dictionary
    :pre-condition: board must be a dictionary in game board format
    :pre-condition: character must be a dictionary in character format
    :post-condition: items in the applicable board key are transferred to the inventory key in dictionary
    :return: None
    """
    current_room = character_coordinate(character)

    # determine if length of board value list is 3 - signifies a special item
    if len(board[current_room]) == 3:
        print("Upon searching the room, you find a special item. "
              f"Congratulations, {character['Name']}, you have located the " + board[current_room][2] + "!")
        # Add special item to inventory
        character["Inventory"].append(board[current_room].pop())

    # Separate if-else for regular items to avoid complex if-conditional
    if board[current_room][1] != "Nothing":
        print(f"Ah, upon inspection you spot something nearby, {character['Name']}. "
              "\nA " + board[current_room][1] + " has been added to your inventory.")
        character["Inventory"].append(board[current_room].pop())
        board[current_room].append("Nothing")

    else:
        print(f"Beyond what you have already seen, there is naught to find here, {character['Name']}. "
              "\nBest to move on, and quickly.")


# ---------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Inventory System ---------- ---------- ---------- #
# ---------------------------------------------------------------------------------- #
def special_item_finder(inventory_item: str) -> bool:
    """
    Return True if an inventory item is special.

    :param inventory_item: a string
    :pre-condition: inventory_item must be an item from an inventory list in a character dictionary; it must be a string
    :post-condition: creates a boolean representing the status of the item as special or not
    :return: True if an item is special, False if not

    # Standard use
    >>> true_inventory = 'Ring of Relvdrun'
    >>> special_item_finder(true_inventory)
    True

    # Standard use
    >>> false_inventory = 'apple'
    >>> special_item_finder(false_inventory)
    False
    """
    return inventory_item in ["Ring of Relvdrun", "Helm of the Deep", "Amulet of the First Flame"]


def view_inventory(character: dict) -> None:
    """
    Allow user to view their inventory items.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in game board format
    :post-condition: print output of inventory contents, but no changes to memory landscape
    :return: None
    """
    print("\nYour satchel contains the following items: ")
    format_list_output(character["Inventory"])

    # Look! I used filter!
    special_items = list(filter(special_item_finder, character["Inventory"]))

    if len(special_items) != 0:
        print(f"It appears you have found treasure in your journey so far, {character['Name']}.")
        format_list_output(special_items)


def wear_special_gear(wearable: str, character: dict):
    """
    Equip a special item.

    :param character: a dictionary
    :param wearable: a string
    :pre-condition: character must be a dictionary in character format
    :pre-condition: wearable must be a string in the special_items list
    :post-condition: wearable is removed from inventory list, added to equipped sub-dictionary in character
    :return: None
    """
    print(f"You feel a surge of power course through your veins as the {wearable}"
          f" binds itself to you, {character['Name']}")

    if "Helm" in wearable:
        print("Your HP permanently increases by 30")
        character['Max HP'] += 30
        character["HP"] += 30
        character["Equipped"]["Head"] = character["Inventory"].pop(character["Inventory"].index(wearable))

    elif "Ring" in wearable:
        print("Your minimum attack permanently increases by 7 and maximum attack by 2.")
        attribute_boost(character, 7, 2, True)
        character["Equipped"]["Hand"] = character["Inventory"].pop(character["Inventory"].index(wearable))

    else:
        print("Your minimum attack permanently increases by 2 and maximum attack by 8.")
        attribute_boost(character, 2, 8, True)
        character["Equipped"]["Neck"] = character["Inventory"].pop(character["Inventory"].index(wearable))


def equip_item(character: dict) -> None:
    """
    Allow user to access and wear items in their inventory.

    :param character: a dictionary
    :pre-condition: character must be a dictionary in character format
    :post-condition: one or more items may be deleted from character["Inventory"]
    :post-condition: one or more items may be added to character["Equipped"]
    :return: None
    """
    special_items = list(filter(special_item_finder, character["Inventory"]))

    if special_items:
        format_list_output(special_items)
        print(f"Which item would you like to use, {character['Name']}?")

    else:
        print(f"You have no equippable items in your inventory, {character['Name']}.")
        return

    while True:
        decision = input()
        if decision == '0' or decision.isnumeric() is False or int(decision) > len(special_items):
            print(f"That is not valid input, {character['Name']}. Enter a number between 1 and {len(special_items)}.")

        else:
            wear_special_gear(special_items[int(decision) - 1], character)
            return


# ------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Choice System ---------- ---------- ---------- #
# ------------------------------------------------------------------------------- #
def additional_actions(board: dict, character: dict) -> None:
    """
    Determine user's course of action.

    :param board: a dictionary
    :param character: a dictionary
    :pre-condition: user_name must be a string
    :pre-condition: board must be a dictionary in game board format
    :pre-condition: character must be a dictionary in character format
    :post-condition: the Character dictionary will be impacted based on which, if any, helper functions are called
    :return: None
    """
    helper_list = [view_inventory,
                   equip_item,
                   heal_items,
                   meditate,
                   search_room,
                   lore,
                   tutorial,
                   faux_information,
                   ['Return',
                    'View Inventory',
                    'Equip item',
                    'Heal',
                    'Meditate',
                    'Search',
                    'Lore',
                    'Tutorial',
                    'Foe Information'],
                   ]

    while True:
        print("\nWhat do you wish to do?")
        format_list_output(helper_list[-1])
        decision = input().upper()

        if decision in ['2', '3', '4']:
            helper_list[int(decision) - 2](character)

        elif decision in ['5', '6']:
            helper_list[int(decision) - 2](board, character)

        elif decision in ['7', '8', '9']:
            helper_list[int(decision) - 2]()

        elif decision == '1':
            return

        else:
            print(f"\nThat is not valid input, {character['Name']}.\n")


# -------------------------------------------------------------------------------- #
# ---------- ---------- ---------- Main Game Loop ---------- ---------- ---------- #
# -------------------------------------------------------------------------------- #
def game():
    """
    Run the game.
    """
    # Intro
    welcome_to_game()

    # Get user's preferred name
    user_name = get_user_name()

    # Standard map size is 25x25
    rows = 25
    columns = 25

    # Initialize board and special items
    board = make_board(rows, columns)
    special_item_maker(board)
    game_map = make_map(board)

    # Initialize User Character
    character = make_character(user_name)
    achieved_goal = False

    # Initialize Boss
    afflicted_king = boss_creator()

    while not achieved_goal and is_alive(character):
        # Reset user's prayer level
        character["Prayer"] = 0

        # Tell the User where they are and what their stats are
        current_status(character=character)
        print_map(game_map)
        describe_current_location(board, character)

        # Get direction of choice - allow for additional actions within get_user_action
        direction = get_user_action(character, board)
        valid_move = validate_move(board, character, direction)

        if valid_move:
            # Re-populate items on board randomly + move around
            random_item_maker(board)
            update_map(direction, character, game_map, board)
            move_character(character, direction)

            # Heal character based on room movement
            turn_based_heal(character)

            # Heal boss if user runs from fight
            afflicted_king['HP'] = 225

            describe_current_location(board, character)

            # Pre-set challenger setting for following conditional
            there_is_a_challenger = False

            # Combat conditionals
            if character_coordinate(character) != max(board):
                there_is_a_challenger = check_for_foes()

            else:
                boss_combat_loop(character, afflicted_king)

            achieved_goal = dead_king(afflicted_king)

            if there_is_a_challenger:
                turn_base_combat(character, board)

            elif is_alive(character) and character_coordinate(character) != max(board):
                print("There do not appear to be any foes in this room. (Enter to continue)\n")
                input()

            check_level(character)

        else:
            wrong_direction(character, board, direction)

    # Print end of game stuff e.g. congrats or "you died"
    if character["HP"] <= 0:
        # Print "you are dead" message
        end_game(dead=True)

    else:
        end_game(winner=True)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
