from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", posts=requests.get("https://api.npoint.io/c4d66f8279a9f91ab429").json(), year=datetime.now().year)


@app.route("/about")
def about():
    return render_template("about.html", year=datetime.now().year)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=datetime.now().year)


@app.route("/post/<num>")
def read_post(num):
    return render_template("post.html", post=requests.get("https://api.npoint.io/c4d66f8279a9f91ab429").json()[int(num) - 1], year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
