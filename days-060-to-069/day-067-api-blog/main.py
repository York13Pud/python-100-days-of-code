from urllib import request
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

# --- Create the base Flask application:
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

ckeditor = CKEditor()
ckeditor.init_app(app)

Bootstrap(app)

# --- Connect to the database:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Define the table schema:
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# --- Define the required fields for the post creation / editing form:
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    """This is the base root for the webapp."""
    posts = BlogPost.query.all()
    for item in posts:
        print(item.id)
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    """This function is used to display the full contents of a blog post. Requires the posts id to passed as an integer."""
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods = ["GET", "POST"])
def new_post():
    """This function is used to create a new blog post."""
    currentdate = datetime.datetime.now().strftime("%B %d, %Y")
    form = CreatePostForm()
    if form.validate_on_submit():
        create_post = BlogPost(
            title = request.form.get("title"),
            subtitle = request.form.get("subtitle"),
            author = request.form.get("author"),
            img_url = request.form.get("img_url"),
            body = request.form.get("body"),
            date = currentdate
        )
        db.session.add(create_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
        
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """This function is used to edit the contents of a blog post. Requires the posts id to passed as an integer."""
    post = BlogPost.query.get(post_id)
    
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>", methods = ["GET"])
def delete_post(post_id):
    """This function will delete a record from the database. 
    Requires an id to be passed in the URL that matches a records id in the database."""
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about", methods=["GET"])
def about():
    """This function directs the user to the about page."""
    return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact():
    """This function directs the user to the contact page."""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)