
import random
from statistics import mean, median, mode
import sys

#     1. Display an intro/welcome message to the player.
#     2. Store a random number as the answer/solution.
def start_game():
    print("Welcome to the Number Guessing Game!\nLets get fun")
    answer = 0
    attempts = 0
    answer_list = []
    guessed_number = random.randint(1, 100)

    while True:
        try:
            answer = int(input("\n What is your tip between 1 and 100? \n "))
            if answer not in range(0, 101):
                print("Message: Please, use number BETWEEN 1 and 100")
                continue
        except ValueError:
            print("Message: Please, use ONLY number between 1 and 100")
#   3. Continuously prompt the player for a guess.
#       a. If the guess greater than the solution, display to the player "It's lower".
#       b. If the guess is less than the solution, display to the player "It's higher".
        else:
            attempts += 1
            if answer > guessed_number:
                print(f"{answer} is too high, try a lower number")
                continue
            if answer < guessed_number:
                print(f"{answer} is too low, try a higher number")
                continue
            else:
#  4. Once the guess is correct, stop looping, inform the user they "Got it" 
# and show how many attempts it took them to get the correct number.
                answer_list.append(attempts)
                print("\n ========================== \n")
                print("\n *** You are rock! You've figured out what was the guessed number! ***")
                print("\n ========================== \n")
                print("\n  ***  Your statics:  *** \n ========================== \n")
# Statitics about attempts
# And show it median, mode and mean                
                print("-==WINNER NUMBER: ==- \n")
                print(f"Your WINNER NUMBER: {answer}")
                print(f"Median of your attempts number is: {median(answer_list)}")
                print(f"Mode of your attempts number is: {mode(answer_list)}")
                print(f"Mean of your attempts is: {mean(answer_list)}")
                print("\n ========================== \n")
            
            
# New game chooser
# If say "Yes" then start the game (and show last score)
# If say "No" then close the game            
            while True:
                try:
                    new_game = input("\n *** Would you like to try again? ***\n(Please use 'y' = Yes or 'n' = No) : ")
                    if new_game != 'y' or 'n':
                        raise ValueError
                except ValueError:
                    print("Message: Please use ONLY 'y' OR 'n' for answer")
                    if new_game == 'y':
                        print("You are unstopable! :) ")
                        print(f"Your last score is: {min(answer_list)} ")
                        guessed_number = random.randint(1, 100)
                        start_game()
                if new_game == 'n':
                    print("Thank you and have a nice day!")
                    sys.exit()


start_game()