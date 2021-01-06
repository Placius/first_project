# My first steps with learning Git and Github
# Find my number game

# import modules

import random, os, time

# drawing the winning number (1 - 100)

win_number = int(random.randint(1,100))

# getting number from user

def GetNumber():
    user_choice_number = int(input("Make your choice: "))
    return user_choice_number

# final points

def EndPoints(tries):
    max_points = 11

    if tries >= 10:
        print("Unfortunetly your score for end is 0.")
    
    else:
        print("Congratulations, you've got", max_points - tries, "points for the end results!")

# creating a game course

user_choice = None

tries = 1

selected_numbers = []

while user_choice != win_number:
    os.system("cls")
    try:
        print("Try nr", tries, "\n\n")
        user_choice = GetNumber()

        # possibilities of choices
        if user_choice == win_number:
            break

        elif user_choice > 100 or user_choice < 1:
            print("\nMy number is only in ranges from 1 to 100...")
        
        elif user_choice in selected_numbers:
            print("\nThis number was selected by you, please try another...")
        
        elif user_choice < win_number:
            print("\nMy number is higher...")
            tries += 1
        
        elif user_choice > win_number:
            print("\nMy number is lower...")
            tries += 1

        else:
            print("\nSomething goes wrong....")
    
    except ValueError:
        print("You must choose number from 1 to 100! TRY AGAIN!")

    time.sleep(2)

    # added user choice number to selectet numbers
    selected_numbers.append(user_choice)

# End of the game and congratulations

os.system("cls")

print("Congratulations! \n\n\nMy number is", str(win_number) + "!","\n\nYou'll make it in", str(tries),"tries!")

EndPoints(tries)
    
time.sleep(4)
