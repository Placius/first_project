# My first steps with learning Git and Github
# Find my number game

# import modules

import random, os, time

# drawing the winning number (1 - 100)

win_number = int(random.randint(1,100))

# creating a definition to getting number from user

def GetNumber():
    user_choice_number = int(input("Make your choice: "))
    return user_choice_number

# creating a game course

user_choice = None

tries = 1

while user_choice != win_number:
    os.system("cls")
    try:
        print("Try nr", tries, "\n\n")
        user_choice = GetNumber()
        # possibilities of choices
        if user_choice == win_number:
            break

        elif user_choice > 100 or user_choice < 1:
            print("My number is only in ranges from 1 to 100...")
        
        elif user_choice < win_number:
            os.system("cls")
            print("My number is higher...")
            tries += 1
        
        elif user_choice > win_number:
            os.system("cls")
            print("My number is lower...")
            tries += 1

        else:
            print("Something goes wrong....")
    
    except ValueError:
        print("You must choose number from 1 to 100! TRY AGAIN!")
        continue

    time.sleep(2)

# End of the game and congratulations

os.system("cls")

print("Congratulations! \n\n\nMy number is", str(win_number) + "!","\n\nYou'll make it in", str(tries),"tries!", "\n\nSee you soon and have a nice day!")
    
time.sleep(4)