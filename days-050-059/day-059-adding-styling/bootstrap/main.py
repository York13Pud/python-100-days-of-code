from flask import Flask, render_template, url_for, request
from post import Post
from smtpemail import send_email
import requests
import inspect

api_url = 'https://api.npoint.io/12b4bed61541bdc8f040'
api_call = requests.get(api_url)
api_call.raise_for_status()
results_json = api_call.json()


articles = []

for article in results_json:
    post_obj = Post(article["id"], article["title"], article["subtitle"], article["body"])
    articles.append(post_obj)

print(articles)
    
app = Flask(__name__)

# --- Files / folders used in all HTML files:
style_sheet_file = 'css/styles.css'
fav_icon_file = 'assets/favicon.ico'
js_script_file = 'js/scripts.js'
images_folder = 'assets/img/'

@app.route('/')
def home():
    return render_template('index.html', 
                           results = articles,
                           css_file = url_for('static', filename = style_sheet_file),
                           favicon = url_for('static', filename = fav_icon_file),
                           jscript = url_for('static', filename = js_script_file),
                           header_image = url_for('static', filename = f"{images_folder}{inspect.stack()[0][3]}-bg.jpg")
                           )

@app.route('/about')
def about():
    return render_template('about.html', 
                           css_file = url_for('static', filename = style_sheet_file),
                           favicon = url_for('static', filename = fav_icon_file),
                           jscript = url_for('static', filename = js_script_file),
                           header_image = url_for('static', filename = f"{images_folder}{inspect.stack()[0][3]}-bg.jpg")
                           )

@app.route('/post')
def post():
    return render_template('post.html', 
                           css_file = url_for('static', filename = style_sheet_file),
                           favicon = url_for('static', filename = fav_icon_file),
                           jscript = url_for('static', filename = js_script_file),
                           header_image = url_for('static', filename = f"{images_folder}{inspect.stack()[0][3]}-bg.jpg")
                           )

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        # Return the contact form page with no fields in the form filed out:
        return render_template('contact.html', 
                            css_file = url_for('static', filename = style_sheet_file),
                            favicon = url_for('static', filename = fav_icon_file),
                            jscript = url_for('static', filename = js_script_file),
                            header_image = url_for('static', filename = f"{images_folder}{inspect.stack()[0][3]}-bg.jpg"),
                            form_title = "Contact Me"
                            )
    
    elif request.method == 'POST':
        
        # Get the elements from the posted form:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        
        # Set the title of the page
        form_title = "Successfully Sent Message"    
        
        # Send an email
        send_email(to_email = "someone@somebody.com", 
                   email_subject = f"New Message from {name}", 
                   email_message = f"From: {name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}"
                   )
        
        # Return the contact form to show the message was sent
        return render_template('contact.html', 
                    css_file = url_for('static', filename = style_sheet_file),
                    favicon = url_for('static', filename = fav_icon_file),
                    jscript = url_for('static', filename = js_script_file),
                    header_image = url_for('static', filename = f"{images_folder}{inspect.stack()[0][3]}-bg.jpg"),
                    form_title = form_title
                    )


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    requested_post = None
    for article in articles:
        if article.id == blog_id:
            requested_post = article
    return render_template("post.html", 
                           post=requested_post,
                           css_file = url_for('static', filename = style_sheet_file),
                           favicon = url_for('static', filename = fav_icon_file),
                           jscript = url_for('static', filename = js_script_file),
                           header_image = url_for('static', filename = f"{images_folder}{inspect.stack()[0][3]}-bg.jpg")
                           )    


if __name__ == "__main__":
    app.run(debug=True)
