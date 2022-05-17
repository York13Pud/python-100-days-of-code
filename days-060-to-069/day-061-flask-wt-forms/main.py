# --- Import the required modules:
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length

# --- Create the application:
def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

# --- Set the secret key:
app.secret_key = "testing"

# --- Create the form and return it as an object:
class LoginForm(FlaskForm):
    email      = EmailField(label='Email:', description='email', validators=[Email(), DataRequired(message="Please enter a valid email address.")])
    # DataRequired make the field a required field and cannot be blank.
    password   = PasswordField(label='Password:', description='Password', validators=[DataRequired(message="Please enter a password."), Length(min=8)])
    submit     = SubmitField(label='Log In', button_map={'submit':'dark'})

# --- Create the route for the root of the site:
@app.route("/")
def home():
    return render_template("index.html")

# --- Create the route for the login page of the site:
@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    # validate_on_subnit() is True by default.
    if login_form.validate_on_submit():
        print(f"Username: {login_form.email.data}")
        print(f"Password: {login_form.password.data}")
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form = login_form)

# --- Run the application:
if __name__ == '__main__':
    app.run(debug=True)