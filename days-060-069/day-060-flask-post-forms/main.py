from crypt import methods
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form['name']
    password = request.form['password']
    
    return f"<h1>Name: {name}<br>Password: {password}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
