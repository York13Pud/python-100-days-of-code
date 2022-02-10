# # To perform movements using turtle, we make use of turtle event listeners.
# # This allows you to move something on the screen using the keyboard arrow keys.
# # Note: Look under screen listeners in the documentation.

# from turtle import Turtle, Screen, reset

# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

# Higher order functions are functions that work with other functions. For example:

# --- Define a basic function to add two values together:
def add(n1, n2):
    return n1 + n2

# --- Define another function that will take n1, n2 and the name of another function
# --- This is the higher order function as it gets the name of another function passed to
# --- the func parameter from the result variable:
def calculator(n1, n2, func):
    # --- This will then call the function that was passed via the result variable and pass the
    # --- values of n1 and n2. In this example, it will add n1 and n2, return it to this function 
    # --- and then return it to result.
    return func(n1, n2)

# --- This will call the calculator function and pass the required arguments to it:
result = calculator(2, 3, add)

# --- This will print the returned value from result:
print(result)