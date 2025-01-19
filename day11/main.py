import art
import random

print(art.logo)

#Functions
def add(a, b):
    return a + b

def deal_a_card(key):
    cards_of_players[key].append(random.choice(cards))

def display_the_status():
    print(f"Your cards are: {cards_of_players[USER]}, "
          f"current score is: {add(cards_of_players[USER][0], cards_of_players[USER][1])}")
    print(f"Computer's first card: {cards_of_players[CPU][0]}")

def winner(userScore, CpuScore) -> str:
    if userScore > CpuScore and userScore < 21:
        return USER
    else:
        return CPU

def to_continue():
    deal_a_card(USER)
    display_the_status()


def to_end():
    temp = 0
    for score in cards_of_players[USER]:
        temp = add(score, temp)
    user_score = temp
    cpu_score = add(cards_of_players[CPU][0], cards_of_players[CPU][1])
    print(f"Your cards are: {cards_of_players[USER]}, "
          f"current score is: {user_score}")
    print(f"Computer's final card: {cards_of_players[CPU]}, "
          f"final score: {cpu_score}")
    print(f"The winner is {winner(user_score, cpu_score)}")

def play():
    # The first init
    cards_of_players[USER] = []
    cards_of_players[CPU] = []
    for i in range(2):
        deal_a_card(USER)
        deal_a_card(CPU)
    display_the_status()
    is_continue = input(f"Type 'y' to continue, type 'n' to quit: ").lower()
    if is_continue == "y":
        to_continue()
        to_end()
    else:
        to_end()

# Variables
USER = "user"
CPU = "cpu"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_of_players = {
    USER:[],
    CPU:[]
}

# Main body
while True:
    is_beginning = input("Do you want to play a game of Blackjack?(Y/N): ").lower()
    if is_beginning == "n":
        break

    print("\n" * 10)
    play()

















