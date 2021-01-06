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

user_choice = None

while user_choice != win_number:
    try:
        user_choice = GetNumber()
        # possibilities of choices
        if user_choice == win_number:
            break

        elif user_choice > 100 or user_choice < 1:
            print("My number is only in ranges from 1 to 100...")
        
        elif user_choice < win_number:
            print("My number is higher...")
        
        elif user_choice > win_number:
            print("My number is lower...")

        else:
            print("Something goes wrong....")
    
    except ValueError:
        print("You must choose number from 1 to 100! TRY AGAIN!")
        continue

# End of the game and congratulations
