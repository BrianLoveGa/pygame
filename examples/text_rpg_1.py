# python text rpg. based on youtube tutorial Bryan Tong
# https://www.youtube.com/watch?v=xHPmXArK6Tg&t=46s

# adapted and modified By: Brian Loveless

# imports if stand-alone python fikle
import cmd
import textwrap
import sys
import os
import time
import random

# for game

screen_width = 100

# basic start player setup


class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.health = 0
        self.magic = 0
        self.status_effects = []
        self.position = 'b2'
        self.game_over = False
        self.solves = 0

# create basic


myPlayer = player()

# title screen


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        set_up_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.... play, help, or quit")
        option = input("> ")
        if option.lower() == ("play"):
            set_up_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print()
    print('###################################')
    print('###################################')
    print("#  Welcome to Brians text RPG game")
    print('###################################')
    print('###################################')
    print()
    print('            _-_ Play _-_           ')
    print('            _-_ Help _-_           ')
    print('            _-_ Quit _-_           ')
    print()
    print('###################################')
    print()
    print('        copyright 2019 B-Love      ')
    print()
    print('###################################')
    title_screen_selections()


def help_menu():
    os.system('clear')
    print('#######################################')
    print("#   Welcome to Brians text RPG game   #")
    print('#######################################')
    print()
    print('            --> HELP <--               ')
    print('                                       ')
    print(' -- Use up, down, left, right to move  ')
    print('  -- or north, south, east, west       ')
    print()
    print(' -- just type your commands            ')
    print(' -- to do them                         ')
    print()
    print(' -- use "look" to inspect something    ')
    print('                                       ')
    print('                                       ')
    print(' -- Good luck brave warrior            ')
    print('#######################################')
    title_screen_selections()


# game map   ---  player start @ b2
#
#       a1       a2        a3      a4     a5
#   ________|__________|________|_______|_______|_
#   |  town |   town   |   town | town  | town  |
#   |factory|  enter   |  hall  | square| shops |   a5
#  _|_______|__________|________|_______|_______|_
#   | woods |          | woods  |       |       |
#   |       |  start   |        |forest |forest |   b5
#  _|_______|__________|________|_______|_______|_
#   |       |          |        |       |       |
#   | swamp |  swamo   | hill   |valley |  cave |   c5
#  _|_______|__________|________|_______|_______|_
#   |       |swamp     |        |       |       |
#   | marsh |          | hill   |valley | hills |   d5
#  _|_______|__________|________|_______|_______|_
#   |castle |  castle  | castle | castle| castle|
#   | gate  | entrance | guard  | hall  | throne|   e5
#  _|_______|__________|__room__|_______|_room  |_
#   |       |          |        |       |       |
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
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
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
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a5',
    },
    'a5': {
        ZONENAME: "Town Shops",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "west woods",
        DESCRIPTION: 'a few shabby trees',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "Home start base",
        DESCRIPTION: 'This is your home - starting point',
        EXAMINATION: 'it\'s a nice place, but not great let\'s get out and go explore maybe the town up north?',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "Woods",
        DESCRIPTION: 'trees boring stupid trees',
        EXAMINATION: 'some squirrels',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "start forest",
        DESCRIPTION: 'the tress are denser here',
        EXAMINATION: 'it\'s much cooler and quieter here',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },
    'b5': {
        ZONENAME: "east forest",
        DESCRIPTION: 'thick with trees',
        EXAMINATION: 'those same blasted squirrels',
        SOLVED: False,
        UP: 'a5',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'c5',
    },
    'c5': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b5',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: '',
    },
    'd1': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'e1',
        LEFT: '',
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'e3',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'e4',
        LEFT: 'd3',
        RIGHT: 'd5',
    },
    'd5': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c5',
        DOWN: 'e5',
        LEFT: 'd4',
        RIGHT: '',
    },
    'e1': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'e2',
    },
    'e2': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd2',
        DOWN: '',
        LEFT: 'e1',
        RIGHT: 'e3',
    },
    'e3': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd3',
        DOWN: '',
        LEFT: 'e2',
        RIGHT: 'e4',
    },
    'e4': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd4',
        DOWN: '',
        LEFT: 'e3',
        RIGHT: 'e5',
    },
    'e5': {
        ZONENAME: "A1 saucy",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd5',
        DOWN: '',
        LEFT: 'e4',
        RIGHT: '',
    }
}

