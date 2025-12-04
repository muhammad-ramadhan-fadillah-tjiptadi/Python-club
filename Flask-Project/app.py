from os import name
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/profile/<username>')
def show_profile(username):
    return render_template("profile.html", username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ID: %d' % post_id

if __name__ == '__main__':
    app.run(debug=True)