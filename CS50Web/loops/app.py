from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie", "David"]
    # pass the full list of names to index.html web page
    return render_template("index.html", names = names)
