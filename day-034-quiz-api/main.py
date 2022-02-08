# You can declare the type for a variable in the following ways:
age: int
name: str
height: float
is_human: bool

# The advantage is that later on, you can do type checks against your code when setting values to
# the previously defined variables. This stops type mismatch occuring. Think of it as a soft
# enforcement of a data type for a variable, which is similar to C but that is a hard enforcement
# of a type and cannot be changed once it is defined.

# -> bool is the expect output at the end of the function.
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    # If you return a non-bool, the call to the function will break and produce an odd result.
    return can_drive

if police_check(18):
    print("You may pass")
else:
    print("Pay a fine.")







