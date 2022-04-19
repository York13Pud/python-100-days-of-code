from flask import Flask, render_template
from post import Post
import requests

api_url = 'https://api.npoint.io/41ac539c14a4896092a0'
api_call = requests.get(api_url)
api_call.raise_for_status()
results_json = api_call.json()

articles = []

for article in results_json:
    post_obj = Post(article["id"], article["title"], article["subtitle"], article["body"])
    articles.append(post_obj)
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', results = articles)

@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    requested_post = None
    for article in articles:
        if article.id == blog_id:
            requested_post = article
    return render_template("post.html", post=requested_post)    

if __name__ == "__main__":
    app.run(debug=True)
