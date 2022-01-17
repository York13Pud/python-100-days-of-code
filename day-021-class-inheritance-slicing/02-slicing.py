# Slicing lists and tuples:

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("a", "b", "c", "d", "e", "f", "g")

# --- Print c to e:
print(piano_keys[2:5])

# --- Print the list from c to the end:
print(piano_keys[2:])

# --- Print the list upto position 5:
print(piano_keys[:5])

# --- Print from c to e in increments of 2:
print(piano_keys[2:5:2])

# --- Print from a to g in increments of 2:
print(piano_keys[::2])

# --- Print from g to a:
print(piano_keys[::-1])

# --- Print from position a to c:
print(piano_tuple[0:3])