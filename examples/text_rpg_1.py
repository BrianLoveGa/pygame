# https://www.youtube.com/watch?v=xHPmXArK6Tg&t=46s
# python text rpg. based on youtube tutorial Bryan Tong

# AND youtube tutorial Vincent Gizzarelli
# https://www.youtube.com/watch?v=VXVCDHSzy6k

# adapted and modified By: Brian Loveless


####### WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#######
#######
#######                         WARRIOR ADVENTURE GAME
#######
#######
#######                         By: B _-_ Love -- (C) Nov 2019
#######
#######
####### <><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# imports if stand-alone python fikle
import cmd
import textwrap
import sys
import os
import time
import random

# for game

screen_width = 200

# basic start player setup


class player:
    def __init__(self):
        self.name = '';
        self.maxhealth = 100;
        self.position = 'b2';
        self.game_over = False;
        self.solves = 0;
        self.attack=10;
        self.health = self.maxhealth;
        #self.magic = 0
        #self.special = '';
        #self.spatck = 15;

# create basic player 


myPlayer = player();

# title screen


def title_screen_selections():
    option = input("> ")
    if option.lower() in  ["play", "new", "begin"]:
        set_up_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() in ["quit", "exit", "stop", "back","/q", "q"]:
        sys.exit()
    elif option.lower() == ("load"):
        load_game()
        pass
    while option.lower() not in ['play', 'help', 'quit', 'load']:
        print(" please enter a valid command .. play, help, load or quit")
        option = input("> ")
        if option.lower() == ("play"):
            set_up_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() in ["quit", "exit", "stop", "back","/q", "q"]:
            sys.exit()
        elif option.lower() == ("load"):
            load_game()
            pass


def title_screen():
    os.system('clear')
    print()
    print('##########################################')
    print('##########################################')
    print("#      Welcome to Brians text RPG game   #")
    print('##########################################')
    print('#                                        #')
    print('#       Warrior Adventure Game           #')
    print('#                                        #')
    print('##########################################')
    print()
    print(' start new with _-_ Play _-_              ')
    print('            _-_ Help _-_                  ')
    print('            _-_ Quit _-_                  ')
    print('            _-_ Load _-_                  ')
    print()
    print('#                                        #')
    print('#                                        #')
    print('#                                        #')
    print('#                                        #')
    print()
    print('         copyright 2019 B-Love            ')
    print()
    title_screen_selections()


def help_menu():
    os.system('clear')
    print('!#################################################!')
    print('!                  --> HELP <--                   !')
    print('!#################################################!')
    print('!#        Welcome to Brians text RPG game        #!')
    print('!#################################################!')
    print()
    print('!        start a new game with play command       !')
    print('!                type play                        !')
    print('!                                                 !')
    print('!      or you can load a game just type load      !')
    print('!                                                 !')
    print('!        quit stops the game                      !')
    print('!#################################################!')
    print('!             in game play ...                    !')
    print('!                                                 !')
    print('!      -- Use up, down, left, right to move       !')
    print('!       -- or north, south, east, west            !')
    print()
    print('!       -- just type your commands                !')
    print('!        -- to do them                            !')
    print()
    print('!       -- use "look" to inspect something        !')
    print('!     -- use "attack" to .. well... attack        !')
    print('!                                                 !')
    print('!         read along, fight, solve riddles        !')
    print('!            simple text game                     !')
    print('!      save the town kill the dragon              !')
    print('!      -- Good luck brave warrior                 !')
    print('!#################################################!')
    title_screen_selections()


# game map   ---  player start @ b2
#
##       can move from square to square 
#           board does not edge wrap ie no going from a1 to e1 or b1 to b5 
#  ... from a1 you can go to a2 or b1 .... from a2  ... a1, a3, or b2 ..
#      the x+ 'walls' are edge of map
##     the --- or | 'walls' can be moved through
#      the X 'walls' interior are no pass - those squares don't connect
#      just pretend ... it's a game .....
#      the only way to get to cave is from sc hills
#      0--0--0-- 'walls' need to be unlocked to enter
#
#
#       a1           a2        a3         a4         a5
#  +|+x+x+xx+x+|+x+x+xx+x+|+x+x+xx+x+|+x+x+xx+x+|+x+x+xx+x+|+
#  x|          |          |          |          |          |x
#  +|  town    |   town   |   town   | town     | town     |+
#  x|factory   |  enter   |  hall    | square   | shops    |x 
#  +|          |          |          |          |          |+                  a5
#  -|----------|----------|----------|----------|----------|-
#  x|          |          |          |          |          |x
#  +|  woods   |          |   woods  |     1    |     2    |+
#  x|    w     |  start   |     e    |   forest |  forest  |x                     b5
#  +|          |          |          |          |          |+
#  -|----------|----------|----------|----------|xxxxxxxxxx|-
#  x|          |          |          |          x          |x
#  +|          |          |     n    |     n    x     x    |+
#  x| beach    |  swamp1  |   hill   |  valley  x    cave  |x                      c5
#  +|          |          |          |          x          |+
#  -|----------|----------|----------|----------|--o--o--o-|-
#  x|          |          |          |          |          |x
#  +|          | swamp 2  |     s    |     s    |   s c    |+
#  x|  marsh   |          |   hill   |   valley |   hills  |x                    d5
#  +|          |          |          |          |          |+
#  -|----------|----------|----------|xxxxxxxxxx|xxxxxxxxxx|-
#  x|          |          |          |          o          |x
#  +| castle   |  castle  |  castle  o castle   | castle   |+
#  x|  gate    | entrance |  guard   | hall     o throne   |x                    e5
#  +|          |          |  room    o          | room     |+
#  x|          |          |          |          o          |x
#  _|+x+x+xx+x+|+x+x+xx+x+|+x+x+xx+x+|+x+x+xx+x+|+x+x+xx+x+|_
#
#
#


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': True, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                 'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False,
                 }


