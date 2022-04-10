from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

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
         return f"<BookCollection {self.title}>"


# --- Create the tableL
db.create_all()

# --- Update a record by its id:
# book_to_update = BookCollection.query.get(1)
# book_to_update.rating = 9
# db.session.commit()

# --- Print All Records:
def get_books():
    global all_books
    all_books = []
    all_books=BookCollection.query.all()
    print(f"\033[1;32;40m{all_books}\033[1;37;40m")
    return all_books

# --- Read A Particular Record By Query:
# book = BookCollection.query.filter_by(title="Nineteen Eighty-Four").first()
# print(f"\033[1;32;40m{book}\033[1;37;40m")

get_books()

@app.route('/')
def home():
    print(f"\033[1;32;40m{all_books}\033[1;37;40m")
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    
    elif request.method == "POST":
        book_to_add = BookCollection(title=request.form['book_name'], author=request.form['book_author'], rating=request.form['book_rating'])
        db.session.add(book_to_add)
        db.session.commit()
        get_books()
        return redirect(url_for('home'))


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        return render_template('delete.html', books=all_books)
    
    elif request.method == "POST":
        book_to_delete = BookCollection.query.get(request.form['book_id'])
        db.session.delete(book_to_delete)
        db.session.commit()
        get_books()
        return redirect(url_for('home'))


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        book = BookCollection.query.filter_by(id=id).first()
        return render_template('edit.html', book=book)
    
    elif request.method == "POST":
        book_to_update = BookCollection.query.get(id)
        book_to_update.rating = float(request.form['book_rating'])
        db.session.commit()
        get_books()
        return redirect(url_for('home'))

# Don't use debug mode. It causes issues with the table insert integrity checks for unique constraints.
if __name__ == "__main__":
    app.run()

