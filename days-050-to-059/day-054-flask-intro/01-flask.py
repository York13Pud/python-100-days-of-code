# Import the required modules:
from flask import Flask

# Define a variable for the flask app:
app = Flask(__name__)

# Create a route to a page that will display Hello:
@app.route('/')
def hello_world():
    return '<h1>Hello!</h1>'

# Create a route to a page that will display Goodbye:
@app.route('/goodbye')
def goodbye():
    return '<h1>Goodbye!</h1>'

# Run the program if __name__ is the same as __main__:
if __name__ == "__main__":
    app.run()