import art
import random


# Functions
def compare(user_guess) -> str:
    if user_guess == nbr_to_guess:
        global game_over
        game_over = True
        return f"You got it! The Answer was {user_guess}"
    elif user_guess > nbr_to_guess:
        return "Too high.\nGuess again."
    elif user_guess < nbr_to_guess:
        return "Too low.\nGuess again."

#Variables
EASY = '1'
HARD = '2'
game_over = False

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty level: ('1' for easy and '2' for hard) ").lower()
player_health = 0
nbr_to_guess = random.randint(1, 100)
print(nbr_to_guess)
if difficulty == EASY:
    player_health = 10
elif difficulty == HARD:
    player_health = 5

#Main

for chances in range(player_health, 0, -1):
    print(f"You have {chances} attempts remaining to guess the number.")
    guess= int(input("Make a guess: "))
    print(compare(guess))
    if game_over:
        break
    elif chances == 1:
        print(f"The number was {nbr_to_guess}.\nYou have run out of guesses, you lose.")












