TO_BE_REPLACED = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    list_of_names = invited_names.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    original_letter = starting_letter.read()

for name in list_of_names:
    if TO_BE_REPLACED in original_letter:
        replacement = original_letter.replace(TO_BE_REPLACED, name.strip())
        print(replacement)
        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as ready_to_send:
            ready_to_send.write(replacement)



