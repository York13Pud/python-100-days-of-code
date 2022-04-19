from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

all_books = []

# --- SQLite3 module method of using a database:
# import sqlite3

# --- Connect to the database. If it is not found, it will be created:
# db = sqlite3.connect("books-collection.db")

# --- Create a cursor to interact with the database:
# cursor = db.cursor()

# --- Create the books table:
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# --- Create a record in the books table:
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# --- SQLAlchemy method. This allows you to do SQL commands in a more Python friendly way.
# 
# from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# --- Create the table schema:
class BookCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
         return f'<Title: {self.title}, Author: {self.author}, Rating: {self.rating}>'

# --- Create the tableL
db.create_all()

# --- Define two variables, each for a book:
book_one = BookCollection(title="Nineteen Eighty-Four", author="George Orwell", rating=8)
book_two = BookCollection(title="A Tale of Two Cities", author="Charles Dickens", rating=7)

# --- Insert the two books, first by adding them to the session and then commiting the session contents.
db.session.add(book_one)
db.session.add(book_two)
db.session.commit()

# --- Delete a record by its id:
#book_to_delete = BookCollection.query.get(2)
#db.session.delete(book_to_delete)
#db.session.commit()

# --- Update a record by its id:
book_to_update = BookCollection.query.get(1)
book_to_update.rating = 9
db.session.commit()

# --- Read All Records:
all_books = BookCollection.query.all()
print(f"\033[1;32;40m{all_books}\033[1;37;40m")

# --- Read A Particular Record By Query:
book = BookCollection.query.filter_by(title="Nineteen Eighty-Four").first()
print(f"\033[1;32;40m{book}\033[1;37;40m")

@app.route('/')
def home():
    print(all_books)
    return render_template('index.html', books=all_books )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    elif request.method == "POST":
        all_books.append({
            "bookname": request.form['book_name'],
            "bookauthor": request.form['book_author'],
            "bookrating": request.form['book_rating']
        })
        return redirect(url_for('home'))

# Don't use debug mode. It causes issues with the table insert integrity checks for unique constraints.
if __name__ == "__main__":
    app.run()

