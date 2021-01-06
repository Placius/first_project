# My first steps with learning Git and Github
# Find my number game

# import modules

import random

# drawing the winning number (1 - 100)

win_number = int(random.randint(1,100))

# creating a definition to getting number from user

def GetNumber():
    user_choice_number = int(input("Make your choice: "))
    return user_choice_number

# creating a game course
