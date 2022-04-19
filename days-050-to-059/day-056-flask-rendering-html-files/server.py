# Import required modules:
from flask import Flask, render_template

# Define a variable for the flask app:
app = Flask(__name__)


# Create a route to a page that will display Hello:
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('test/cv.html')

@app.route('/personal-site')
def personal_site():
    return render_template('personal-site/index.html')
# export FLASK_APP=server.py
# export FLASK_ENV=development

# Run the program if __name__ is the same as __main__:
if __name__ == "__main__":
    app.run(debug=True)