# game interactivity section


def print_location():
    print('\n' + ('#' * (10 + len(myPlayer.position))))
    print(('#' * (4 + len(myPlayer.position))))
    print('# _-_ ' + myPlayer.position.upper() + ' #')
    print('# ' + (zonemap[myPlayer.position][DESCRIPTION]) + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.position))))
    print(('#' * (10 + len(myPlayer.position))))


def prompt():
    print('\n' + '+' * (4 + len(myPlayer.position)))
    print('\n' + '+' * (4 + len(myPlayer.position)))
    print('+     what would you like to do ?      +')
    print('+         options include :            +')
    print()
    print('+   move , go, travel, walk, examine   +')
    print('+  inspect, interact, look, and quit   +')
    print('\n' + '+' * (4 + len(myPlayer.position)))
    print('\n' + '+' * (4 + len(myPlayer.position)))
    action = input(">")
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'exit', 'stop', 'esc', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("unknown action typed, try again.\n")
        action = input(">")
    if action.lower() in ['quit', 'exit', 'stop', 'esc']:
        sys.exit()

    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())

    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

    # if action.lower()
    # if action.lower()


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
        print("please enter a valid direction")


def movement_handler(destination):
    if destination == '':
        print("that way is blocked choose another direction")
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


def set_up_game():
    os.system('clear')

    # what's in a name
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    player_name = input(">")
    myPlayer.name = player_name

    # need a job ?
    question2 = "Hello, " + myPlayer.name + " what role do you want to play?\n"
    question2add = " Choose: warrior , wizard, or thief ... \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    for character in question2add:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    player_job = input(">")
    valid_jobs = ['warrior', 'wizard', 'thief']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("Greetings " + myPlayer.name + " The " + myPlayer.job + " .\n")
    while player_job.lower() not in valid_jobs:
        player_job = input(">")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("Greetings " + myPlayer.name +
                  " The " + myPlayer.job + " .\n")

    if myPlayer.job is 'warrior':
        myPlayer.health = 120
        myPlayer.magic = 20
        myPlayer.status_effects = ['axe_swing']
    if myPlayer.job is 'wizard':
        myPlayer.health = 50
        myPlayer.magic = 120
        myPlayer.status_effects = ['fire_ball']
    if myPlayer.job is 'thief':
        myPlayer.health = 80
        myPlayer.magic = 80
        myPlayer.status_effects = ['sneak_out']


# intro
    intro1 = f".. your health is a number"  " hp ! ..\n"
    intro2 = f".. your magic is a different number" " mp ! ..\n"
    intro3 = ".. Welcome to Ye Olde Wooden Stock ..\n"
    intro4 = ".. I hope you enjoy your time .. \n"
    intro5 = ".. when suddenly there was a noise ..\n"
    intro6 = ".. SSSSSSCCCCRRRRRCCCCHHHHHH!!!!!@$#<<|>> ..\n "
    intro7 = ".. oh no what was that awful screech ..\n"
    intro8 = ".. lets go see what the noise was ..\n"
    intro9 = " ...                           ... "
    intro10 = " ...                           ... "

    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in intro2:
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
        time.sleep(0.04)

    os.system('clear')
    print("#$#$#$#$#$#$#$#$#$#$#$#$#")
    print('#$#                   #$#')
    print('#$#                   #$#')
    print('#$#     LETS BEGIN    #$#')
    print('#$#                   #$#')
    print('#$#                   #$#')
    print('#$#  game starts now  #$#')
    print('#$#                   #$#')
    print("#$#$#$#$#$#$#$#$#$#$#$#$#")
    main_game_loop()


title_screen()
