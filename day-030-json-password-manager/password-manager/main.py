# --- Import the required modules / libraries
import json
import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# --- Define constants used:
TITLE = "Password Manager"

# --- Define a function to search the websites stored in the JSON file:
def search_details():
    try:
        with open("./data.json", mode="r") as data_file:
            data = json.load(data_file)
            found_website = website_entry.get()
            found_username = data[website_entry.get()]['username']
            found_password = data[website_entry.get()]['password']
            
    except FileNotFoundError:
        messagebox.showinfo(title=TITLE, message="No Data File Found")
    
    except KeyError:
        if found_website == "":
            messagebox.showinfo(title=TITLE, message="Please enter a website to search for.")
        else:
            messagebox.showinfo(title=TITLE, message=f"No entry found for {website_entry.get()}")
    
    else:            
        messagebox.showinfo(title=TITLE, message=f"The username and password for {found_website} is:\nUsername: {found_username}\nPassword: {found_password}")   


# --- Define a function to generate a random password:
def random_password():
    """This function will generate a random password with alphabet charecters, numbers and symbols, 
    add it to the password_entry box and copy the password to the clipboard. """
    
    # Clear the current password in the entry box:
    password_entry.delete(0,END)

    # Create lists that will contain the charecters used to generate a password:    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Create a blank list that will be used to store the charecters chosen for the password:
    password_list = []

    # Use list comprehension to get the random charecters and add them to the password_list:    
    password_list += ([random.choice(letters) for _ in range(random.randint(8, 14))])
    password_list += ([random.choice(symbols) for _ in range(random.randint(2, 6))])
    password_list += ([random.choice(numbers) for _ in range(random.randint(2, 6))])
    
    # Shuffle the charecters in the password_list list:
    random.shuffle(password_list)

    # Use the join function to add each charecter from the password_list to a string variable called password.
    # "" signifies no space between each charecter. " " would ass a space between each charecter:
    password = "".join(password_list)

    # Copy the password to the clipboard:
    pyperclip.copy(password)

    # Display the password in the password_entry box:
    password_entry.insert(0, password)
    

# --- Define a function to validate the entry boxes have data and write to a file when all is ok:
def save_to_file():
    """This function wil take all of the entries in the entry boxes, check if they are all populated 
    and if so, write them to a file and clear the website and password entry boxes. If one or more boxes are empty, 
    a messagebox will advise the user to check the boxes and not write to the file."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    
    # Check if the entry boxes are populated:
    if website == "" or username =="" or password == "":
        messagebox.showerror(title=TITLE, message="Please check that all of the boxes have been entered.")
    # If the entry boxes are populated, write the contents of each to a file and then delete the values
    # stored in website_entry and password_entry boxes.
    else:
        try:
            with open("./data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            new_file = {}
            with open("./data.json", mode="w") as data_file:
                json.dump(new_file, data_file)
            messagebox.showinfo(title=TITLE, message=f"The data.json file was missing but has been created. Please click add again.")
        else:            
            data.update(new_data)
            with open("./data.json", mode="w") as data_file:
                json.dump(data, data_file, indent = 4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                    
# --- Setup the UI for the password manager:

window = Tk()
window.title(TITLE)
window.config(padx=20, pady=20)
window.geometry("550x400")

canvas = Canvas(width=200, height=200)

background = PhotoImage(file="./logo.png")

# 100, 100 are positional, not the size.
canvas.create_image(110, 100, image=background)
canvas.grid(row=0, column=0, columnspan=3)


website_label = Label(text=f"Website:")
website_label.grid(row=1, column=0, sticky="E", pady=5)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W", pady=5)
website_entry.focus()

search_button = Button(text="Search", width=14, command=search_details)
search_button.grid(row=1, column=2,  sticky="W", pady=5)

username_label = Label(text=f"Email/Username:")
username_label.grid(row=2, column=0, sticky="E", pady=5)

username_entry = Entry(width=40, )
username_entry.grid(row=2, column=1, columnspan=2, sticky="W", pady=5)
username_entry.insert(END, string="username@mysite.com")

password_label = Label(text=f"Password:")
password_label.grid(row=3, column=0, sticky="E", pady=5)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W", pady=5)

gen_password_button = Button(text="Generate Password", width=14, command=random_password)
gen_password_button.grid(row=3, column=2,  sticky="W", pady=5)

add_button = Button(text="Add", width=37, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="W", pady=5)

window.mainloop()