zonemap = {
    'a1': {
        ZONENAME: "Town factory",
        DESCRIPTION: 'Where they make the sauce',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'b1',
        LEFT: 'x',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a5',
    },
    'a5': {
        ZONENAME: "Town Shops",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: 'x',
    },
    'b1': {
        ZONENAME: "west woods",
        DESCRIPTION: 'a few shabby trees',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: 'x',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "Home start base",
        DESCRIPTION: 'This is your home - starting point',
        EXAMINATION: 'it\'s a nice place, but not great let\'s get out and go explore maybe the town up north?',
        SOLVED: True,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "E Woods",
        DESCRIPTION: 'trees boring stupid trees',
        EXAMINATION: 'some squirrels',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "start forest 1",
        DESCRIPTION: 'the tress are denser here',
        EXAMINATION: 'it\'s much cooler and quieter here',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },
    'b5': {
        ZONENAME: "deep forest 2",
        DESCRIPTION: 'thick with trees',
        EXAMINATION: 'those same blasted squirrels',
        SOLVED: False,
        UP: 'a5',
        DOWN: 'x',
        LEFT: 'b4',
        RIGHT: 'x',
    },
    'c1': {
        ZONENAME: "beach",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: 'x',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "swamp 1",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "north hills",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "north valley",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'x',
    },
    'c5': {
        ZONENAME: "secret cave",
        DESCRIPTION: 'You have found the secret cave there is a chest inside',
        EXAMINATION: "it's a cave with a treasure chest - use the key to open it",
        SOLVED: False,
        UP: 'x',
        DOWN: 'o',
        LEFT: 'x',
        RIGHT: 'x',
    },
    'd1': {
        ZONENAME: "marsh lands",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'e1',
        LEFT: 'x',
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "swamp 2",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "south hills",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'o',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "south valley",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'x',
        LEFT: 'd3',
        RIGHT: 'd5',
    },
    'd5': {
        ZONENAME: "soith castle side hills",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'o',
        DOWN: 'x',
        LEFT: 'd4',
        RIGHT: 'x',
    },
    'e1': {
        ZONENAME: "castle square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd1',
        DOWN: 'x',
        LEFT: 'x',
        RIGHT: 'e2',
    },
    'e2': {
        ZONENAME: "castle gate",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd2',
        DOWN: 'x',
        LEFT: 'e1',
        RIGHT: 'o',
    },
    'e3': {
        ZONENAME: "Castle guard room",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd3',
        DOWN: 'x',
        LEFT: 'e2',
        RIGHT: 'o',
    },
    'e4': {
        ZONENAME: "Castle hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'x',
        LEFT: 'e3',
        RIGHT: 'o',
    },
    'e5': {
        ZONENAME: "Castle throne room",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'x',
        DOWN: 'x',
        LEFT: 'e4',
        RIGHT: 'x',
    }
}

# game interactivity section


def print_location():
    print("@@_-_-_-_-_.................._-_-_-_-_-_-_-@@")
    print("WM_-_-_-_-_.................._-_-_-_-_-_-_-MW")
    print("# #    " + (zonemap[myPlayer.position][ZONENAME]) + "     # #")
    print('# _-_  ' + myPlayer.position.upper() + '   #')
    print('#  ' + (zonemap[myPlayer.position][DESCRIPTION]) + '   #')
    print("!!!!_-_-_-_-_.................._-_-_-_-_-_-_-!!!!")
    print("!!!!_-_-_-_-_.................._-_-_-_-_-_-_-!!!!")


