import  random
import art
import game_data
print(art.logo)


# Functions
def set_data():
    global person_1, person_2
    person_1 = random.choice(game_data.data)
    person_2 = random.choice(game_data.data)

def display():
    print(f"Compare A: {person_1[NAME]}, a {person_1[DESCRIPTION]}, from {person_1[COUNTRY]}")
    print(art.vs)
    print(f"Against B: {person_2[NAME]}, a {person_2[DESCRIPTION]}, from {person_2[COUNTRY]}")

def compare(person_a: dict, person_b: dict) -> bool:
    return person_a[FOLLOWER_COUNT] > person_b[FOLLOWER_COUNT]

def continue_or_end(user_choice):
    global GAME_OVER
    global score
    if user_choice == "a":
        if compare(person_1, person_2):
            score += 1
        else:
            GAME_OVER = True
    elif user_choice == "b":
        if not compare(person_1, person_2):
            score += 1
        else:
            GAME_OVER = True

def display_result():
    print(f"Your'r right! Current score: {score}")

def play():
    display()
    choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()
    continue_or_end(choice)

# Variables
person_1 = ""
person_2 = ""
score = 0
# keys of data
GAME_OVER = False
NAME = 'name'
FOLLOWER_COUNT = 'follower_count'
DESCRIPTION = 'description'
COUNTRY = 'country'

# Main body
while not GAME_OVER:
    set_data()
    play()
    if GAME_OVER:
        print(f"Sorry, That's wrong. Final score: {score}")
    else:
        display_result()
        print(art.logo)




























