from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
# render more.html page that has more information
def more():
    return render_template("more.html")
