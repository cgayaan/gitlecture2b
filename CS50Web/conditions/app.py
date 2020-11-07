import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    # the all_saints variable is a boolean so it returns true or false
    # check if month is November and the day is 1st
    all_saints = now.month == 11 and now.day == 1
    return render_template("index.html", all_saints = all_saints)
