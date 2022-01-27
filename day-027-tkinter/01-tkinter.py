import tkinter

def button_clicked():
    my_label.config(text=input.get())

# Create a new window (does nothing until you state it wait for a condition to match):
window = tkinter.Tk()

# Set the title for the window:
window.title("My Program")

# Set the size of the window:
window.minsize(width=300,height=300)

# Add padding to the window (can also do it for an element in the window as well):
window.config(padx=20, pady=20)

# Create a label in the window:
my_label = tkinter.Label(text="Some Text", font=("Ariel", 24, "bold"))

# Display the label on the screen with packer. By default, it will be centred at the top of the window area:
# side will move the label to the left centre of the screen and expand will make it the full width so it is centred.
# Pack has a lot more options available:
my_label.grid(row=0, column=0)

# To change the property(/ies) of something that is already created, you can override it at another point.
# For example, let's change the my_label text:
my_label["text"] = "Different Text"
# or
my_label.config(text="My Text")

# Creating a button:    
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Creating another button:    
button_two = tkinter.Button(text="Click Me Too", command=button_clicked)
button_two.grid(row=0, column=2)

# An input box is called an entry:
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)

# Window layout options:
# Pack is a very basic one that puts elements in am order that they are listed in the code, always starting at the top by default.

# Place is used for precise positioning on the window.
# my_label.place(x=0, y=150) # left centre.

# Grid is the best one to use. It uses a column, row format and is a relative layout
# my_label.grid(row=0, column=0)
#
# Note: You cannot mix grid and pack in the same program.

# Keeps the window on the screen and always has to be at the end of the program:
window.mainloop()