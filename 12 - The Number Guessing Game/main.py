from art import logo
import random
from replit import clear

def guess_the_number():
    guess_this = random.randit(1,100)
    print("Welcome to: ")
    print(logo)
    print("I'm thinking of a number between 1 and 100, try to guess it")
    difficulty = input("Chose a difficulty. Tpe 'easy' or 'hard': ")
    if difficulty == "easy":
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5
    
    while guesses > 0:
        if guesses > 1:
            print(f"You have {guesses} guesses left for the number that I'm thinking of.")
        else:
            print(f"Last try to guess the number that I'm thinking of.")
        attempt = int(input("Take you guess: "))
        if attempt > guess_this:
            print("Too high")
        elif attempt < guess_this:
            print("Too low")
        if guesses == 1:
            print("Game Over")
        elif attempt == guess_this:
            def game_over():
                print(f"Correct: The answer was {guess_this}. Thanks for completing that!")
                return guesses - guesses
        guesses -= 1

    play_again = input("\n Do you want to play again? Type 'y' if yes and 'n'n to quit")
    if play_again == 'y':
        clear()
        guess_the_number()
    else:
        print("Goodbye!")

guess_the_number()
              

