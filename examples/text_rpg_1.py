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
        self.health = 0
        self.magic = 0
        self.status_effects = []
        self.location = 'start'

# create basic


myPlayer = player()

# title screen


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()  # coming soon
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.... play, help, or quit")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()  # coming soon
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
    print()
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







# GAME FUNCTIONALITY

def start_game():




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
#   |       |          |        |       |       |   c5
#  _|_______|__________|________|_______|_______|_ 
#   |       |          |        |       |       |
#   |       |          |        |       |       |   d5
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

solved_places = {'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False, 'a5' : False,
                 'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False, 'b5' : False,
                 'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False, 'c5' : False, 
                 'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False, 'd5' : False, 
                 'e1' : False, 'e2' : False, 'e3' : False, 'e4' : False, 'e5' : False,  
                 }


zonemap = [
    'a1' : {
        ZONENAME:"Town factory",
        DESCRIPTION:'Where they make the sauce',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '',
        DOWN = 'b1',
        LEFT = '', 
        RIGHT = 'a2',
    },
        'a2' : {
        ZONENAME:"Town Entrance",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '', 
        DOWN = 'b2', 
        LEFT = 'a1',
        RIGHT = 'a3', 
    },
        'a3' : {
        ZONENAME:"Town Hall",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '', 
        DOWN = 'b3', 
        LEFT = 'a2', 
        RIGHT = 'a4',
    },
        'a4' : {
        ZONENAME:"Town Square",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '', 
        DOWN = 'b4', 
        LEFT = 'a3', 
        RIGHT = 'a5', 
    },
        'a5' : {
        ZONENAME:"Town Shops",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '', 
        DOWN = 'b5', 
        LEFT = 'a4', 
        RIGHT = '', 
    },
        'b1' : {
        ZONENAME:"west woods",
        DESCRIPTION:'a few shabby trees',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a1', 
        DOWN = 'c1', 
        LEFT = '', '
        RIGHT = 'b2', 
    },
        'b2' : {
        ZONENAME:"Home start base",
        DESCRIPTION:'This is your home - starting point',
        EXAMINATION = 'it\'s a nice place, but not great let\'s get out and go explore maybe the town up north?'
        SOLVED = False
        UP = 'a2',
        DOWN = 'c2',
        LEFT = 'b1',
        RIGHT = 'b3',
    },
        'b3' : {
        ZONENAME:"Woods",
        DESCRIPTION:'trees boring stupid trees',
        EXAMINATION = 'some squirrels'
        SOLVED = False
        UP = 'a3',
        DOWN = 'c3', 
        LEFT = 'b2',
        RIGHT = 'b4', 
    },
        'b4' : {
        ZONENAME:"start forest",
        DESCRIPTION:'the tress are denser here',
        EXAMINATION = 'it\'s much cooler and quieter here'
        SOLVED = False
        UP = 'a4', 
        DOWN = 'c4', 
        LEFT = 'b3', 
        RIGHT = 'b5', 
    },
        'b5' : {
        ZONENAME:"east forest",
        DESCRIPTION:'thick with trees',
        EXAMINATION = 'those same blasted squirrels'
        SOLVED = False
        UP = 'a5', 
        DOWN = 'c5', 
        LEFT = 'b4', 
        RIGHT = '', 
    },
        'c1' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'b1',
        DOWN = 'd1', 
        LEFT = '', 
        RIGHT = 'c2', 
    },
        'c2' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'b2', 
        DOWN = 'd2', 
        LEFT = 'c1', 
        RIGHT = 'c3', 
    },
        'c3' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'b3', 
        DOWN = 'd3', 
        LEFT = 'c2', 
        RIGHT = 'c4', 
    },
        'c4' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'b4', 
        DOWN = 'd4', 
        LEFT = 'c3', 
        RIGHT = 'c5', 
    },
        'c5' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'b5', 
        DOWN = 'd5', 
        LEFT = 'c4', 
        RIGHT = '',
    },
        'd1' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'c1',
        DOWN = 'e1', 
        LEFT = '', 
        RIGHT = 'd2', 
    },
        'd2' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'c2',
        DOWN = 'e2', 
        LEFT = 'd1', 
        RIGHT = 'd3',
    },
        'd3' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'c3',
        DOWN = 'e3', 
        LEFT = 'd2', 
        RIGHT = 'd4',
    },
        'd4' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'c4',
        DOWN = 'e4', 
        LEFT = 'd3', 
        RIGHT = 'd5',
    },
        'd5' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'c5',
        DOWN = 'e5', 
        LEFT = 'd4', 
        RIGHT = '',
    },
        'e1' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'd1',
        DOWN = '', 
        LEFT = '', 
        RIGHT = 'e2',
    },
        'e2' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'd2',
        DOWN = '', 
        LEFT = 'e1', 
        RIGHT = 'e3',
    },
        'e3' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'd3',
        DOWN = '', 
        LEFT = 'e2', 
        RIGHT = 'e4',
    },
        'e4' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'd4',
        DOWN = '', 
        LEFT = 'e3', 
        RIGHT = 'e5',
    },
        'e5' : {
        ZONENAME:"A1 saucy",
        DESCRIPTION:'description',
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'd5',
        DOWN = '', 
        LEFT = 'e4', 
        RIGHT = '',
    }
]