def prompt():
    print("_-_-_-_-_.................._-_-_-_-_-_-_-")
    print('+                                       +')
    print('+      what would you like to do ?      +')
    print('+          options include :            +')
    print('+                                       +')
    print('+    move , go, travel, walk,           +')
    print('+    up   down   left   right           +')
    print('+                                       +')
    print('+   examine,inspect, interact, look,    +')
    print('+                                       +')
    print('+    and if all else fails try fight    +')
    print('+                                       +')
    print('+ or quit, exit, stop,    to end game   +')
    print("_-_-_-_-_.................._-_-_-_-_-_-_-")


    action = input(">")
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'exit', 'stop', 'esc', 'examine',
                          'where', 'attack','inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("unknown action typed, try again.\n")
        action = input(">")
    if action.lower() in ['quit', 'exit', 'stop', 'esc']:
        sys.exit()

    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())

    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())






def player_move(myAction):
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.position][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.position][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.position][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.position][RIGHT]
        movement_handler(destination)
    else:
        prin t("please enter a valid direction")
 
 
def movement_handler(destination):
    if destination == 'x':
        print("that way is blocked choose another direction")
    elif destination == 'o':
        map_unlock()
        pass
    else:
        myPlayer.position = destination
        print("\n" + "!! you have moved to " +
            destination + " on the map.  !!")
        print_location()


def player_examine(action):
    if zonemap[myPlayer.position][SOLVED]:
        print("nothing left here to do move to another zone")
    else:
        print("puzzle here or fight or somehting")


# GAME FUNCTIONALITY section




def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # here handle if puzzles solved, boss defeated, all zones explored....






###   load game


# # intro
#     intro1 = ".. your health is a number %i/%i " % (myPlayer.health, myPlayer.maxhealth)
#     intro2 = ".. your attacks deal out %i  hit points " % myPlayer.attack
#     intro3 = ".. you have solved %i  puzzles ..." % myPlayer.solves
#     intro4 = ".. Welcome back to warrior adventure ..\n"
#     intro5 = ".. I hope you are enjoying your time .. \n"




#### THE GAME BEGINS >>>>
### ENTER PLAYER NAME SET STORY


def set_up_game():
    os.system('clear')

    # what's in a name
    question1 = "Greetings stranger ... I'm the narrator for your story ... what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    player_name = input("==> ")
    if input == None:
        print("#! HEY _ YOU GOT A NAME RIGHT ? TYPE IT IN ... ")
        player_name = input("==> ")
    else:
        myPlayer.name = player_name

    question2 = "Hello, " + myPlayer.name + " welcome to the game .... \n"
    # need a job ?
    #question2 = "Hello, " + myPlayer.name + " what role do you want to play?\n"
    # question2add = " Choose: warrior , wizard, or thief ... \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)
    # for character in question2add:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.06)
    # player_job = input("==> ")
    # valid_jobs = ['warrior', 'wizard', 'thief']
    # while player_job.lower() not in valid_jobs:
    #     print('... choose: warrior, wizard, or thief ...')
    #     player_job = input("-->")
    #     if player_job.lower() in valid_jobs:
    #         myPlayer.job = player_job
    #         print("Greetings " + myPlayer.name +
    #               " The " + myPlayer.job + " .\n")

    # if myPlayer.job is 'warrior':
    #     self.health = 120
    #     self.magic = 20
    #     self.special = 'axe_swing'
    # if myPlayer.job is 'wizard':
    #     self.health = 50
    #     self.magic = 120
    #     self.special = 'fire_ball'
    # if myPlayer.job is 'thief':
    #     self.health = 80
    #     self.magic = 80
    #     self.special = 'sneak_out'


# intro
    intro1 = ".. your health is a number %i/%i " % (myPlayer.health, myPlayer.maxhealth)
    intro2 = ".. your attacks deal out %i  hit points " % myPlayer.attack
    intro22 = ".. you have solved %i  puzzles ..." % myPlayer.solves
    intro3 = ".. Welcome to warrior adventure ..\n"
    intro4 = ".. I hope you enjoy your time .. \n"
    intro5 = ".. when suddenly there was a noise ..\n"
    intro6 = ".. SSSSSSCCCCRRRRRCCCCHHHHHH!!!!!@$#<<|>> ..\n "
    intro7 = ".. oh no what was that awful screech ..\n"
    intro8 = ".. lets go see what the noise was ..\n"
    intro9 = " ...       . . .              ... "
    intro10 = " ...                ...              ...     ... "

    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in intro22:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in intro4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in intro5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in intro6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    for character in intro7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in intro8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in intro9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in intro10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.003)

    os.system('clear')
    print('!#######################################!')
    print('#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#')
    print('#$#                                   #$#')
    print('#$#                                   #$#')
    print('#$#           LETS BEGIN !!           #$#')
    print('#$#                                   #$#')
    print('#$#                                   #$#')
    print('#$#          game starts now          #$#')
    print('#$#                                   #$#')
    print('#$#                                   #$#')
    print('#$#                                   #$#')
    print('#$#                                   #$#')
    print('#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#')
    print('!#######################################!')
    main_game_loop()


title_screen()
