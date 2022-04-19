# Import the required modules:
from flask import Flask
from random import randint


# Define a variable for the flask app:
app = Flask(__name__)


# Define a variable that will produce a random number between 0 and 9:
number_to_guess = randint(0,9)
print(number_to_guess)


# Create a route to a page that will display Hello:
@app.route('/')
def hello_world():
    return '<h1>Hello!</h1><h1>Guess a number between 0 and 9</h1>'\
           '<a href="/guess/0"><h2>Zero</h2></a>'\
           '<a href="/guess/1"><h2>One</h2></a>'\
           '<a href="/guess/2"><h2>Two</h2></a>'\
           '<a href="/guess/3"><h2>Three</h2></a>'\
           '<a href="/guess/4"><h2>Four</h2></a>'\
           '<a href="/guess/5"><h2>Five</h2></a>'\
           '<a href="/guess/6"><h2>Six</h2></a>'\
           '<a href="/guess/7"><h2>Seven</h2></a>'\
           '<a href="/guess/8"><h2>Eight</h2></a>'\
           '<a href="/guess/9"><h2>Nine</h2></a>'

          
@app.route('/guess/<guess>')
def your_guess(guess):
    guess = int(guess)
    if guess == number_to_guess:
        return f'<h1>{guess} is correct</h1>'
    elif guess > number_to_guess:
        return f'<h1>{guess} is too high</h1>'
    elif guess < number_to_guess:
        return f'<h1>{guess} is too low</h1>'

           
# Run the program if __name__ is the same as __main__:
if __name__ == "__main__":
    app.run(debug=True)