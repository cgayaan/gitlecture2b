from flask import Flask, render_template
# import flask from the Flask module
# import render template
app = Flask(__name__)
# create new web application of type Flask
@app.route("/")
# / means the default page, so when user goes to the default page, the function below is what should run
def index():
# render the index.html file which is inside the templates folder
    return render_template("index.html")
