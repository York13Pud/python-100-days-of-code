from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def user_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    
    while True:
        shift = int(input("Type the shift number (upto 26):\n"))
        try:
            shift
        except:
            print('Please use numeric digits.')
            continue
        if shift > 26:
            print("The shift number is over 26. Please try again.")
            continue
        break
    caesar(plain_text = text, shift_amount = shift, shift_direction = direction)


def caesar(plain_text, shift_amount, shift_direction):
    final_text = ""
    for letter in plain_text:
        letter_index = (alphabet.index(letter))
        if shift_direction == "encode":
            new_letter_point = letter_index + shift_amount
        elif shift_direction == "decode":
            new_letter_point = letter_index - shift_amount
        new_letter = alphabet[new_letter_point]
        final_text += new_letter
    print(f"The {shift_direction}d text is: {final_text}")
    run_again = input("Would you like to run the cipher again? Yes or No?: ")
    run_again_loop = False
    while not run_again_loop:
        if run_again == "Yes" or run_again == "yes" or run_again == "YES" or run_again == "y" or run_again == "Y":
            user_input()
        else:
            run_again_loop = True
            print("Goodbye!")
            break

user_input()