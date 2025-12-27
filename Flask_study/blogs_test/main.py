from flask import Flask, render_template, abort
import requests


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/5ce2f239c7c10cd4c436")
    data = response.json()
    return render_template("index.html", data=data)
@app.route('/posts/<post_id>')
def get_blog_posts(post_id):
    response = requests.get("https://api.npoint.io/5ce2f239c7c10cd4c436")
    data = response.json()
    if response.status_code != 200:
        abort(500)
    dataset = next((posts for posts in data if posts['id'] == int(post_id)), None)
    if dataset is None:
        abort(404)
    return render_template("post.html", title=dataset['title'], subtitle=dataset['subtitle'], content=dataset['body'])

if __name__ == "__main__":
    app.run(debug=True)
