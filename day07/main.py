from hangman_words import word_list
from hangman_art import logo, stages
import random


def game_is_over(winner: bool):
    if winner:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost!")


print(logo)

GAME_OVER = False
is_winner = False
UNDER_LINE_CHAR = '_'
TOTAL_CHANCE = 7
current_chance = TOTAL_CHANCE
guess = ""
correct_letters = []
word_to_guess = random.choice(word_list)

while not GAME_OVER:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in word_to_guess:
        if letter == guess:
            display += guess
            correct_letters += guess
        elif letter in correct_letters:
            display += letter
            if display == word_to_guess:
                is_winner = True
        else:
            display += UNDER_LINE_CHAR
    if current_chance == 0 or is_winner:
        GAME_OVER = True
    elif guess not in word_to_guess:
        print(stages[current_chance -1])
        current_chance -= 1
    print(current_chance)
    print(word_to_guess)
    print(display)

game_is_over(is_winner)
