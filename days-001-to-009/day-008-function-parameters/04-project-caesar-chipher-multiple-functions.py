alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# count = 0


def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for charecter in plain_text:
        char_index = (alphabet.index(charecter))
        # print(char_index)
        new_char_point = char_index + shift_amount
        new_letter = alphabet[new_char_point]
        encoded_text += new_letter
    print(f"The encoded text is: {encoded_text}")

def decrypt(plain_text, shift_amount):
    decoded_text = ""
    for charecter in plain_text:
        char_index = (alphabet.index(charecter))
        # print(char_index)
        new_char_point = char_index - shift_amount
        # print(new_char_point)
        new_letter = alphabet[new_char_point]
        # print(new_letter)
        decoded_text += new_letter
    print(f"The decoded text is: {decoded_text}")

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# Index out of range due to the list only having 26 letters. 
# A simple workaround for this is to just duplicate the entries in the list.

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
