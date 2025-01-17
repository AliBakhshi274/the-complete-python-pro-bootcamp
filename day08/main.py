import copy
from art import logo

def encode_operation(shift_to_left, text, alphabet) -> str:
    temp = ""
    bkup_alphabet = copy.deepcopy(alphabet)
    for i in range(shift_to_left):
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

if direction == ENCODE:
    print("encoding....")
    print(f"Encoded text is: {encode_operation(shift, text, alphabet)}")

elif direction == DECODE:
    print("decoding....")

else:
    print("enter a valid direction!!!")

















