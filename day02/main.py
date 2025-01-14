# Solution_1
# print("Welcom to the tip calculator!")
#
# bill = float(input("what was the total bill? "))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
#
# total_tip_amount = tip / 100 * bill + bill
# bill_per_person = total_tip_amount / people
# final_amount = round(bill_per_person, 2)
#
# print(f"Each person should pay ${final_amount}")
from json.encoder import py_encode_basestring_ascii

# Solution_2
print("Welcom to the tip calculator!")

bill = ""
tip = ""
people = ""

try:
    # get bill amount
    while True:
        bill = float(input("what was the total bill --> $"))
        if bill < 0:
            print("The bill can't be negative. Please enter a valid amount.")
        else:
            break

    # get tip amount
    while True:
        tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
        tip_amount_list = [10, 12, 15]
        if tip not in tip_amount_list:
            print("Please enter 10, 12 or 15.")
        else:
            break

    # get people
    while True:
        people = input("How many people to split the bill? ")
        list_of_invalid_input = ["", "0"]
        if not people.isdigit() or people in list_of_invalid_input:
            print("Please enter a valid amount!!!")
        else:
            people = int(people)
            break

except ValueError:
    print("Please enter a valid amount!")

total_amount: float = tip / 100 * bill + bill
total_amount_per_person = round(total_amount / people, 2)
print(f"Thank you for your bill. Your total amount is: ${total_amount_per_person}")
