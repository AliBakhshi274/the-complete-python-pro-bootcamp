import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 0 1 2
# 0->rock 1->paper 2->scissors

user_choice = int(input("What do you choose? (0 for Rock, 1 for paper, 2 for scissors).\n---> "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid choice!!!")

# Computer

print("Computer chose: ")
computer_random_choice = random.randint(0, 2)
if computer_random_choice == 0:
    print(rock)
elif computer_random_choice == 1:
    print(paper)
else:
    print(scissors)

# Calc

if computer_random_choice == user_choice:
    print("Draw!")
elif ((user_choice == 0 and computer_random_choice == 2) or
      (user_choice == 1 and computer_random_choice == 0) or
      (user_choice == 2 and computer_random_choice == 1)):
    print("You win!")
else:
    print("You lose!")
