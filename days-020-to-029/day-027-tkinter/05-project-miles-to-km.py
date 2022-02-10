import tkinter
from tkinter import *

# --- Define a constant that is used for the window title and the program title:
PROG_NAME = "Miles to Kilometres Converter"

# --- define a function that take the miles and converts them to km's.
# --- It then updates equal_to_label with the converted km's:
def button_clicked():
    equal_to_label.config(text=f"is equal to: {(float(miles_entry.get()) * 1.61):.2f} Km's")

# --- Create a new window (does nothing until you state it wait for a condition to match):
window = tkinter.Tk()

# --- Set the title for the window:
window.title(PROG_NAME)

# --- Set the size of the window:
window.minsize(width=300,height=150)

# --- Add padding to the window:
window.config(padx=10, pady=20)

# --- Display a label with the program name:
title = tkinter.Label(text=PROG_NAME, font=("Ariel", 24, "bold"))
title.grid(row=0, column=0, columnspan=3, sticky="W")

# --- Display a text entry box to input the miles into:
miles_entry = tkinter.Entry(width=25, )
miles_entry.grid(row=1, column=0, sticky="W")
miles_entry.insert(END, string="Enter the number of miles")

# --- Display a label with Miles in it:
miles_label = tkinter.Label(text="Miles", font=("Ariel", 16, "normal"))
miles_label.grid(row=1, column=1, sticky="W")
miles_label.config(padx=0, pady=20)

# --- Display a button that, when clicked, will call the button_clicked function:
calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=2, column=0, sticky="W")

# --- Display a label with the converted km's in it. The default is 0. 
# --- It is updated when calculator_button is clicked:
equal_to_label = tkinter.Label(text="is equal to: 0 Km", font=("Ariel", 16, "normal"))
equal_to_label.grid(row=3, column=0, sticky="W")
equal_to_label.config(padx=0, pady=20)

# --- Keeps the window on the screen until the user closes the program:
window.mainloop()