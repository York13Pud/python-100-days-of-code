# Import required modules:
from flask import Flask, render_template
from datetime import date
import random
import requests


# Define a variable for the flask app:
app = Flask(__name__)


# Create a route to a page that will display Hello:
@app.route('/')
def hello_world():
    current_year = date.today().year
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, current_year = current_year)


@app.route('/guess/<name>')
def guess_name(name):
    # --- Make the API calls to get the age and gender using the name:
    get_age = requests.get(url=f'https://api.agify.io?name={name}')
    get_gender = requests.get(url=f'https://api.genderize.io?name={name}')
    
    # --- Render the results as JSON:
    age_json = get_age.json()
    gender_json = get_gender.json()
    
    # --- Get the age and gender:
    age = age_json["age"]
    gender = gender_json["gender"]
    
    # --- Render the HTML with the name, age and gender being passed to it:
    return render_template('age_gender/guess.html', name = name, age = age, gender = gender)

    
@app.route('/blog')
def blog():
    api_url = 'https://api.npoint.io/41ac539c14a4896092a0'
    api_call = requests.get(api_url)
    api_call.raise_for_status()
    results_json = api_call.json()
    return render_template('blog/index.html', results = results_json)
    

# export FLASK_APP=server.py
# export FLASK_ENV=development

# Run the program if __name__ is the same as __main__:
if __name__ == "__main__":
    app.run(debug=True)