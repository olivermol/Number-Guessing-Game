
import random
from statistics import mean, median, mode
import sys

#     1. Display an intro/welcome message to the player.
#     2. Store a random number as the answer/solution.
def start_game():
    print("Welcome to the Number Guessing Game! \n Lets get fun")
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
                print("{} is too high, try a lower number".format(answer))
                continue
            if answer < guessed_number:
                print("{} is too low, try a higher number".format(answer))
                continue
            else:
                answer_list.append(attempts)
                print("\n ***You are rock! You've figured out what was the guessed number!***")
                print("\n  ***  Your statics:  *** \n ========================== \n")
                
                print("-==WINNER NUMBER: ==- \n")
                print("Your WINNER NUMBER: {}".format(answer))
                print(f"Median of your attempts number is: {median(answer_list)}")
                print(f"Mode of your attempts number is: {mode(answer_list)}")
                print(f"Mean of your attempts is: {mean(answer_list)}")
                print("\n ========================== \n")
            
            
            
            while True:
                try:
                    new_game = input("\n Would you like to try again? \n (Please use 'y' = Yes or 'n' = No)")
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


                    
                    


            



#    Psuedo-code Hints
    
#     When the program starts, we want to:
#     ------------------------------------


    
#     4. Once the guess is correct, stop looping, inform the user they "Got it"
#          and show how many attempts it took them to get the correct number.
#     5. Save their attempt number to a list.
#     6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
#     7. Ask the player if they want to play again.
    
#     ( You can add more features/enhancements if you'd like to. )
    
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()