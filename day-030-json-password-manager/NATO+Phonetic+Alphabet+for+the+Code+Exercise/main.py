import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# --- Define a function to ask for the user to type something,
# --- check that the input is in the dict and then print out.
# --- If the input is not in the dict, error and recurse the function again. 
def text_input_output():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]    
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        text_input_output()      
    else:
        print(output_list)

# Start the program
text_input_output()