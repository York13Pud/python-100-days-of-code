# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt.
#
# Replace the [name] placeholder with the actual name.
#
# Save the letters in the folder "ReadyToSend".

# --- Read list of invitees and put the invitees into a list as individual items:
with open("./Input/Names/invited_names.txt") as intivee_file:
    invited = intivee_file.readlines()

# --- Read the invite template to a reusable variable:
with open("./Input/Letters/starting_letter.txt") as letter_template_file:
    letter_template = letter_template_file.read()

# --- Create a letter for each person on the invite list:
for name in invited:
    # --- We need to remove the \n from each persons entry in the list:
    name = name.strip("\n")
    # --- Perform a replace of [name] with the persons name:
    invite_letter = letter_template.replace("[name]", name)
    # --- Write the invite out for each person:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invite_output:
        invite_output.write(invite_letter)