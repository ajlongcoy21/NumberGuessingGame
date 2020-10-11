"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
"""

import random

LOWER_RANGE = 1
UPPER_RANGE = 10

def display_intro():
    """
    Displays the intro message of the game
    """
    print("\n")
    print("*"*120)
    print("""
    Welcome to Number Guessing Game! We will generate a number (1-10) for you to guess until you
    get the correct answer. After each guess we will tell you if the random number is LOWER, HIGHER 
    or CORRECT. Good luck and have fun!
        """)
    print("*"*120)
    print("\n")

def generate_random_number():
    """
    Genrates the random number for the user to guess during the round
    """
    return random.randint(LOWER_RANGE,UPPER_RANGE)

def get_player_guess():
    """
    Asks the player for their guess and checks to make sure the guess is within the range.
    """
    try:
        player_guess = int(input("Please enter your guess for the random number: "))
    except ValueError:
        raise ValueError("Your entry was not a valid number. Please try again.")
    else:
        if player_guess < LOWER_RANGE or player_guess > UPPER_RANGE :
            raise ValueError("The number you have selected is out of range. Please try again.")
        else:
            return player_guess

def ask_to_play_again():
    """
    Asks the user if they want to play again
    """
    
    asking = True
    question = "Would you like to play again (Y/N): "

    while asking:
        player_answer = input(question)
        if player_answer.upper() == "N" or player_answer.upper() == "Y":
            asking = False
        else:
            question = "Sorry I did not understand your reply, would you like to play again (Y/N): "
    
    return player_answer.upper()

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    # Setup the game variables
    play_again = True
    high_score = 999
    player_guess_attempts = 0

    # Call the display_intro function
    display_intro()

    # Store random number as the answer/solution
    random_number = generate_random_number()

    # Loop to continuously promt the player for a guess
    while play_again:

        try:
            player_guess_attempts += 1
            player_guess = get_player_guess() 
        except ValueError as err:
            print("{}".format(err))
        else:

            # Check to see if the player guessed correctly
            # If player did not guess correctly, indicate if they need to guess higher or lower

            if player_guess == random_number :
                
                print("You have guessed the number in {} attempts! Congratulations :)".format(player_guess_attempts))

                # Check to see if the player set a new high score
                if player_guess_attempts < high_score:
                    high_score = player_guess_attempts
                
                # Ask the player if they want to play again
                player_response = ask_to_play_again()

                # If player wants to play again, setup variables for a new round
                # Else thank them for playing and end the game

                if player_response == "Y":
                    player_guess_attempts = 0
                    random_number = generate_random_number()
                    print("\n")
                    print("*"*120)
                    print("\nThe high score of this game is {}. Good luck trying to beat it!\n".format(high_score))
                    continue
                else:
                    print("\nThank you for playing. Hope to see you again soon!\n")
                    break
            elif player_guess < random_number :
                print("It's Higher")
            else:
                print("It's lower")
        


# Kick off the program by calling the start_game function.
start_game()