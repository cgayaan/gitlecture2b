from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
# hello function will get the name value from the html form
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
