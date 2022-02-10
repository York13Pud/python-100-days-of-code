# Addition:
print(2+2)

# Subtraction:
print(3-2)

# Multiplication:
print(2*2)

# Division (result is always a float for division):
print(4/2)

# Something to the power of something (exponent):
print(2**4)

# Python follows PEMDAS when performing maths:
# 1. Perentheses ()
# 2. Exponents **
# 3. Multiplication *
# 4. Division /
# 5. Addition +
# 6. Subtraction -

# Below equals 7.
print(3 * 3 + 3 / 3 - 3)

# Below equals 3.
print(3 * (3 + 3) / 3 - 3)

# Round a number:
print(round(8/3))

# Round a number to two decimal places:
print(round(8/3, 2))

# Round down (floor) to the next full integer
print(8//3)

# You can continue performing math operations on a variable by calling it again (applies to all math functions):
result = 4 / 2
result /= 2

# The ouput will be 1.0 (float as it is a division).
print(result)

# As it turns out, you can mix data types in a print function by using f-string by putting an f before the first string and then
# putting and a variable in {}:
test_data = 1
print(f"The value of test_data is: {test_data}")
