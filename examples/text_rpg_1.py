# python text rpg. based on youtube tutorial Bryan Tong
# https://www.youtube.com/watch?v=xHPmXArK6Tg&t=46s

# adapted and modified By: Brian Loveless

### imports if stand-alone python fikle
import cmd
import textwrap
import sys
import os
import time
import random

## for game

screen_width = 100

###### basic start player setup 

class player:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.magic = 0
        self.status_effects = []
        self.location = 'start'
        
#create basic

myPlayer = player()

####### title screen

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # coming soon
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
