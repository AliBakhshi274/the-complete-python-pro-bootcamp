print("Welcom to the Brand Name Generator.")

# Solution_1
# cityName: str = input("What's the name of the city you grew up in?\n---> ")
# petName: str = input("What's your pet's name?\n---> ")
# print("Your brand name could be " + cityName + " " + petName + "!" )


# Solution_2
# print("Your brand name could be " +
#       input("What's the name of the city you grew up in?\n---> ") +
#       " " +
#       input("What's your pet's name?\n---> ") +
#       "!")

# Solution_3 --> Error_Handling
cityName: str
petName: str

while True:
    print("What's the name of the city you grew up in?")
    cityName = input("--> ")
    if cityName.strip() == "":
        print("You haven't entered anything. Please try again.")
    else:
        break
while True:
    print("What's your pet's name?")
    petName = input("--> ")
    if petName.strip() == "":
        print("You haven't entered anything. Please try again.")
    else:
        break

print("Your brand name could be " + cityName + " " + petName + "!" )