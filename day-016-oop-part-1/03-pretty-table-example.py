# --- Import the PrettyTable class from the prettytable module:
from prettytable import PrettyTable

# --- Create a new object called "table" that uses the PrettyTable class:
table = PrettyTable()

# --- These are methods (functions) to add columns:
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

# --- These are attributes (variables), rather than methods
table.header = True
table.header_style = "upper"
table.align = "l"

# --- Display the table:
print(table)