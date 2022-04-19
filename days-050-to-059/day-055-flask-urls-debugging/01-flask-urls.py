# Import the required modules:
from flask import Flask


# Define a variable for the flask app:
app = Flask(__name__)


# Create a route to a page that will display Hello:
@app.route('/')
def hello_world():
    return '<h1>Hello!</h1>'


# Define some decorator functions to format HTML.
def make_bold(function_called_from):
    def bold_text():
        return f'<b>{function_called_from()}</b>'
    print(bold_text)
    return bold_text

def make_italic(function_called_from):
    def italic_text():
        return f'<em>{function_called_from()}</em>'
    print(italic_text)
    return italic_text

def make_underlined(function_called_from):
    def underlined_text():
        return f'<u>{function_called_from()}</u>'
    print(underlined_text)
    return underlined_text

def make_h1(function_called_from):
    def h1_text():
        return f'<h1 style="color:red">{function_called_from()}</h1>'
    print(h1_text)
    return h1_text


# Create a route to a page that will display Goodbye:
@app.route('/goodbye')
@make_h1
@make_bold
@make_italic
@make_underlined
def goodbye():
    return 'Goodbye!'


# You can use variables in the URL and pass them to the function to use. 
# To do this, the variable name is enclosed in <> and is a string by default.
# You can also add to the path after the variable name.
# For example:
@app.route('/queue/<string:name>/<int:number>')
def greeting(name, number):
    # You can add multiple HTML elements either in one line or by spliting the lines up using \
    return f'<h1 style="color:red">Hello, {name}! You are {number} in the queue.</h1>' \
            '<h2>Please wait</h2>' \
            '<img src="https://media.giphy.com/media/4SY40ExbxfyOyD91VI/giphy.gif">'
            

# Run the program if __name__ is the same as __main__:
if __name__ == "__main__":
    app.run(debug=True)