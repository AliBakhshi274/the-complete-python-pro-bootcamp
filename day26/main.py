import pandas

def set_data_to_dict() -> dict:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    return {row.letter: row.code for (index, row) in data.iterrows()}


data_to_dict = set_data_to_dict()
user_input = input("Enter a word: ")
user_input_to_list_of_letters = [letter.upper() for letter in user_input]

sample_names = [data_to_dict[letter] for letter in user_input_to_list_of_letters]
print(sample_names)

