import copy
from art import logo

def encode_decode_operation(shift, text, alphabet) -> str:
    temp = ""
    bkup_alphabet = copy.deepcopy(alphabet)
    for i in range(shift):
        temp += alphabet.pop(0)
    for i in range(len(temp)):
        alphabet += temp[i]

    encoded_text = ""
    index = 0
    i = 0
    while True:
        if len(text) == len(encoded_text) or i == len(alphabet):
            break
        elif text[index] == bkup_alphabet[i]:
            encoded_text += alphabet[i]
            index += 1
            i=0
        else:
            i += 1
    return encoded_text

ENCODE = '1'
DECODE = '2'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)

direction = input("Type '1' to encode or '2' to decode: ").lower()
text = input("Type your text: ").lower()
shift = int(input("Type the shift number: "))

while True:
    if direction == ENCODE:
        print("encoding....")
        print(f"The text has been 'Encoded': {encode_decode_operation(shift, text, alphabet)}")

    elif direction == DECODE:
        print("decoding....")
        shift_amount = len(alphabet) - shift
        print(f"The text has been 'Decoded': {encode_decode_operation(shift_amount, text, alphabet)}")

    user_choice = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if user_choice == "no":
        break

















