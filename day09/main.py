import Art

print(Art.logo)

print("Welcom to the Secret auction program.")

def the_winner(all_of_offers):
    max_bid = 0
    winner_name = ""
    for key in all_of_offers:
        if all_of_offers[key] > max_bid:
            max_bid = all_of_offers[key]
            winner_name = key
    return  max_bid, winner_name

offers = {}
while True:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    offers[name] = bid
    another_offer = input("Would you like to continue? (Y/N)").lower()
    if another_offer == "n":
        max_value , winner_name = the_winner(offers)
        print(f"The winner is {winner_name} and the bid is {max_value}")
        break
    print("\n" * 100)



















# student_scores = {
#     "hary": 91,
#     "mohammad":50,
#     "ahmad":10,
#     "amirali":24,
#     "gol":89
# }
#
# student_grades = {}
#
# for key in student_scores:
#     if student_scores[key] >= 90:
#         student_grades[key] = "Outstanding"
#     elif 81 < student_scores[key] < 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif 71< student_scores[key] < 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
#
# print(student_grades)





















