print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcom to Treasure Island.\nYour mission is to find the treasure.")
choise1 = input('You\'re at a cross read. Where do you want to go? '
                'Type "Left" or "Right"\n--->').lower()
if choise1 == "left":
    choise2 = input('You\'ve come to a lake, there is an island in the middle of the lake. '
                    'Type "wait" for wait for a boat. Type "swim" for swim a cross.').lower()
    if choise2 == "wait":
        choise3 = input(
            'You arrived at the island unharmed. There is house with 3 doors. One red, one yellow, one blue. Which colour do you choose?').lower()
        if choise3 == "red":
            print("It's a room full of fire.\nGeme Over!!!!")
        elif choise3 == "yellow":
            print("You found the treasure.\nYou Win!!!")
        elif choise3 == "blue":
            print("You enter a room of beasts.\nGeme Over!!!!")
        else:
            print("You chose a door that doesn't exist.\nGeme Over!!!!")
    else:
        print("You got attacked by an angry trout.\nGeme Over!!!")
else:
    print("You fell in to a hole.\nGeme Over!!!!")
