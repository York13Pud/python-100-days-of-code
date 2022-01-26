import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
# ===================================================================================

# --- First, import the data from the CSV file to a data frame:
nato_data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")

# --- Loop through the rows of a data frame to create a dictionary:
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# ===================================================================================

# --- Ask the user for their first name and covert it to uppercase:
name = input("What is your first name?: ").upper()

# --- Look for the letter in the nato_dict and add the code to the list:
name_letter_list = [nato_dict[letter] for letter in name]

# --- Print out the result:
print(name_letter_list)