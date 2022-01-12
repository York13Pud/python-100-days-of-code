# Tuples look like a list but in () rather than [] and are accessed in a similar way:
my_tuple = (1, 2, 3)
print(my_tuple[0])

# The main difference with a tuple is that you cannot change an existing value once it is set.
# The below will produce an error indicating that the object (2) does not support reassignment:
my_tuple[2] = 4

# You cannot add or delete either. Think of it as WORM.
# This is classed as immutable.