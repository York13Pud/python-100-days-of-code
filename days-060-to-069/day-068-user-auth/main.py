from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    if current_user.is_authenticated is True:
        return redirect(url_for("secrets"))
    else:
        return render_template("index.html", logged_in = current_user.is_authenticated)


@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        
        # --- Check if the user already exists in the database:
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("The email address entered already exists. Please try logging in instead!")
            return redirect(url_for('login'))

        # --- Create a new object for the new user:
        new_user = User(
            email = request.form.get("email"),
            password = generate_password_hash(password=request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
            name = request.form.get("name")
        )
        # --- Commit the new user to the database:
        db.session.add(new_user)
        db.session.commit()
        print(new_user.id)
        load_user(int(new_user.id))
        
        print(current_user.is_authenticated)
        return redirect(url_for("login"))
    
    else:
        return render_template("register.html", logged_in = current_user.is_authenticated)


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
            email = request.form.get('email')
            password = request.form.get('password')
        
            user = User.query.filter_by(email=email).first()
            # --- Check if email address is correct:
            if not user:
                flash("Email address is not valid.<br>Please try again.")
                return redirect(url_for('login'))
            # --- Check if password is correct:
            elif not check_password_hash(user.password, password):
                flash('Password address is not valid.<br>Please try again.')
                return redirect(url_for('login'))
            # --- If both are correct, proceed to login:
            else:
                login_user(user)
                return redirect(url_for('secrets'))
                
          
    return render_template("login.html", logged_in = current_user.is_authenticated)



@app.route('/secrets')
@login_required
def secrets():
    print(current_user.is_authenticated)
    return render_template("secrets.html", name=current_user.name, logged_in = current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(directory="static/files", path="cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
