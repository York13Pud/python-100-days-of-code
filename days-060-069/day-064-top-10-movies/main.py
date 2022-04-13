# --- Import the required modules and libraries
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


# --- Define the Flask / Bootstrap application:
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# --- SQLAlchemy database configuration:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# --- Define the table schema:
class TopTenMovies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
         return f'<Title: {self.title}>'


# --- Define a class for the edit movie details page:
class EditMovieForm(FlaskForm):
    rating = FloatField(label="Movie Rating", description="Movie Rating", validators=[DataRequired(message="Please enter a score between 1 and 10.")])
    review = StringField(label="Movie Review", description="Movie Review", validators=[DataRequired(message="Please enter a review")])
    submit = SubmitField(label="Update")


# --- Define a class to create a search form for a movie:
class SearchMovieForm(FlaskForm):
    title       = StringField(label="Movie Title", validators=[DataRequired(message="Please enter a name")])
    submit      = SubmitField(label="Add Movie")


# --- Define a class that is used to build the details for a movie the user selects:
class SelectMovie():
    def __init__(self, json_to_process):
        self.id             = json_to_process["id"]
        self.title          = json_to_process["title"]
        self.overview       = json_to_process["overview"]
        self.releasedate    = json_to_process["release_date"]
        self.rating         = json_to_process["vote_average"]
        self.img_url        = json_to_process["poster_path"]
    
    def __repr__(self):
         return f'<Title: {self.title}>'


# --- Define a variable that is used to store a list of found movie objects:
list_of_found_movies = []
    
# # --- Create the database / table:
# db.create_all()


def get_all_movies():
    """This function will retrieve all of the movies that are stored in the database."""
    global list_of_movies
    list_of_movies = TopTenMovies.query.order_by(TopTenMovies.rating.desc()).all()
    print(f"\033[1;32;40m{list_of_movies}\033[1;37;40m")
    return list_of_movies


@app.route("/")
def home():
    """This function is the main index page for the application"""
    get_all_movies()
    return render_template("index.html", movies=list_of_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """This function is used to edit the rating and """
    form = EditMovieForm()
    movie_id = request.args.get("id")
    movie = TopTenMovies.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    """This function will delete a record from the database. 
    Requires an id to be passed in the URL that matches a records id in the database."""
    movie_id = request.args.get("id")    
    movie_to_delete = TopTenMovies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    get_all_movies()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET","POST"])
def add():
    """This function will present a form for the user to enter a movie name into.
    It will then pass that to the select_movie function."""
    form = SearchMovieForm()
    if form.validate_on_submit():
        return redirect(url_for("select_movie", title=form.title.data))
    return render_template("add.html", form=form)
        

@app.route("/select", methods=["GET", "POST"])
def select_movie():
    """This function will take the movie name that the user searched for and
    make an API call to the movies site. The response is then presented as a 
    list of names and dates as hyperlinks for the user to select from. The
    link will call the find function and pass through the data needed."""
    global list_of_found_movies
    
    # --- Get the name of the movie to search from the add form:
    movie_search_name = request.args.get("title")

    # --- Define the variables and parameters need for the API call:
    movie_search_api_key = "enter api key"
    movie_search_api_url = f"https://api.themoviedb.org/3/search/movie"
    movie_search_api_params = {
        "api_key": movie_search_api_key,
        "language": "en-US",
        "query": movie_search_name
    }
        
    # --- Execute the API call to get the movie data:
    movie_search_api_call = requests.get(url=movie_search_api_url, params=movie_search_api_params)

    # --- If an error occurs, this will print out the response and its meaning:
    movie_search_api_call.raise_for_status()

    # --- Format the response from the API call to json:
    data = movie_search_api_call.json()

    for movie in data["results"]:
        list_of_found_movies.append(SelectMovie(json_to_process=movie))
    
    return render_template("select.html", movies_found = list_of_found_movies)


@app.route("/find")
def find_movie():
    """This function will find the movie the user selected in the existing list of movies
    and then add it to the database. It will then take the user to the edit function to
    add a rating and a review."""
    global list_of_found_movies
    
    movie_id = request.args.get("id")
    print(movie_id)
    for movie in list_of_found_movies:
        if int(movie.id) == int(movie_id):
            print(movie.title)
            movie_to_add = TopTenMovies(title=movie.title, 
                                        year=movie.releasedate, 
                                        description=movie.overview,
                                        rating=movie.rating,
                                        ranking="1",
                                        review="To update",
                                        img_url=f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2/{movie.img_url}")
            db.session.add(movie_to_add)
            db.session.commit()
            list_of_found_movies = []
            return redirect(url_for("edit", id=movie_to_add.id))
    return redirect(url_for('select_movie'))
    

# --- Run the application:
if __name__ == '__main__':
    app.run(debug=True)